from fastapi import APIRouter, HTTPException
from core.exceptions.user import (
    DuplicateUserException,
    UserNotFoundException,
    InvalidUserCredentialsException,
)
from core.dependencies.db import scope
from core.dto.user import UserSignupDto, UserLoginDto
import uuid
from core.queries.user import get_user_by_email
from core.utils.auth import create_access_token, get_password_hash, verify_password

router = APIRouter(
    prefix="/api/user",
)


@router.post(
    "/register",
    tags=["user"],
    status_code=201,
    summary="Create a new user",
    description="Create a new user",
    response_description="User created successfully",
)
async def signup(user_cred: UserSignupDto):
    # check if the user with given credentials exist if exists return 409
    try:
        user = get_user_by_email(user_cred.email)
        if user is not None:
            raise DuplicateUserException()
        # if the user does not exist then hash the password
        document_id = str(uuid.uuid4())
        collection = scope.collection("users")
        hashed_pwd = get_password_hash(user_cred.password)
        new_user = {
            "name": user_cred.name,
            "email": user_cred.email,
            "password": hashed_pwd,
            "branch": user_cred.branch,
            "phone": {
                "country_code": user_cred.phone.country_code,
                "mobile_number": user_cred.phone.mobile_number,
            },
            "age": user_cred.age,
            "year_of_enrollment": user_cred.year_of_enrollment.isoformat(),
            "year_of_grad": user_cred.year_of_graduation.isoformat(),
            "role": "student",
        }
        # store in the database
        collection.insert(document_id, new_user)
        token_data = {
            "uuid": document_id,
            "name": user_cred.name,
            "email": user_cred.email,
        }
        # generate jwt for the user
        token = create_access_token(token_data)
        # return jwt with user id and email
        return {
            "access_token": token,
            "uuid": document_id,
            "name": user_cred.name,
            "email": user_cred.email,
        }
    except Exception as excp:
        status_code = 500  # Default status code for unhandled exceptions
        detail = "Internal Server Error"
        if isinstance(excp, DuplicateUserException):
            status_code = 409
            detail = "User with given credentials already exists"
        # If no exception is cached throw internal error
        raise HTTPException(
            status_code=status_code,
            detail=detail,
        )


@router.post(
    "/login",
    tags=["user"],
    status_code=200,
    summary="Endpoint to for user login",
    description="Login using email and password",
    response_description="User Logged In successfully",
)
async def login(user_cred: UserLoginDto):
    try:
        # check if the user exists in the database if not return 404
        user = get_user_by_email(user_cred.email)
        if user is None:
            raise UserNotFoundException()
        # if the user exist check for password matche
        if not verify_password(
            user_cred.password, str(user["password"])
        ):  # if the password matches
            raise InvalidUserCredentialsException()
        token_data = {
            "uuid": user["document_id"],
            "name": user["name"],
            "email": user["email"],
        }
        access_token = create_access_token(token_data)  # generate jwt
        return {
            "access_token": access_token,
            "uuid": user["document_id"],
            "name": user["name"],
            "email": user["email"],
        }  # return jwt user email and uuid
    except Exception as excp:

        status_code = 500  # Default status code for unhandled exceptions
        detail = "Internal Server Error "
        print(excp)
        if isinstance(excp, UserNotFoundException):  # if user not found
            status_code = 404
            detail = "User with given credentials does not exist"
        if isinstance(excp, InvalidUserCredentialsException):
            status_code = 401
            detail = "User with given credentials are incorrect"
        # If no exception is cached throw internal error
        raise HTTPException(
            status_code=status_code,
            detail=detail,
        )


# @router.post(
#     "/create/",
#     tags=["users"],
#     status_code=201,
#     summary="Create a new user",
#     description="Create a new user",
#     response_description="User created successfully",
# )
# async def create_user(user: User):
#     new_user = {
#         "firstName": user.firstName,
#         "lastName": user.lastName,
#         "email": user.email,
#     }
#     collection = scope.collection("users")
#     collection.upsert("3", new_user)
#     result = collection.get("3")
#     return result.value
