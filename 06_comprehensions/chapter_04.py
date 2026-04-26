# GENERATOR
daily_sales = [5,56,34,33,1,2,77,800,5]

total = sum(i for i in daily_sales if i > 5)
# print(total)
total1 = sum([x for x in daily_sales if x > 5])
# print(total1)


items = [
        {"name": "Notebook", "price": 250, "category": "Stationery"},
        {"name": "Pen", "price": 100, "category": "Stationery"},
        {"name": "Bag", "price": 1200, "category": "Accessories"},
        {"name": "Bottle", "price": 400, "category": "Utensils"},
    ]
    
name_of_product_less_500 = [item["name"] for item in items if item["price"] < 500 ]
unique_categories = {item["category"] for item in items}
product_to_price = {item["name"]:item["price"] for item in items }
discounted_prices = list(item["price"]* 0.9 for item in items)

a = (name_of_product_less_500, unique_categories,product_to_price, discounted_prices )
print(discounted_prices)