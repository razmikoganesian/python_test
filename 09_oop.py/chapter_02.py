# attribute shadowing
class Tea:
    temperature = 'Hot'
    strength = 'strong'


cutting_tea = Tea()
print(cutting_tea.temperature)

cutting_tea.temperature = 'Mild'
cutting_tea.cup = 'Medium'
print(f"After changing var it become: {cutting_tea.temperature}")
print(f"Direct address to Tea class display: {Tea.temperature}")
print(f'Cup size is: {cutting_tea.cup}')

# delete operation
del cutting_tea.temperature
del cutting_tea.cup
print(f"After  deleting it become: {cutting_tea.temperature}")
print(f'Cup after deletion is: {cutting_tea.cup}') # will display an error, 'Tea' object has no attribute 'cup'

