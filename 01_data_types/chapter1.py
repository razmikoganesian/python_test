# IMMUTABLE -  REFERENCE ID WILL BE CHANGE

sugar_amount = 2
print(f"Initial sugar amount is {sugar_amount}")

sugar_amount = 12
print(f"Secondly sugar amount is {sugar_amount}")

print(f" ID of 2: {id(2)}")
print(f" ID of 2: {id(12)}")


# IMMUTABLE - REFERENCE ID WILL BE THE SAME
spice_mix = set()
print(f'Initial spice mix ID is {id(spice_mix)}')
spice_mix.add("Ginger")
spice_mix.add("Kakao")
print(f'After spice mix ID is {id(spice_mix)}')
print(spice_mix)
