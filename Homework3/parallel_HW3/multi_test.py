import time
from multiprocessing import Pool


def mult(x, y):
    square = x * y
    print("start process")
    time.sleep(1)
    return square

def loop_through():
    pool = Pool()
    result = pool.starmap_async(mult, zip(range(0, 5), range(1, 6)))
    print("main script")
    print(result.get())
    print("end main script")


if __name__ == "__main__":
    loop_through()

    loop_through()
