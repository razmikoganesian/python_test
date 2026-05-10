import time

while True:
    try:
        seconds = int(input(("Please enter a time in seconds!")))
        if seconds < 1:
            print("Please enter a number greater then 0")
            continue
        break
    except ValueError:
        print('Invalid number, please enter a number')

    
print("\n Timer started..")
for remainig in range(seconds, 0, -1):
    minutes, seconds = divmod(remainig, 60)
    time_format = f"{minutes:02}:{seconds:02}"
    print(f"⏰ Time left: {time_format} ", end="\r")
    time.sleep(1)

print("\n Time's up! Take a break or move on")
