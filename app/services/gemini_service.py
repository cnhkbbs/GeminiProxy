from typing import Any
import httpx
from fastapi import HTTPException, Request
from fastapi.responses import StreamingResponse
from app.config.settings import settings

class GeminiService:
    def __init__(self):
        self.base_url = settings.GEMINI_BASE_URL

    async def proxy_request(self, path: str, request: Request) -> Any:
        api_key = request.headers.get("X-API-Key")
        if not api_key:
            raise HTTPException(status_code=400, detail="Missing X-API-Key header")
            
        url = f"{self.base_url}{path}"
        if "key=" not in url:
            url = f"{url}{'&' if '?' in url else '?'}key={api_key}"

        headers = {k: v for k, v in request.headers.items()
                  if k.lower() not in ["host", "x-auth-key", "x-api-key"]}
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(
                    method=request.method,
                    url=url,
                    headers=headers,
                    content=await request.body(),
                    timeout=None
                )
                
                if "text/event-stream" in response.headers.get("content-type", ""):
                    return StreamingResponse(
                        response.aiter_bytes(),
                        media_type="text/event-stream"
                    )
                
                return response.json()
                
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
