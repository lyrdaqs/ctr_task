import logging
from typing import List
from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute, APIRouter
from gateways.instances import mongo_conn, redis_client
from app.apis.v1 import schemas
import numpy as np


logger = logging.getLogger('app')
app_router = APIRouter(
    tags=['predict ctr']
)


@app_router.post("/predict", response_model=List[schemas.AdResponse])
async def get_estimated_cvr_by_ads(request: schemas.AdRequest):
    ad_ids = request.adIdList
    ads_data = []
    for ad_id in ad_ids:
        try:
            cvr = redis_client.get(ad_id)
            if cvr:
                cvr = cvr.decode('utf-8')
                ads_data.append({'adId': ad_id, 'estimatedCVR': cvr})
            else:
                ads = mongo_conn.get_documents_by_ids([ad_id])
                if len(ads) != 0:
                    ads_data.append(ads[0])
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    return ads_data



@app_router.get("/stats")
async def get_endpoint_stats():
    stats = {}
    key = "endpoint:/api/v1/predict"
    endpoint = key.split(":")[-1]
    try:
        count = int(redis_client.hget(key, "count") or 0)
        total_time = float(redis_client.hget(key, "total_time") or 0)
        avg_time = total_time / count if count > 0 else 0
        response_times = redis_client.lrange('response_times', 0, -1)
        response_times = [float(response_time.decode()) for response_time in response_times]
        percentile_99 = np.percentile(response_times, 99)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    stats[endpoint] = {"count": count, "avg_response_time": avg_time, 
                       'percentile_99': percentile_99}
    return stats


