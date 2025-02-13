from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from app.env import SETTINGS

api_key_header = APIKeyHeader(name="x-api-key")


def authenticate_request(api_key: str = Security(api_key_header)) -> bool:
    return api_key == SETTINGS.api_key
