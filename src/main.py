from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.post('/teste-2')
async def root():
    return {'message': 'Hello World222'}

