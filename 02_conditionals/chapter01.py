kettle_boiled = False
if kettle_boiled:
    print(f"Kettle Done! Time to make some tea")
else:
    print(f"Water is not boiled!")

snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "chipsi":
    print(f"Order confirmed with {snack}")
else:
    print("No way man")

