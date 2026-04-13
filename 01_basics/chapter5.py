# TUPLES (). IMMUTABLE
masala_spices = ("cardamon", "lemon", "cinamon")

(spice1, spice2, spice3) = masala_spices
print(f"Spices one is {spice1}")

cardamon_ratio, lemon_ratio = 2,3
print(f"Ratio of lemon is {lemon_ratio} and cardamon ratio is {cardamon_ratio}")
cardamon_ratio, lemon_ratio = lemon_ratio,cardamon_ratio # SWAP VARIABLES
print(f"Ratio of lemon is {lemon_ratio} and cardamon ratio is {cardamon_ratio}")

# membership testing

print(f"Is ginger in masala spices? {'ginger' in masala_spices}")
print(f"Is ginger in masala spices? {'cinamon' in masala_spices}")