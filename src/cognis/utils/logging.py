import time
import functools
import logging

logger = logging.getLogger("cognis.trace")

def trace_execution(func):
    """
    FAANG Level Decorator: Tracks latency and status of AI operations.
    Useful for system optimization and observability.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        logger.info(f"Start: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start_time
            logger.info(f"Success: {func.__name__} in {duration:.4f}s")
            return result
        except Exception as e:
            logger.error(f"Failed: {func.__name__} | Error: {str(e)}")
            raise
    return wrapper
