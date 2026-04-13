from fastapi import APIRouter, Depends
from app.deps.auth import get_user
from app.db.supabase import supabase

router = APIRouter(prefix="/stats")

@router.get("/")
def get_stats(user=Depends(get_user)):
    user_id = user["sub"]
    role = user.get("role")

    query = supabase.table("rides").select("*")

    if role != "accountant":
        query = query.eq("user_id", user_id)

    rides = query.execute().data

    total_km = sum(r["km"] for r in rides)
    total_sum = total_km * 0.5

    return {
        "totalKm": total_km,
        "totalSum": total_sum
    }