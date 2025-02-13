import os
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv, find_dotenv

import jwt
import pytest

load_dotenv(find_dotenv("test.env"))


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


@pytest.fixture
def jwt_auth_token():
    access_token_expires = timedelta(minutes=60)
    token = create_access_token(
        data={"user": "david", "organization": "ABC Corp", "permissions": ["read"]},
        secret=os.getenv("SECRET_KEY"),
        algo=os.getenv("ALGORITHM"),
        expires_delta=access_token_expires,
    )
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    return headers


@pytest.fixture
def jwt_auth_token_no_permissions():
    access_token_expires = timedelta(minutes=60)
    token = create_access_token(
        data={"user": "Derek", "organization": "ABC Corp", "permissions": []},
        secret=os.getenv("SECRET_KEY"),
        algo=os.getenv("ALGORITHM"),
        expires_delta=access_token_expires,
    )
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    return headers


@pytest.fixture
def jwt_auth_token_invalid_format():
    access_token_expires = timedelta(minutes=60)
    token = create_access_token(
        data={"user": "Derek", "organization": "ABC Corp"},
        secret=os.getenv("SECRET_KEY"),
        algo=os.getenv("ALGORITHM"),
        expires_delta=access_token_expires,
    )
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    return headers


@pytest.fixture
def api_key():
    api_key = os.getenv("API_KEY")
    headers = {"Content-Type": "application/json", "x-api-key": api_key}
    return headers


@pytest.fixture
def invalid_api_key():
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "wrongkey",
    }
    return headers
