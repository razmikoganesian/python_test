


# for i in range(1,11):
#     print(f"Serving tea to client #{i}")


# for i in range(1,5):
#     print(f"Preparing tea for batch#{i}")

def multiplication_table(number: int) -> list[str]:
    a = []
    for i in range(1,11):
        a.append(f"{number} * {i} = {number*i}")
    return a

# print(multiplication_table(4))

a = ["James", "Mike", "Peter", "Shone", "Bob", "SuperMan"]

for i in a: 
    print(f"Name is {i}")