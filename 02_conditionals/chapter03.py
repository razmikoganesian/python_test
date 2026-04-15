device_status = input("Enter device status. active/passive.  ").lower()
temp = int(input("Input temperature. "))

if device_status == "active":
    if temp > 50:
        print("High temperature alert!")
    else:
        print("Temperature is normal :)")
else:
    print("Device is offline") 