# RETURN
from math import remainder
import re


def  make_tea():
    return "here is your tea!"

return_value = make_tea()

# print(return_value)

def ideal_tea():
    pass

def sold_cups():
    return 125

total_cups = sold_cups()


def tea_status(cups_left_in_stock):
    if cups_left_in_stock == 0:
        return "Sorry man, no coffee any more"
    else:
        return "Tea is ready for you!"
    print('Tea status is more then you think') # unreacheable part of code
    
# print(tea_status(0))
# print(tea_status(5))

def tea_report():
    return 100, 200, "Yes", 

sold, remain_item, not_paid  = tea_report()
print(sold)
print(f"remaining items: {remain_item}")

