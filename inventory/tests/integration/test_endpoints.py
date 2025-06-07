from unittest.mock import patch

import httpx


@patch("app.application.use_cases.httpx.get")
def test_get_inventory(mock_get, client):
    mock_get.return_value = httpx.Response(status_code=200, json={"data": {
        "type": "products",
        "id": 1,
        "attributes": {
            "name": "Zapato",
            "price": 99.99
        }
    }})
    headers = {"x-api-key": "supersecreta123"}
    response = client.get("/inventory/1", headers=headers)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["type"] == "inventory"
    assert data["attributes"]["name"] == "Zapato"
    assert data["attributes"]["price"] == 99.99