# NUMBERS
black_tea_grams = 12
ginger_grams = 4

total = black_tea_grams + ginger_grams
print(f"Total grams is:  {total}")

milk_litres = 3
servings = 6
milk_serving = milk_litres / servings
print(f"Milk per serving is {milk_serving}")

total_tea_bag = 7
pots = 2
bags_per_pot = total_tea_bag // pots # round number
print(f"Bags per pot is {bags_per_pot}")

total_cadamon_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamon_pods % pods_per_cup
print(f"leftover cadamon pods is {leftover_pods}")


base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor # 2 * 2 * 2
print(f"power flavour is {powerful_flavour}")


total_tea_leaves_harvested = 1_000_000_000 # for python is ok
print(f"tea leaves harvested are {total_tea_leaves_harvested}")