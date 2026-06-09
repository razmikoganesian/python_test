from multiprocessing import Process
import time


def cpu_heavy():
    print(f"Crunching some numbers....")
    total = 0
    for i in range(10**8):
        total += i
    print("Done ✅")


if __name__ == "__main__":
    start = time.time()

    process = [Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in process]
    [t.join() for t in process]

    finish = time.time()

    print(f"Time taken is {finish -start:.2f} seconds")
