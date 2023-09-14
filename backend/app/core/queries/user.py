from core.dependencies.db import scope
from couchbase.options import QueryOptions


def get_user_by_email(email: str):
    result = scope.query(
        "SELECT * FROM users WHERE email=$1",
        QueryOptions(positional_parameters=[email]),
    )
    result = result.execute()
    if len(result) == 0:
        return None
    return result[0]


def get_user_by_email(email: str):
    result = scope.query(
        "SELECT Meta().id as document_id, * FROM users WHERE email=$1",
        QueryOptions(positional_parameters=[email]),
    )
    result = result.execute()
    if len(result) == 0:
        return None
    else:
        exist_user = result[0]["users"]
        exist_user.update({"document_id": result[0]["document_id"]})
        return exist_user
