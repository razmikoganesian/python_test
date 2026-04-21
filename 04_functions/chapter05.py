loyalty_points = 0

def process_transactions(transactions: list[int]) -> int:
    sum = 0
    for i in transactions:
        sum  = sum + i

    def apply_bonus():
        nonlocal sum
        if sum > 1000:
            sum  = sum + 50
    apply_bonus()  

    global loyalty_points
    loyalty_points = loyalty_points +  sum // 100

    return sum


a = process_transactions([1000,100,1000])
print(a)

print(loyalty_points)