from fastapi import FastAPI
from src.core.config import get_settings
from src.core.logger import ApiLogger

app = FastAPI()

@app.get('/')
async def root():
    settings = get_settings()
    api_logger = ApiLogger()

    api_logger.debug('This is a debug line')
    api_logger.info('This is a info line')
    api_logger.warning('This is a warning line')
    api_logger.error('This is a error line')
    api_logger.critical('This is a critical line')

    return {'message': 'Hello World', 'log_level': settings.log_level}

@app.post('/teste-2')
async def root():
    return {'message': 'Hello World222'}

