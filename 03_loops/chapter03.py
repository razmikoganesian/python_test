names = ["James", "Mike", "Peter", "Shone", "Bob", "SuperMan", "Sam"]
bills = [50, 70, 100, 120, 170,4,44,600]

# ZIP for 2 loops

for name, amount in zip(names, bills):
    print(f"{name} have a {amount} $$$")
print("-----------")
# WHILE LOOP

temp = 40

while temp <= 100:
    # temp = temp + 15
    temp += 14
    print(f"Temperature is {temp}")

print("Water is bolied!")
print("-----------")


def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    result = []
    i = 0
    while balance > 0:
        amount = withdrawals[i]
        if amount < balance:
            balance = balance - amount
            result.append(f"Withdrawn: {amount}")
        else:
            result.append(f"Insufficient funds for requested amount: {amount}")
        i = i + 1

    result.append(f"Remaining Balance: {balance}")
    return result
    



simulate_atm_withdrawals(100, [10,20,30,40,50])