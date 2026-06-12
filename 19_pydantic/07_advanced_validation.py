from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime


class Person(BaseModel):
    first_name: str
    second_name: str

    @field_validator("first_name", "second_name")
    def names_must_be_capitalize(cls, value):
        if not value.istitle():
            raise ValueError("Names must be capitilized")
        return value


class User(BaseModel):
    email: str

    @field_validator("email")
    def normilize_email(cls, value):
        return value.lower().strip()


class Product(BaseModel):
    price: str

    @field_validator("price", mode="before")
    def parse_price(cls, value):
        if isinstance(value, str):
            return float(value.replace("$", "").replace(",", "."))
        return value


class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def validate_date_range(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError("end date must be after start_date")
        return values
