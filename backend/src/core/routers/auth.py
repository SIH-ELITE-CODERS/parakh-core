from fastapi import APIRouter
from dependencies.db import scope
from dto.user import UserSignupDto as User

router = APIRouter(
    prefix="/api/user",
)


@router.get("/")
async def get_users():
    collection = scope.collection("users")
    # get all users
    result = scope.query(f"SELECT * FROM users").execute()
    return result[0]


@router.post(
    "/create/",
    tags=["users"],
    status_code=201,
    summary="Create a new user",
    description="Create a new user",
    response_description="User created successfully",
)
async def create_user(user: User):
    new_user = {
        "firstName": user.firstName,
        "lastName": user.lastName,
        "email": user.email,
    }
    collection = scope.collection("users")
    collection.upsert("3", new_user)
    result = collection.get("3")
    return result.value


# @router.get("/users",tags=["users"])
