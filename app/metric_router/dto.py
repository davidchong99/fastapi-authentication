from uuid import UUID
from pydantic import BaseModel


class MetricData(BaseModel):
    id: int
    name: str
    value: int
