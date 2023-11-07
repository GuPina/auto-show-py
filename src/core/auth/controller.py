from fastapi import APIRouter
from src.core.auth.service import AuthService

from src.core.auth.schema import Login

router = APIRouter()

@router.post('/login')
async def login(dto: Login):
    service = AuthService()
    return service.login(dto)