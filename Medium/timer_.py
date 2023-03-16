from contextlib import contextmanager
import time


@contextmanager
def timer():
    start = time.time()
    yield
    print(f"execution time is {(time.time() - start)} seconds *")


with timer():
    time.sleep(1)
