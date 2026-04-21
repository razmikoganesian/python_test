# FUNCTION SCOPE
def serve_tea():
    tea_type = "Masala tea" # local scope
    print(f"Inside function {tea_type}")


tea_type = "Lemon"
serve_tea()


def tea_counter():
    tea_order = "lemon" # Enclosing scope
    def print_order():
        tea_order = "Ginger"
        print(f"Inner {tea_order}")
    print_order()
    print(f"Outer {tea_order}")

tea_order = "Green tea"
tea_counter()
print("Global: scope ", tea_order)

