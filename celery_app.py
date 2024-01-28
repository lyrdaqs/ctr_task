from gateways.instances import mongo_conn, redis_client
from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger
import redis
import settings


app = Celery('tasks', broker=settings.REDIS_URL, backend=settings.REDIS_URL)
logger = get_task_logger(__name__)


@app.task(name="update_cache")
def update_cache():
    cursor = mongo_conn.export()
    for document in cursor:
        redis_client.set(int(document['adId']), document['estimatedCVR'])


app.conf.beat_schedule = {
    'update-cache-every-minute': {
        'task': 'update_cache',
        'schedule': 60.0,
    },
}
