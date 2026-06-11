from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product_one = Product(id=1, name="Laptop", price=400.55, in_stock=True)
product_two = Product(id=2, name="Keyboard", price=11.99)
product_three = Product(name="Keyboard")
