flavours = ["Ginger", "Lemon", "Out of Stock",  "Discontinued"]

for i in flavours:
    if i == "Discontinued":
        continue
    if i == "Out of Stock":
        break
    print(f"{i} item found")
print("Outside of loop")
print("---------------")

# FOR ELSE
staff = [("Alex", 16), ("Mike", 34), ("Nick", 50) ]


for name, age in staff:
    if age > 18:
        print(f"{name} is available as a manager")
        break
else:
    print("No adult persons")