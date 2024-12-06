from typing import Any, Annotated

from fastapi import APIRouter, Body, Depends

from app.application.form import get_matching_forms
from app.application.protocols.database import DatabaseGateway

form_router = APIRouter()


@form_router.post("/get_form")
async def get_form(
        database: Annotated[DatabaseGateway, Depends()],
        form_data: dict[str, str] = Body(),
) -> Any:
    forms = await get_matching_forms(form_data, database)
    return forms

# {
#   "additionalProp1": "string",
#   "additionalProp2": "+79111111111",
#   "additionalProp3": "12.12.2001",
#   "additionalProp4": "2001-12-12",
#   "additionalProp5": "123@mail.ru"
# }
