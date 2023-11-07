from fastapi import FastAPI
from src.core.config import get_settings

app = FastAPI()

@app.get('/')
async def root():
    settings = get_settings()
    return {'message': 'Hello World', 'log_level': settings.log_level}

@app.post('/teste-2')
async def root():
    return {'message': 'Hello World222'}

