from functools import wraps
import json
from redis_init import get_redis
from typing import Callable


def cash(key_template: str):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if not kwargs['redis']:
                raise ValueError("Redis instance is not provided")
            arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
            combined_args = {**dict(zip(arg_names, args)), **kwargs}
            try:
                key = key_template.format(**combined_args)
                redis = kwargs['redis']
                farm_entity_cache = await redis.get(key)
                if farm_entity_cache:
                    return json.loads(farm_entity_cache)
            except KeyError as e:
                raise ValueError(f"Missing value for key template: {e}")
            result = await func(*args, **kwargs)
            await redis.set(key, json.dumps(result))
            return result
        return wrapper
    return decorator