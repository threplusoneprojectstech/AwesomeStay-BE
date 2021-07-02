from fastapi import security
import jwt
import time
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET = "2ab9aa21482f4e138e3b363f7183350c"

def SignJWT(userId: str):
    payload = {
        "user_id": userId,
        "expires": time.time()+3600
    }
    token = jwt.encode(payload, SECRET, algorithm="HS256")
    
    return token

class JWTBearer(HTTPBearer):
    def __init__(this, auto_error:bool = True):
        super(JWTBearer, this).__init__(auto_error=auto_error)
    async def __call__(this, request: Request):
        credentials: HTTPAuthorizationCredentials= await super(JWTBearer, this).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="invalid authorization")
            if not this.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="invalid / expiredd token")
        else:
            raise HTTPException(status_code=403, detail="invalid authorization code")
    def verify_jwt(self, token: str) -> bool:
        try:
            decoded_token = jwt.decode(token, SECRET, algorithms=["HS256"])
            if decoded_token["expires"] >= time.time():
                return True
            else:
                return False
        except:
            return False
