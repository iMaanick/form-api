from typing import Union

from pydantic import BaseModel

from app.application.models import Email, Phone, Date, Text


class FormField(BaseModel):
    name: str
    field: Union[Email, Phone, Date, Text]
