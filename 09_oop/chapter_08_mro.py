class A:
    label = 'A: Base class'

class B(A):
    label = 'B: B class'

class C(A):
    label = 'C: C class'

class D(B,C):
    pass

test1 = D()
print(test1.label)
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# procedure of classes
