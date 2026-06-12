from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username: str

    @field_validator("username")
    def username_length(cls, value):
        if len(value) < 4:
            raise ValueError("Username must be at least 4 chars")
        return value


class SignUpData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords do not match")
        return values
