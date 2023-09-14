from datetime import timedelta, datetime
from typing_extensions import deprecated
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic_core import to_json
import dotenv
import os

dotenv.load_dotenv()
from core.dto.user import UserTokenData

SECRET_KEY = str(os.getenv("JWT_SECRET_KEY"))
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_pwd, hashed_pwd):
    tmp = pwd_context.verify(plain_pwd, hashed_pwd)
    return tmp


def get_password_hash(pwd):
    return pwd_context.hash(pwd)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
