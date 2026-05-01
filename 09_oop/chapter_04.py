# INIT
class TeaOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}-ml of {self.type} tea"

a = TeaOrder(type_="Green tea", size=120)

print(a.summary())

b = TeaOrder(type_="Masala tea", size=150)
print(b.summary())

