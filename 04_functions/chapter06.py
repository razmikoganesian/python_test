# PARAMETERS
tea = "Ginger tea"

def prepare_tea(tea_name):
    print(f"Preparing Ginget tea {tea_name}")

prepare_tea(tea)


tea1 = [1,2,3]

def edit_tea(cup):
    cup[1] = 'Wrong tea'

edit_tea(tea1)
print(tea1)

# ARGS / *KWARGS
def make_tea(tea, milk, ginger):
    print(tea, milk, ginger)

make_tea("SUpER", "TEA", 'SHOULD BE DONE')
make_tea(tea="Green", milk="3.2%", ginger="YES")
print("--------")


def special_tea(*ingredients, **extras):
    print(f"Ingredients {ingredients} and some extras {extras}")

special_tea("Cinamon", "Cardamon", sweetstaff = "Honey", foam = 'yes')
print("--------")

def tea_order(order=[]):
    order.append("Masala")
    print(order)

tea_order()

def tea_order1(order=None):
    if order is None:
        order = []
    print(order)

tea_order1()
tea_order1()
