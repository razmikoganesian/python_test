# Types of functinos
def pure_tea(cups):
    return cups * 10

total_tea = 0

# STRONGLY NOT RECOMENDED
def impure_tea(cups):
    global total_tea
    total_tea +=cups

def pour_tea(n):
    if n == 0:
        return "All cups poured"
    return pour_tea(n-1)

print(pour_tea(4))

# LAMBDA
chai_type = ["Lemon tea", "Green tea", "Black tea", "Karkade", "Milk tea", "Green tea"]

strong_tea = list(filter(lambda chai: chai != "Green tea", chai_type))
print(strong_tea)

print('--------')
counter = 0
def impure_increment():
    global counter
    counter += 1
    return counter

print('--------')

def square_list(nums):
    new_list = list(map(lambda x:x ** 2,nums))
    return new_list

print(square_list([1,2,3,4]))