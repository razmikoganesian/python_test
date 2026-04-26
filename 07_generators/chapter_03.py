# FROM AND CLOSE YIELD THE GENERATORS
def local_tea():
    yield "Green tea"
    yield "Lemon tea"


def imported_tea():
    yield "Masala tea"
    yield "Oolong"

def full_menu():
    yield from local_tea()
    yield from imported_tea()

for tea in full_menu():
    print(tea)
print("----------")
def tea_table():
    try:
        order = yield # pause program and wait a value
        while True:
            print(f"Preparing: {order}")
            order = yield  "Waiting for tea order"
    except:
        print("Table is closed, no more tea")

table = tea_table()
next(table) # start generator
table.send("2 cups of green tea")
table.send("6 cups of black tea")
table.close() # cleanup

