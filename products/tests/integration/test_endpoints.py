def test_create_product(client):
    response = client.post("/products", json={
        "name": "Pantalón",
        "price": 89.5
    })
    assert response.status_code == 201
    data = response.json()["data"]
    assert data["type"] == "products"
    assert data["attributes"]["name"] == "Pantalón"
    assert data["attributes"]["price"] == 89.5