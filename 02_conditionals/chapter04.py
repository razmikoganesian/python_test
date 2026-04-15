input_order_amount = int(input("pleas enter order amount -    "))

delivery_fees = 0 if input_order_amount > 300 else 30
  
print(delivery_fees)