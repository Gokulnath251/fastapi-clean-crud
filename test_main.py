from fastapi.testclient import TestClient
from main import app

# Create a test client simulating an HTTP caller (browser or frontend)
client = TestClient(app)

def test_list_products():
    """Verify that listing products returns 200 OK and a list."""
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_product_success():
    """Verify that creating a valid product returns 201 Created."""
    payload = {
        "name": "MRF Cricket Bat",
        "price": 3200.0,
        "cost_price": 2400.0,
        "in_stock": True
    }
    response = client.post("/products", json=payload)
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == "MRF Cricket Bat"
    assert data["price"] == 3200.0
    # Ensure cost_price was excluded by response_model for security
    assert "cost_price" not in data

def test_create_product_invalid_price():
    """Verify that negative prices get rejected with 422 Unprocessable Entity."""
    payload = {
        "name": "Invalid Ball",
        "price": -50.0,
        "cost_price": 20.0,
        "in_stock": True
    }
    response = client.post("/products", json=payload)
    assert response.status_code == 422
