from unittest.mock import patch

import httpx

HEADERS = {"x-api-key": "supersecreta123"}

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
    response = client.get("/inventory/1", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["type"] == "inventory"
    assert data["attributes"]["name"] == "Zapato"
    assert data["attributes"]["price"] == 99.99

@patch("app.application.use_cases.httpx.get")
def test_get_inventory_not_found(mock_get, client):
    mock_get.return_value = httpx.Response(status_code=404, json={"detail": "Not Found"})
    response = client.get("/inventory/1", headers=HEADERS)
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Product not found"

@patch("app.application.use_cases.httpx.get")
def test_update_inventory(mock_get, client):
    mock_get.return_value = httpx.Response(status_code=200, json={"data": {
        "type": "products",
        "id": 1,
        "attributes": {
            "name": "Zapato",
            "price": 99.99
        }
    }})
    response = client.post(f"/inventory/1?quantity=10", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["type"] == "inventory"
    assert data["attributes"]["name"] == "Zapato"
    assert data["attributes"]["price"] == 99.99
    assert data["attributes"]["quantity"] == 10

@patch("app.application.use_cases.httpx.get")
def test_get_inventory_not_found_with_retry(mock_get, client):
    mock_get.return_value = httpx.Response(status_code=404, json={"detail": "Not Found"})
    response = client.get("/inventory/1", headers=HEADERS)
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Product not found"