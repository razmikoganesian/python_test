import subprocess
import os
import time

import psutil


def clear_screen():
    subprocess.run(["cls" if os.name == "nt" else "clear"], shell=True)


def show_stats():
    print("*" * 30)
    print("⭐️ System resource monitor")

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    print(f"CPU usage {cpu} %")
    print(
        f"RAM memory usage is {ram.percent}% ({round(ram.used / 1e9)} GB used of {round(ram.total / 1e9)} GB )"
    )
    print(
        f"DISK usage is {disk.percent}% ({round(disk.used / 1e9)} GB used of {round(disk.total / 1e9)} GB ) "
    )
    print("#" * 30)


if __name__ == "__main__":
    try:
        while True:
            clear_screen()
            show_stats()
            time.sleep(3)
    except KeyboardInterrupt:
        print("Monitoring Finito!!!")
