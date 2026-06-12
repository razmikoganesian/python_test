from pydantic import BaseModel, field_validator, model_validator
from typing import List, Optional


class Address(BaseModel):
    street: str
    city: str
    post_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


address = Address(street="some address", city="Mumbai", post_code="433320")
user = User(id=1, name="Test name", address=address)

user_data = {
    "id": 1,
    "name": "Test name",
    "address": {"street": "test street", "city": "Yerevan", "post_code": "Af34RT"},
}

user = User(**user_data)
print(user)
