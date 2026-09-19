from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import main_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"msg": "Hello World!"}


app.include_router(main_router)
