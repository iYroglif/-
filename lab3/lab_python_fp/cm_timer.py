from time import time
from time import sleep
from contextlib import contextmanager

class cm_timer_1:

    def __enter__(self):
        self.t = time()

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print(time() - self.t)

@contextmanager
def cm_timer_2():
    t = time()
    yield
    print(time() - t)

if __name__ == '__main__':
    with cm_timer_1():
        sleep(5.5)

    with cm_timer_2():
        sleep(5.5)