# MUTABLE  - LIST
ingredients = ["water", "milk", "black tea leafs"]

ingredients.append('lemon')
print(f"New ingredients are {ingredients}")
ingredients.remove("water")
print(f"New ingredients are {ingredients}")

spice_options = ["ginger", "cardamon"]
tea_ingredients = ["water", "milk"]

tea_ingredients.extend(spice_options) # combine 2 list together
print((tea_ingredients))
print(tea_ingredients[1])

tea_ingredients.insert(1,"magic powder")
print(tea_ingredients)

last_added = tea_ingredients.pop() # delete last item from list and create a variable
print(last_added)
print(tea_ingredients)

# reverse data in list
tea_ingredients.reverse()
print(tea_ingredients)

# sorting
tea_ingredients.sort()
print(tea_ingredients)

# MAX from list
suger_levels = [1,2,3,4,5]
print(f"Maximum sugar level is {max(suger_levels)}")
print(f"Minimum sugar level is {min(suger_levels)}")


# operators  with list

base_liquid = ["water", "milk"]
extra_flavour = ['ginger']

full_liquid_mix = base_liquid + extra_flavour
print(full_liquid_mix)


strong_brew = ["black tea"] * 3
print(strong_brew)

# convert string to a list

a = "CINNAMON"
raw_space_data = bytearray(b"CINNAMON")
print(raw_space_data)