import threading
import time


def prepare_tea(type_, wait_time):
    print(f"{type_} Tea brewing...")
    time.sleep(2)
    print(f"{type_} Tea is ready!")


start = time.time()

t1 = threading.Thread(target=prepare_tea, args=("Masala", 2))
t2 = threading.Thread(target=prepare_tea, args=("Ginger", 5))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Tea Brewing Finished in {end - start:.2f} seconds")
