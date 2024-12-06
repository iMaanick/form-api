from unittest.mock import AsyncMock

from _pytest.monkeypatch import MonkeyPatch
from starlette import status
from starlette.testclient import TestClient

from app.application.models import FormTemplate
from app.application.models.field_value_type import FieldValueType


def test_get_form_unprocessable_entity_params(
        client: TestClient,
        mock_database_gateway: AsyncMock,
        monkeypatch: MonkeyPatch
) -> None:
    params = {'key1': 'value1', 'key2': 'value2'}
    response = client.post(
        "/get_form",
        params=params,
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_get_form_unprocessable_entity_json(
        client: TestClient,
        mock_database_gateway: AsyncMock,
        monkeypatch: MonkeyPatch
) -> None:
    data = {'integer': 123, 'boolean': True, 'list': ['a', 'b', 'c']}
    response = client.post(
        "/get_form",
        json=data,
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_get_form_check_types(
        client: TestClient,
        mock_database_gateway: AsyncMock,
        monkeypatch: MonkeyPatch
) -> None:
    mock_database_gateway.get_matching_forms.return_value = []
    data = {
        "additionalProp1": "string",
        "additionalProp2": "+79111111111",
        "additionalProp3": "12.12.2001",
        "additionalProp4": "2001-12-12",
        "additionalProp5": "123@mail.ru"
    }

    response = client.post(
        "/get_form",
        json=data,
    )
    assert response.json() == {
        'additionalProp1': 'text',
        'additionalProp2': 'phone',
        'additionalProp3': 'date',
        'additionalProp4': 'date',
        'additionalProp5': 'email'
    }


def test_get_form_success(
        client: TestClient,
        mock_database_gateway: AsyncMock,
        monkeypatch: MonkeyPatch
) -> None:
    mock_database_gateway.get_matching_forms.return_value = [
        FormTemplate(
            id=1,
            name="First",
            fields={"email": FieldValueType.email}
        ),
        FormTemplate(
            id=2,
            name="Second",
            fields={"Text": FieldValueType.text}
        ),
    ]
    data = {
        "email": "MNK@mail.ru",
    }

    response = client.post(
        "/get_form",
        json=data,
    )
    assert response.json() == [{'name': 'First'}]
