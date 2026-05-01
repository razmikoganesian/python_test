class BaseClass:
    def __init__(self, age) -> None:
        self._age = age


    @property
    def age(self):
        return self._age * 2
    

    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Age must be between 1 to 5")
        
aaa = BaseClass(2)
print(aaa.age)

aaa.age = 5
print(aaa.age)