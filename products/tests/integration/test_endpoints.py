def test_create_product(client):
    response = client.post("/products", json={
        "name": "Pantalón",
        "price": 89.5
    })
    assert response.status_code == 201
    data = response.json()["data"]
    assert data["type"] == "productos"
    assert data["attributes"]["nombre"] == "Pantalón"
    assert data["attributes"]["precio"] == 89.5