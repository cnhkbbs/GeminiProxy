from fastapi import Request, HTTPException
from app.config.settings import settings

async def verify_auth_header(request: Request):
    auth_header = request.headers.get("X-Auth-Key")
    if not auth_header or auth_header != settings.AUTH_SECRET_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")