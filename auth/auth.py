from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import decode, PyJWTError


# JWT_SECRET = os.getenv("JWT_SECRET")# For demonstration purposes, using a hardcoded secret
JWT_SECRET = "supersecret"  # Stored in env/Vault for API only
ALGORITHM = "HS256"
EXPECTED_ISSUER = "argo"
EXPECTED_AUDIENCE = "dns-api"  # Change per API

auth_scheme = HTTPBearer()

def verify_jwt(token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    print(f"Verifying JWT: {token.credentials}")
    try:
        payload = decode(token.credentials, JWT_SECRET, audience=EXPECTED_AUDIENCE, algorithms=[ALGORITHM])
        print(f"Decoded JWT payload: {payload}")
        if payload["iss"] != EXPECTED_ISSUER:
            raise HTTPException(status_code=403, detail="Invalid issuer")
        if payload["aud"] != EXPECTED_AUDIENCE:
            raise HTTPException(status_code=403, detail="Invalid audience")
    except PyJWTError as e:
        raise HTTPException(status_code=403, detail=str(e))

    return payload
