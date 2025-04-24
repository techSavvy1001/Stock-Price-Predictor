from fastapi import FastAPI, Request
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Load the trained model
with open("app/model.pkl", "rb") as f:
    model = pickle.load(f)

class StockData(BaseModel):
    features: list  # Example: [value1, value2, ...]

@app.post("/predict")
def predict(data: StockData):
    features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features)
    return {"predicted_price": prediction[0]}
