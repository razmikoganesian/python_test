# DICTIONARY
tea_order = dict(type="Masala Tea", size="large", sugar =1)
print(f"Tea order : {tea_order}")

tea_recipe = {

}
# add data to DICT
tea_recipe["base"] = "black tea"
tea_recipe["liquid"] = "milk"

print(tea_recipe["liquid"])
# delete data from DICT

del tea_recipe['liquid']
print(tea_recipe)

print(f"Is sugar in tea order - {'suger' in tea_order}")
# ONLY KEYS OR VALUES OR ITEMS
tea_order1 = dict(type="Green Tea", size="medium", sugar =2)
print(f"Order details keys: {tea_order1.keys()}")
print(f"Order details keys: {tea_order1.values()}")
print(f"Order details keys: {tea_order1.items()}")
print('------------------')
# delete last item and save in variable
last_item = tea_order1.popitem()
print(last_item)
print(tea_order1)

# add data
extra_spices = {"lemon": "sliced", "cinamon": "powder"}
tea_order1.update(extra_spices)
print(tea_order1)


tea_size = tea_order1['size']
print(tea_size)

# GET
tea_test_get = tea_order1.get('notes', 'No such thing')
print(tea_test_get)