from pydantic import BaseModel

from app.application.models import FormField


class FormTemplate(BaseModel):
    name: str
    fields: list[FormField]
