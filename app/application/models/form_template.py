from pydantic import BaseModel

from app.adapters.sqlalchemy_db.models.field_value_type import FieldValueType


class FormTemplate(BaseModel):
    id: int
    name: str
    fields: dict[str, FieldValueType]
