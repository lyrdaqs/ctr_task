from time import perf_counter
from fastapi import Response, Request
from gateways.instances import redis_client


def cache_stats_enpoint(endpoint, process_time):
    redis_key = f"endpoint:{endpoint}"
    redis_client.hincrby(redis_key, "count", amount=1)
    redis_client.hincrbyfloat(redis_key, "total_time", amount=process_time)
    redis_client.rpush('response_times', process_time)