# models.py

from pydantic import BaseModel

class KeyValueRequest(BaseModel):
    key: str
    value: str
