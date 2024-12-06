from typing import Annotated

from fastapi import APIRouter, Body, Depends

from app.application.form import get_matching_forms
from app.application.models import GetFormResponse, FormTemplate
from app.application.protocols.database import DatabaseGateway

form_router = APIRouter()


@form_router.post("/get_form", response_model=list[GetFormResponse])
async def get_form(
        database: Annotated[DatabaseGateway, Depends()],
        form_data: dict[str, str] = Body(),
) -> list[FormTemplate]:
    forms = await get_matching_forms(form_data, database)
    return forms
