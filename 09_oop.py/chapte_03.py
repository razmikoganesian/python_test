# SELF ARGS
from pydoc import describe


class Tea:
    size = 150 


    def describe(self):
        return f"A {self.size}-ml is a size of tea cup"
    
a = Tea()
print(a.describe())

b = Tea()
b.size = 200
print(b.describe())