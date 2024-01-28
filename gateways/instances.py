from gateways.mongo import MongoConnection
import redis
import settings


mongo_conn = MongoConnection(settings.DATABASE_NAME, settings.APP_COL)
redis_client = redis.Redis(host=settings.REDIS_HOST, port=6379, db=0)
