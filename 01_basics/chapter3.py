# STRINGS
tea_type = "Ginger tea"
customer_name = "Alex"

print(f"Order for {customer_name} : {tea_type} please")

tea_description = "Aromatic and Bold"

print(f'First word is : {tea_description[0:8]}') # will print Aromatic 
print(f'First word is : {tea_description[::-1]}') # reverse string


label_text = 'Tea Spécial'
encoded_label = label_text.encode("utf-8")
print(encoded_label)

print(encoded_label.decode("utf-8"))