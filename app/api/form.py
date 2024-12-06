from typing import Any

from fastapi import APIRouter, Body

from app.application.models import FormField

form_router = APIRouter()


@form_router.post("/get_form")
async def get_form(
        form_data: dict[str, str] = Body()
) -> Any:
    fields = []
    for key, value in form_data.items():
        fields.append(FormField(name=key, field={"value": value}))
        print(fields[-1].field)
    return {"1": 1}

# {
#   "additionalProp1": "string",
#   "additionalProp2": "+79111111111",
#   "additionalProp3": "12.12.2001",
#   "additionalProp4": "2001-12-12",
#   "additionalProp5": "123@mail.ru"
# }
