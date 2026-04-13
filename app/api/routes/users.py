from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/users")

@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return {
        "user_id": user.get("sub"),
        "email": user.get("email"),
    }