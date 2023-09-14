from pydantic import UUID4, BaseModel
from datetime import date


class UserTokenData(BaseModel):
    id: UUID4
    email: str


class contact_phone(BaseModel):
    country_code: str
    mobile_number: str


class UserSignupDto(BaseModel):
    name: str
    email: str
    password: str
    branch: str
    phone: contact_phone
    age: int
    year_of_enrollment: date
    year_of_graduation: date


class UserLoginDto(BaseModel):
    email: str
    password: str
