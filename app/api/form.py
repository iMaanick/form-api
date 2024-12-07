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
    """
    Handles POST requests to match a submitted form against predefined form templates.

    **Endpoint**: `/get_form`

    ### Request:
    - **Method**: POST
    - **Body**: A dictionary containing field names as keys and their respective values as strings.

    Example:
    ```json
    {
        "Email Address": "user1@example.com",
        "Phone Number": "+71234567890",
        "Birth Date": "2000-01-01"
    }
    ```

    ### Response:
    - If a matching template is found:
      A list of dictionaries containing the names of matching form templates.
      Example:
      ```json
      [
          {
              "name": "Registration Form"
          }
      ]
      ```
    - If no matching template is found:
      A dictionary with field names as keys and their determined types as values.
      Example:
      ```json
      {
          "Email Address": "email",
          "Phone Number": "phone",
          "Birth Date": "date"
      }
      ```

    ### Parameters:
    - `database` (DatabaseGateway): Injected dependency for database interaction.
    - `form_data` (dict[str, str]): Submitted form fields and their respective values.

    ### Returns:
    - `Union[list[FormTemplate], dict[str, FieldValueType]]`:
      - A list of matching form templates or
      - A dictionary with field types if no match is found.
    """
    search_fields = await get_search_fields(form_data)
    forms = await get_matching_forms(search_fields, database)
    if not forms:
        return {field.name: field.field.type for field in search_fields}
    return forms
