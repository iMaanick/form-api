from pydantic import BaseModel


class GetFormResponse(BaseModel):
    name: str
