class NameSpace:
    origin = 'China'


print(NameSpace.origin)

NameSpace.is_hot = True

print(NameSpace.is_hot)

# creating objects from clas NameSpace

test = NameSpace()
print(f"Country is {test.origin}", f"Is tea is hot - {test.is_hot}")
print('-----------')
test.is_hot = False
print("Class: ", NameSpace.is_hot)
print(f"Is tea is hot - {test.is_hot}")
test.flavour = "Ginger"
print(test.flavour)