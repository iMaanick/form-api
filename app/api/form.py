from typing import Annotated, Union

from fastapi import APIRouter, Body, Depends

from app.application.form import get_matching_forms, get_search_fields
from app.application.models import GetFormResponse, FormTemplate
from app.application.models.field_value_type import FieldValueType
from app.application.protocols.database import DatabaseGateway

form_router = APIRouter()


@form_router.post("/get_form", response_model=Union[list[GetFormResponse], dict[str, FieldValueType]] )
async def get_form(
        database: Annotated[DatabaseGateway, Depends()],
        form_data: dict[str, str] = Body(),
) -> Union[list[FormTemplate], dict[str, FieldValueType]]:
    search_fields = await get_search_fields(form_data)
    forms = await get_matching_forms(search_fields, database)
    if not forms:
        return {field.name: field.field.type for field in search_fields}
    return forms
