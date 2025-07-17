from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request, HTTPException
import time
from collections import defaultdict

limiter = Limiter(key_func=get_remote_address)

# Simple in-memory rate limiting for development
request_counts = defaultdict(list)
RATE_LIMIT = 5  # requests per minute


async def rate_limit(request: Request):
    """Simple rate limiting dependency"""
    client_ip = get_remote_address(request)
    current_time = time.time()
    
    # Clean old requests (older than 1 minute)
    request_counts[client_ip] = [
        req_time for req_time in request_counts[client_ip] 
        if current_time - req_time < 60
    ]
    
    # Check if rate limit exceeded
    if len(request_counts[client_ip]) >= RATE_LIMIT:
        raise HTTPException(
            status_code=429, 
            detail="Rate limit exceeded. Please try again later."
        )
    
    # Add current request
    request_counts[client_ip].append(current_time)
    return True
