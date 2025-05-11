from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/predict", json={
        "Warehouse_block": "B",
        "Mode_of_Shipment": "Ship",
        "Customer_care_calls": 2,
        "Customer_rating": 3,
        "Cost_of_the_Product": 150,
        "Prior_purchases": 1,
        "Product_importance": "low",
        "Gender": "M",
        "Discount_offered": 10,
        "Weight_in_gms": 2500
    })
    assert response.status_code == 200
    assert response.json()["prediction"] in ["On Time", "Delayed"]
