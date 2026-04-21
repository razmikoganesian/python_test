def get_input():
    print("Getting user input")

def validate_input():
    print("Validating user info")

def save_to_db():
    print("saveing to DB")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registartion completed")

# radbility

def calculate_bills(tea_cups_amount, cup_price):
    return cup_price * tea_cups_amount

first_bill = calculate_bills(4,2)
# print(f"Order for table 2  -  {calculate_bills(4,7)}")

# traceability
def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100


orders = [100,150, 200, 300]

for price in orders:
    final_amount = add_vat(price=price, vat_rate=10)
    print(f"Original value is {price}, and final amount is {final_amount}")

