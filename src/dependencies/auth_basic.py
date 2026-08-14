from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

def get_current_user_basic(
    credentials: HTTPBasicCredentials = Depends(security),
    
)
