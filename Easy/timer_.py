from contextlib import contextmanager
import time


@contextmanager
def timer():
    start = time.monotonic()
    yield
    print(f"execution time is {(time.monotonic() - start)} seconds")


if __name__ == '__main__':
    with timer():
        time.sleep(1)
