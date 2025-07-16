from aiocache import Cache, cached


@cached(ttl=60, cache=Cache.MEMORY)
async def get_expensive_data(key: str):
    # Placeholder for expensive data retrieval
    return f"Expensive data for {key}"
