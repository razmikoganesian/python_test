from packaging import tags
from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Union
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")}
    )


user = User(
    id=1,
    name="Test Name",
    email="test@,ail.com",
    is_active=True,
    created_at=datetime(2024, 3, 15, 14, 30, 14),
    address=Address(street="Lenin street", city="Ulianovsk", zip_code="433320"),
    tags=["test_tag", "new_user"],
)

python_dict = user.model_dump()
print(python_dict)

print("*" * 40)
json_str = user.model_dump_json()
print(json_str)
