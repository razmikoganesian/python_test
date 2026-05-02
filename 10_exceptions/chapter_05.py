class InvaliTeaError(Exception): pass

def bill(flavor, cups):
    menu = {"masala" : 3,
            "lemon": 4,
            "ice_tea": 5}
    try:
        if flavor not in menu:
            raise InvaliTeaError(f"That tea {flavor} is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an interger")
        total = menu[flavor] * cups
        print(f"Total price is {total}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print('It is Done!')

bill("aaa", 'twelve')