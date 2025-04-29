from datetime import datetime

def user_dict(user: dict):
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "created_at": user["created_at"]
    }
