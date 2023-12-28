from os import getenv

from redis import Redis


REDIS = Redis(host=getenv("REDIS_HOST"), port=getenv("REDIS_PORT"), db=0, decode_responses=True)
