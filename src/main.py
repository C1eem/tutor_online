# import os
# import sys

# sys.path.insert(1, os.path.join(sys.path[0], ".."))

import uvicorn
from fastapi import FastAPI

from routers.admin import router as admin_router
from routers.users import router as user_router

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Hello World!"}


app.include_router(user_router)
app.include_router(admin_router)
