import sys
from fractions import Fraction
from decimal import Decimal as 

# BOOLEAN
is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(total_actions) # result is 6

milk_is_presnt = 0 # no milk
print(f"is there a milk? {bool(milk_is_presnt)}") # result false

# LOGICAL OPERATORS

water_hot  = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can serve a tea? {can_serve}")


# Difficult numbers
ideal_temp = 95.5
current_temp = 95.32

print(f"Ideal temperature is {ideal_temp}")
print(f"Current temperature is {current_temp}")
print(f"Difference between temperatures is {ideal_temp - current_temp}")
print(sys.float_info)