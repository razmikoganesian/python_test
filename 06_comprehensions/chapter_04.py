# GENERATOR
daily_sales = [5,56,34,33,1,2,77,800,5]

total = sum(i for i in daily_sales if i > 5)
print(total)
total1 = sum([x for x in daily_sales if x > 5])
print(total1)