from fastapi import FastAPI

from src.api import main_router

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Hello World!"}


app.include_router(main_router)
