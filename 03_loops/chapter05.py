# WALRUS OPERATOR

from operator import indexOf


value = 13

reminder = value % 4

if reminder:
    print(f"Number is not fully divisible, the reminder is {reminder}")
print("---------")

value = 15
if (reminder := value % 4):
    print(f"Number is not fully divisible, the reminder is {reminder}")

# available_size = ['small', "medium", "large", "xxxl"]
# if (requested_size := input("Enter your favouritesize:  ").lower()) in available_size:
#     print(f"Requested size is {requested_size}")
# else:
#     print(f"No such size")
# print("---------")

flavours = ['masala', 'lemon', "ginger", "mint"]

print("Available flavours: ", flavours)

while (flavor := input("Choose your flavor:  ")) not in flavours:
    print(f"Sorry , {flavor} is not available")
print(f"You choose {flavor} ")