from fastapi import HTTPException
from src.core.auth.schema import Login


class AuthService:
    def login(self, dto: Login):
        if not (dto.login == 'admin@admin.com' and dto.password == '55882122'):
            raise HTTPException(400, 'Usuario ou senha invalido')
        
        return {'message': 'Usuario autenticado'}