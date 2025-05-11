from fastapi import FastAPI
from app.schemas import ShipmentInput, PredictionResponse
from app.model import predict_delay

app = FastAPI()

@app.post("/predict", response_model=PredictionResponse)
def predict_shipment(input: ShipmentInput):
    result = predict_delay(input.dict())
    return PredictionResponse(prediction=result)
