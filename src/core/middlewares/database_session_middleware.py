from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from src.core.database import SessionLocal


class DataBaseSessionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatcha(self, request: Request, call_next: RequestResponseEndpoint):
        response = Response("Internal Server Error", status_code=500)


        try:
            request.state.db = SessionLocal()
            response = await call_next(request)
        finally:
            request.state.db.close()

        return response