from app.application.models import FormTemplate, FormField


async def filter_matching_forms(
        form_templates: list[FormTemplate],
        search_fields: list[FormField]
) -> list[FormTemplate]:
    matching_forms = []
    for form in form_templates:
        if all(form.fields.get(field.name) == field.field.type for field in search_fields):
            matching_forms.append(form)
    return matching_forms
