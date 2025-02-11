from redis_init import get_redis
from fastapi import Depends, APIRouter
from redis.asyncio import Redis  # Исправлено

test_redis = APIRouter()


@test_redis.post("/set/", response_model=None)
async def set_value(key: str, value: str, redis: Redis = Depends(get_redis)):
    await redis.set(key, value)
    return {"message": f"Key {key} set with value {value}"}


@test_redis.get("/get/")
async def get_value(key: str, redis: Redis = Depends(get_redis)):
    value = await redis.get(key)
    return {"message": f"Value for key {key}: {value}"}
