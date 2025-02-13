from pydantic import BaseModel


class Organization(BaseModel):
    org: str
