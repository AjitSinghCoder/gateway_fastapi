from fastapi import HTTPException, Request,Depends
from fastapi.security import OAuth2PasswordBearer,APIKeyHeader
import jwt
from dotenv import load_dotenv
import os

load_dotenv()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

API_KEY_NAME = "Authorization"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def verify_token(token: str = Depends(api_key_header)):
    try:
        if not token:
            raise HTTPException(
                status_code=401,
                detail="You didn't pass the api key in the header! Header: x-api-key",
            )
        
        if not token.startswith("Bearer "):
            raise HTTPException(
                status_code=401,
                detail="Invalid token format. Expected 'Bearer <token>'",
            )
        token = token.split(" ")[1]
        # Decode the J
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
