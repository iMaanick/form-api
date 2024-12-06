from enum import Enum


class FieldValueType(str, Enum):
    email = "email"
    phone = "phone"
    date = "date"
    text = "text"
