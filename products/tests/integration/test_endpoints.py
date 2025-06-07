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

def test_get_product_by_id(client):
    response = client.post("/products", json={
        "name": "Pantalón",
        "price": 89.5
    })
    assert response.status_code == 201
    data = response.json()["data"]
    product_id = data["id"]
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["type"] == "products"
    assert data["id"] == product_id
    assert data["attributes"]["name"] == "Pantalón"
    assert data["attributes"]["price"] == 89.5


def test_get_products(client):
    response = client.post("/products", json={
        "name": "Pantalón",
        "price": 89.5
    })
    assert response.status_code == 201
    data = response.json()["data"]
    product_id = data["id"]
    response = client.get("/products")
    assert response.status_code == 200
    data = response.json()["data"]
    assert len(data) == 1
    assert data[0]["type"] == "products"
    assert data[0]["id"] == product_id
    assert data[0]["attributes"]["name"] == "Pantalón"
    assert data[0]["attributes"]["price"] == 89.5   