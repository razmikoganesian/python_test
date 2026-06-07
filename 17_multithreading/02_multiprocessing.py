from multiprocessing import Process
import time


def brew_tea(name):
    print(f"Start of tea {name} tea brewing")
    time.sleep(3)
    print(f"End of tea {name} tea brewing")


if __name__ == "__main__":
    tea_makers = [
        Process(target=brew_tea, args=(f"Tea Maker #{i+1}",)) for i in range(3)
    ]

    # Start all process
    for p in tea_makers:
        p.start()
    # Wait for all to complete
    for p in tea_makers:
        p.join()


print("All tea served!")
