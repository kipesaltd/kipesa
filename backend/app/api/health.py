from fastapi import APIRouter
from app.db.health import check_database_connection, get_connection_info

router = APIRouter()


@router.get("/health")
async def health_check():
    """Basic health check endpoint."""
    return {"status": "healthy", "message": "API is running"}


@router.get("/health/db")
async def database_health_check():
    """Database health check endpoint."""
    is_healthy = await check_database_connection()
    if is_healthy:
        return {"status": "healthy", "database": "connected"}
    else:
        return {"status": "unhealthy", "database": "disconnected"}


@router.get("/health/db/info")
async def database_info():
    """Get detailed database connection information."""
    return await get_connection_info() 