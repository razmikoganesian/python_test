# LIST COMPREHENSION

menu = [
    "Green tea",
    "Black tea",
    "Lemon tea",
    "Masala tea",
    "Ice tea"
]

iced_tea = [tea for tea in menu if "Ice" in tea]
iced_tea1 = [tea for tea in menu if len(tea) > 9]
print(iced_tea)
print(iced_tea1)