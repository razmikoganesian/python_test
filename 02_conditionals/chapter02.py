size = input('Enter size of cup: large/medium/small:  ').lower()

if size == "medium":
    print(f"Price for medium is 15$")
elif size == "large":
    print(f"Price for large is 20$")
elif size == "small":
    print(f"Price for large is 10$")
else:
    print("Size is not readable")





def calculate_delivery_charge(distance: float) -> str:
    if distance <= 2:
        return "Delivery charge: 0"
    elif distance <=5:
        return "Delivery charge: 30"
    elif distance <= 10:
        return "Delivery charge: 50"
    else:
        return "Delivery not available for your location."
    
    pass
distance = float(input("Enter distance in numbers.  "))
print(calculate_delivery_charge(distance))
