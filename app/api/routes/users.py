from fastapi import APIRouter, Depends
from app.deps.auth import get_user

router = APIRouter(prefix="/users")

@router.get("/me")
def get_me(user=Depends(get_user)):
    return {
        "user_id": user.get("sub"),
        "email": user.get("email"),
    }