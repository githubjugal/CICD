from app.model import predict_delay

def test_model_prediction():
    sample = {
        "Warehouse_block": "A",
        "Mode_of_Shipment": "Flight",
        "Customer_care_calls": 3,
        "Customer_rating": 4,
        "Cost_of_the_Product": 200.0,
        "Prior_purchases": 2,
        "Product_importance": "medium",
        "Gender": "F",
        "Discount_offered": 5.0,
        "Weight_in_gms": 3000
    }
    result = predict_delay(sample)
    assert result in ["On Time", "Delayed"]
