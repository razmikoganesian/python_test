# NON LOCAL
def update_order():
    tea_type = "Ulun"
    def kitchen():
        nonlocal tea_type
        tea_type = "Green"
    kitchen()
    print(f"After kitche update value if tea is {tea_type}")

# update_order()

# global scope
tea_type = "Black"

def front_desk():
    def kitchen():
        global tea_type
        tea_type = "Black with milk"
    kitchen()
    print(f"Global scope var was changed to {tea_type}")

front_desk()