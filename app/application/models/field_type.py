from datetime import datetime

from pydantic import BaseModel, constr
from pydantic import field_validator, EmailStr

from app.application.models.field_value_type import FieldValueType


class Date(BaseModel):
    value: constr(pattern=r'^(?:\d{4}-\d{2}-\d{2}|\d{2}\.\d{2}\.\d{4})$')

    @field_validator('value')
    def validate_date(cls, v):
        try:
            if len(v.split('-')) == 3:
                datetime.strptime(v, '%Y-%m-%d')
            elif len(v.split('.')) == 3:
                datetime.strptime(v, '%d.%m.%Y')
            else:
                raise ValueError('Invalid date format')
            return v
        except ValueError:
            raise ValueError('Invalid date format, expected DD.MM.YYYY or YYYY-MM-DD')

    type: FieldValueType = FieldValueType.date


class Email(BaseModel):
    value: EmailStr
    type: FieldValueType = FieldValueType.email


class Phone(BaseModel):
    value: constr(pattern=r'^\+7\d{10}$')
    type: FieldValueType = FieldValueType.phone


class Text(BaseModel):
    value: str
    type: FieldValueType = FieldValueType.text
