# multiple exception

def process_order(tea_type, cup_number):
    try:
        price = {"masala" : 20}[tea_type] # forcing to get a key error
        cost = price  * cup_number
        print(f"Total is: {cost}")
    except KeyError:
        print(f"Sorry that {tea_type} is not exist")
    except TypeError:
        print("Quantity must ne in number")
    

process_order("lemon", 3)
process_order("masala", "two")