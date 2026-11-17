''' ASGI - Asynchronous Server Gateway Interface
    - Uvicorn
    - Hypercorn
    - Daphne
FastAPI
'''
from fastapi import FastAPI
app=FastAPI()
@app.get("/")
async def root():
    return {"message": "Help, world"}