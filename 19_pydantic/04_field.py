from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Emplyee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=25,
        description="Employee name",
        examples=["LTD Hachapuri"],
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000,
    )


class User(BaseModel):
    email: EmailStr
    phone: str = Field(..., pattern=r"^\+?\d{10,15}$")
