from typing import Any, Annotated

from fastapi import APIRouter, Body, Depends

from app.application.form import filter_matching_forms
from app.application.models import FormField
from app.application.protocols.database import DatabaseGateway

form_router = APIRouter()


@form_router.post("/get_form")
async def get_form(
        database: Annotated[DatabaseGateway, Depends()],
        form_data: dict[str, str] = Body(),
) -> Any:
    search_fields = []
    for key, value in form_data.items():
        search_fields.append(FormField(name=key, field={"value": value}))
    data = await database.get_matching_forms(search_fields)
    res = await filter_matching_forms(data, search_fields)
    return res

# {
#   "additionalProp1": "string",
#   "additionalProp2": "+79111111111",
#   "additionalProp3": "12.12.2001",
#   "additionalProp4": "2001-12-12",
#   "additionalProp5": "123@mail.ru"
# }
