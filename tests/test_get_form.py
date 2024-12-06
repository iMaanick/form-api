from unittest.mock import AsyncMock

from _pytest.monkeypatch import MonkeyPatch
from starlette import status
from starlette.testclient import TestClient


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
