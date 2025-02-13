from pydantic import BaseModel
from uuid import UUID


class Identity(BaseModel):
    user: str
    organization: str
    permissions: list[str]
    exp: int
