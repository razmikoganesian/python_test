# our own exceptions
def brew_tea(flavor):
    if flavor not in ["masala", "ginger", "lemon"]:
        raise ValueError("Unsupported tea flavor ...")
    print(f"brewing {flavor} tea...")

# brew_tea("mint")


# custom exceptions
class OutOfingredientsError(Exception):
    pass

def make_tea(milk, suger):
    if milk == 0 and suger == 0:
        raise OutOfingredientsError("Missing milk and suger")
    print("Tea is ready")

make_tea(0,0)
