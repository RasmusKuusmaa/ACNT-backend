from fastapi import APIRouter, Depends
from app.deps.auth import get_user
from app.db.supabase import supabase

router = APIRouter(prefix="/rides")

@router.get("/")
def get_rides(user=Depends(get_user)):
    user_id = user["sub"]
    role = user.get("role")

    query = supabase.table("rides").select("*")

    if role != "accountant":
        query = query.eq("user_id", user_id)

    return query.execute().data


@router.post("/")
def add_ride(ride: dict, user=Depends(get_user)):
    user_id = user["sub"]

    ride["user_id"] = user_id

    return supabase.table("rides").insert(ride).execute().data

@router.post("/bulk")
def add_rides_bulk(rides: list[dict], user=Depends(get_user)):
    user_id = user["sub"]

    for ride in rides:
        ride["user_id"] = user_id
        ride.pop("id", None)

    return supabase.table("rides").insert(rides).execute().data