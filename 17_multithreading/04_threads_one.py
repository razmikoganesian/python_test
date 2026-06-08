import threading
import time


def boiling_milk():
    print(f"Boiling milk...")
    time.sleep(2)
    print(f"Milk boiled!")


def toast_bun():
    print(f"Toasting bun...")
    time.sleep(2)
    print(f"Bun Toasted!")


start = time.time()

t1 = threading.Thread(target=boiling_milk())
t2 = threading.Thread(target=toast_bun())

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Breakfast Finished in {end - start:.2f} seconds")
