from pydantic import BaseModel


class UserSignupDto(BaseModel):
    firstName: str
    lastName: str
    email: str
