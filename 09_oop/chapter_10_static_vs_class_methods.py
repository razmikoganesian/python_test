class TeaOrder:
    def __init__(self, tea_type, sugar_level, size_of_cup) -> None:
        self.tea_type = tea_type
        self.sugar_level = sugar_level
        self.size_of_cup = size_of_cup

    @classmethod
    def from_dictionary(cls, order_data):
        return cls(
            order_data['tea_type'],
            order_data['sugar_level'],
            order_data['size_of_cup'],
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sugar_level, size_of_cup = order_string.split('/')
        return cls(tea_type, sugar_level, size_of_cup)
    

class TeaUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]
    
print(TeaUtils.is_valid_size("Medium"))
    

order1 = TeaOrder.from_dictionary({"tea_type": "Lemon tea",
                                   "sugar_level" : "0 sugar",
                                    "size_of_cup": "Medium"
                                   })

order2 = TeaOrder.from_string("Masala tea / 2 sugar / Large")

print(order1.__dict__)
print('---------')
print(order2.__dict__)

order3 = TeaOrder("Ice tea", "3 sugar", "Small")
print(order3.__dict__)

