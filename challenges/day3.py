def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please netre a valid number!")

person_number = int(input("How many persons? :  ").strip())
names = []
for i in range(person_number):
    name = input(f"Please enter person name #{i+1}  ").strip()
    names.append(name)

total_bill = get_float("Enter a total bill number:  ")
share = round(total_bill / person_number)

print("*" * 40)
print(f"Total bill is {total_bill}")
print(f"there are {person_number} persons, each have to pay {share}")

for name in names:
    print(f"{name} owes {share} $$$")
print("*" * 40)