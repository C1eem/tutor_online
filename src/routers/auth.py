from fastapi import APIRouter, Depends, HTTPException, Response, status

from dependencies.auth_jwt import config, security
from schemas.users import UserLoginSchema

router = APIRouter(prefix="/auth", tags=["Авторизация"])


@router.post("/login")
async def login(
    creds: UserLoginSchema,
    response: Response,
):
    if creds.username == "test" and creds.password == "test":
        token = security.create_access_token(uid="12345")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token": token}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
    )


@router.get("/protected", dependencies=[Depends(security.access_token_required)])
async def protected():
    return {"data": "TOP SECRETS"}
