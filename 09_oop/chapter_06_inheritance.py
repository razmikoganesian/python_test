# Inheritance
class BaseTea:
    def __init__(self, type_) -> None:
        self.type = type_


    def prepare(self):
        print(f"Preparing {self.type} some tea")


class MasalaTea(BaseTea):
    def add_spices(self):
        print('Add cardamon, ginger, cloves')
    

# Composition
class TeaShop:
    tea_cls = BaseTea # reference to BaseTea

    def __init__(self) -> None:
        self.tea = self.tea_cls("Regular")

    def serve(self):
        print(f"Serving {self.tea.type} tea in a shop")
        self.tea.prepare()

class FancyTeaShop(TeaShop):
    tea_cls = MasalaTea

    def __init__(self) -> None:
        super().__init__()

shop = TeaShop()
fancy = FancyTeaShop()
shop.serve()
fancy.serve()
fancy.tea.add_spices()
