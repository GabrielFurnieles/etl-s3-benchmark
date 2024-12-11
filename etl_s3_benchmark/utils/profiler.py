import time
import psutil
import functools
import tracemalloc
from typing import Callable, TypeVar, Any

T = TypeVar("T")


def profile_function(func: Callable[..., T]) -> Callable[..., tuple[T, dict]]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> tuple[T, dict]:
        # Start memory tracking
        tracemalloc.start()
        process = psutil.Process()
        start_memory = process.memory_info().rss / 1024 / 1024  # Convert to MB

        # Start timing
        start_time = time.time()

        try:
            # Execute the function
            result = func(*args, **kwargs)

            # Get memory peak
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            # Get execution time
            execution_time = time.time() - start_time

            # Get final memory usage
            end_memory = process.memory_info().rss / 1024 / 1024
            memory_difference = end_memory - start_memory

            # Prepare profiling results
            profiling_data = {
                "execution_time_seconds": round(execution_time, 3),
                "memory_usage_mb": {
                    "start": round(start_memory, 2),
                    "end": round(end_memory, 2),
                    "difference": round(memory_difference, 2),
                    "peak": round(peak / 1024 / 1024, 2),  # Convert to MB
                },
            }

            return result, profiling_data

        finally:
            # Ensure tracemalloc is stopped even if an exception occurs
            if tracemalloc.is_tracing():
                tracemalloc.stop()

    return wrapper
