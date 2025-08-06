from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.db.health import check_database_connection, get_connection_info
from app.core.performance import get_performance_summary

router = APIRouter()


@router.get("/health")
async def health_check():
    """Basic health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow(),
        "service": "kipesa-api"
    }


@router.get("/health/database")
async def database_health_check(db: AsyncSession = Depends(get_db)):
    """Database health check endpoint."""
    is_healthy = await check_database_connection()
    connection_info = await get_connection_info()
    
    return {
        "status": "healthy" if is_healthy else "unhealthy",
        "database": connection_info,
        "timestamp": datetime.utcnow()
    }


@router.get("/health/performance")
async def performance_health_check():
    """Performance monitoring endpoint."""
    performance_summary = await get_performance_summary()
    
    return {
        "status": "healthy",
        "performance": performance_summary,
        "timestamp": datetime.utcnow()
    } 