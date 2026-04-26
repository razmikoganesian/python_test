#  INFINITE GENERATORS
def infinite_tea():
    count = 1
    while True:
        yield f"Refile #{count}"
        count += 1

refill = infinite_tea()
user1 = infinite_tea()

# for _ in range(3):
#     print(next(refill))

# for _ in range(6):
#     print(next(user1))

# --------------------------------------------
# send data to generator
def tea_customer():
    print("Welcome!  What tea would you prefer? ")
    order = yield # pause program and wait a value
    while True:
        print(f"Preparing: {order}")
        order = yield # pause program and wait a value

stall = tea_customer()
next(stall) # start the generator
stall.send("Green tea")
stall.send("Lemon tea")