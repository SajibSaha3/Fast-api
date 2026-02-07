from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(title="Iris Classification API")

# Load model safely
try:
    with open("iris.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionOutput(BaseModel):
    prediction: str

@app.get("/")
def root():
    return {"message": "Iris Classification API is running"}

@app.post("/predict", response_model=PredictionOutput)
def predict(data: IrisInput):
    try:
        features = np.array([[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]])

        prediction = model.predict(features)
        return {"prediction": prediction[0]}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
