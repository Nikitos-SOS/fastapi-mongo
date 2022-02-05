from fastapi import FastAPI

from server.routes.student import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouter, tags=['Student'], prefix='/student')

@app.get('/', description='Root', tags=['root'])
async def get_root():
    return {'message':'Hello, world'}