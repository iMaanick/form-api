from enum import Enum


class FormValueType(str, Enum):
    email = "email"
    phone = "телефон"
    date = "дата"
    text = "текст"
