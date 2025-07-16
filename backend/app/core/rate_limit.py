from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request

limiter = Limiter(key_func=get_remote_address)


async def rate_limit(request: Request):
    return await limiter.limit("5/minute")(request)
