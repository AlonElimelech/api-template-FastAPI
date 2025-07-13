# pip install PyJWT
from jwt import encode

shared_secret = "supersecret"
payload = {
    "iss": "argo",
    "aud": "dns-api",
}
token = encode(payload, shared_secret, algorithm="HS256")
print(token)
