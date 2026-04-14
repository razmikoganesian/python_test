# SET
essential_spices = {"lemon", "ginger", "milk"}
optional_spices = {"cardamon", "ginger" ,"black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}") # ginger display just once

common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}") # ONLY ginger display

only_in_essential = essential_spices - optional_spices
print(f"Only in essential spicewa {only_in_essential}")

print(f"Is clobess in essential spices? {'cloves' in essential_spices}") # return false

