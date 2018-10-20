from contextlib import contextmanager
import time


@contextmanager
def timer():
    stats=dict()
    start=time.perf_counter()
    stats["started"]=start
    try:
        yield stats
    finally:
        end=time.perf_counter()
        stats["ended"]=end

with timer() as stats:
    time.sleep(5)
print(stats)
