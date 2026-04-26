# BASIC
def serve_tea():
    yield "Cup 1: Masala tea"
    yield "Cup 2: Green tea"
    yield "Cup 3: Black tea"
    yield "Cup 4: MasaLemonla tea"
    yield "Cup 5: Ginger tea"


stall = serve_tea()

for cap in stall:
    print(cap)
print('---------')
def get_list_of_tea():
    return ['cup1', 'cup2', 'cup3']

# generator function

def generator_of_tea():
    yield "Cup1"
    yield "Cup2"
    yield "Cup3"

tea = generator_of_tea()
# to print value from generator use NEXT
print(next(tea))
print(next(tea))
print('---------')
print(next(tea))
# print(next(tea)) # return STOP ITERATION