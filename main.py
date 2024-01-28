from fastapi import FastAPI, Response, Request
from app.apis.v1.router import app_router
import settings
import uvicorn
import logging
from utils.middlewares import cache_stats_enpoint
from time import perf_counter



app = FastAPI(title='CTR WEB API')


app.include_router(app_router, prefix='/api/v1')


@app.middleware("http")
async def track_request_stats(request: Request, call_next):
    start_time = perf_counter()
    response: Response = await call_next(request)
    process_time = perf_counter() - start_time
    cache_stats_enpoint(request.url.path, process_time)
    return response


@app.on_event("startup")
def on_startup():
    logging.config.dictConfig(settings.LOGGING)


@app.get("/ping/")
async def ping() -> dict:
    return {"ping": "pong"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
