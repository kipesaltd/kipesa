import time
import asyncio
from typing import Dict, Any, Optional
from loguru import logger
from functools import wraps
from contextlib import asynccontextmanager

class PerformanceMonitor:
    """Performance monitoring for the application."""
    
    def __init__(self):
        self.metrics = {}
        self.request_times = []
    
    def track_request(self, endpoint: str, method: str, duration: float):
        """Track request performance."""
        key = f"{method}:{endpoint}"
        if key not in self.metrics:
            self.metrics[key] = {
                'count': 0,
                'total_time': 0,
                'avg_time': 0,
                'min_time': float('inf'),
                'max_time': 0
            }
        
        metric = self.metrics[key]
        metric['count'] += 1
        metric['total_time'] += duration
        metric['avg_time'] = metric['total_time'] / metric['count']
        metric['min_time'] = min(metric['min_time'], duration)
        metric['max_time'] = max(metric['max_time'], duration)
        
        # Log slow requests
        if duration > 5.0:  # 5 seconds threshold
            logger.warning(f"Slow request: {key} took {duration:.2f}s")
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics."""
        return self.metrics
    
    def reset_metrics(self):
        """Reset performance metrics."""
        self.metrics = {}

# Global performance monitor
performance_monitor = PerformanceMonitor()

def track_performance(endpoint: str, method: str = "GET"):
    """Decorator to track function performance."""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = await func(*args, **kwargs)
                duration = time.time() - start_time
                performance_monitor.track_request(endpoint, method, duration)
                return result
            except Exception as e:
                duration = time.time() - start_time
                performance_monitor.track_request(endpoint, method, duration)
                raise
        return wrapper
    return decorator

@asynccontextmanager
async def track_operation(operation_name: str):
    """Context manager to track operation performance."""
    start_time = time.time()
    try:
        yield
    finally:
        duration = time.time() - start_time
        logger.info(f"Operation '{operation_name}' took {duration:.3f}s")

class DatabaseQueryTracker:
    """Track database query performance."""
    
    def __init__(self):
        self.query_times = []
        self.slow_query_threshold = 1.0  # 1 second
    
    def track_query(self, query: str, duration: float):
        """Track database query performance."""
        self.query_times.append({
            'query': query,
            'duration': duration,
            'timestamp': time.time()
        })
        
        if duration > self.slow_query_threshold:
            logger.warning(f"Slow database query ({duration:.3f}s): {query[:100]}...")
    
    def get_slow_queries(self, threshold: float = None) -> list:
        """Get slow queries."""
        threshold = threshold or self.slow_query_threshold
        return [q for q in self.query_times if q['duration'] > threshold]

# Global database query tracker
db_tracker = DatabaseQueryTracker()

def track_db_query(query: str):
    """Decorator to track database query performance."""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = await func(*args, **kwargs)
                duration = time.time() - start_time
                db_tracker.track_query(query, duration)
                return result
            except Exception as e:
                duration = time.time() - start_time
                db_tracker.track_query(query, duration)
                raise
        return wrapper
    return decorator

async def get_performance_summary() -> Dict[str, Any]:
    """Get comprehensive performance summary."""
    return {
        'request_metrics': performance_monitor.get_metrics(),
        'slow_queries': db_tracker.get_slow_queries(),
        'total_requests': sum(m['count'] for m in performance_monitor.metrics.values()),
        'average_response_time': sum(m['avg_time'] * m['count'] for m in performance_monitor.metrics.values()) / max(sum(m['count'] for m in performance_monitor.metrics.values()), 1) if performance_monitor.metrics else 0
    } 