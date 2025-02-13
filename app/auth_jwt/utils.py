from datetime import timedelta, datetime, timezone
import jwt
from app.env import SETTINGS


# This function is not used by FASTAPI. It is used by tests to create a token
def create_access_token(
    data: dict, secret: str, algo: str, expires_delta: timedelta | None = None
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret, algo)
    return encoded_jwt


def decode_access_token(token: str, secret: str, algo: str):
    return jwt.decode(token, secret, algorithms=[algo])
