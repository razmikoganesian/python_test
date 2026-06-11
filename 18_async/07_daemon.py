import threading
import time


def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temparature...")
        time.sleep(3)


t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main programm done!")
