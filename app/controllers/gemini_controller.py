from fastapi import APIRouter, Request, Depends
from app.services.gemini_service import GeminiService
from app.middleware.auth_middleware import verify_auth_header

router = APIRouter()
gemini_service = GeminiService()

@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"], dependencies=[Depends(verify_auth_header)])
async def proxy_gemini(request: Request, path: str):
    return await gemini_service.proxy_request(path, request)