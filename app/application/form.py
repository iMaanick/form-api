from app.application.models import FormTemplate, FormField
from app.application.protocols.database import DatabaseGateway


async def filter_matching_forms(
        form_templates: list[FormTemplate],
        search_fields: list[FormField]
) -> list[FormTemplate]:
    matching_forms = []
    for form in form_templates:
        if all(form.fields.get(field.name) == field.field.type for field in search_fields):
            matching_forms.append(form)
    return matching_forms


async def get_search_fields(
        form_data: dict[str, str],
) -> list[FormTemplate]:
    search_fields = []
    for name, field_value in form_data.items():
        search_fields.append(FormField(name=name, field={"value": field_value}))
    return search_fields


async def get_matching_forms(
        form_data: dict[str, str],
        database: DatabaseGateway,
) -> list[FormTemplate]:
    search_fields = await get_search_fields(form_data)
    forms = await database.get_matching_forms(len(search_fields))
    matching_forms = await filter_matching_forms(forms, search_fields)
    return matching_forms
