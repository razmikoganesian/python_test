
def token_dispenser(start: int = 1):
    try:
        while True:
            print(f"Start value is {start}")
            new_value = yield start
            if new_value is not None:
                start = new_value
            else:
                start += 1
    except GeneratorExit:
        print("Dispenser closed")
        raise

        
        



reset_token = token_dispenser()
next(reset_token)

# for i in range(4):
#     next(reset_token)

print(reset_token.send(3))
print(next(reset_token))


reset_token.close() # cleanup