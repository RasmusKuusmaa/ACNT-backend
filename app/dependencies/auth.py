import jwt
from fastapi import HTTPException, Header
from app.core.config import settings

SUPABASE_JWT_SECRET = settings.SUPABASE_SERVICE_ROLE_KEY 

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")

    try:
        token = authorization.replace("Bearer ", "")

        payload = jwt.decode(
            token,
            options={"verify_signature": False}  
        )

        return payload

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")