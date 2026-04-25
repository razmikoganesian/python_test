# SET COMPREHENSION
favourite_teas = [
    "Masala tea",
    "Green tea",
    "Black tea",
    "Milk tea",
    "Lemon tea",
    "Crazy ice tea",
    "Berhamot tea",
    "Masala tea",
    "Green tea",
]

unique_tea = {tea for tea in favourite_teas}
unique_tea1 = {tea for tea in favourite_teas if len(tea) < 6 }

# print(unique_tea)


recipes = {
    "Masala tea": ['Ginger', 'Cardamon', 'Clove'],
    "Elaichi tea": ['Lemon', 'Cardamon', 'Milk'],
    "Spicy tea": ['Lemon', 'Black paper', 'Clove'],
    "Spicy tea": ["Ratatui"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
unique_keys = {key for key in recipes.keys() }
print(unique_spices)
print(unique_keys)