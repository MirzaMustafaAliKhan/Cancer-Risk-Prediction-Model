from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.responses import RedirectResponse


app = FastAPI()

# Load the scaler and model
scaler = joblib.load("scaler.pkl")
model = joblib.load("best_model.pkl")

# Define the input data model
class CancerData(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float
    radius_se: float
    texture_se: float
    perimeter_se: float
    area_se: float
    smoothness_se: float
    compactness_se: float
    concavity_se: float
    concave_points_se: float
    symmetry_se: float
    fractal_dimension_se: float
    radius_worst: float
    texture_worst: float
    perimeter_worst: float
    area_worst: float
    smoothness_worst: float
    compactness_worst: float
    concavity_worst: float
    concave_points_worst: float
    symmetry_worst: float
    fractal_dimension_worst: float

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

@app.post("/predict")
def predict(data: CancerData):
    # Create input array in the exact order
    input_array = np.array([[ 
        data.radius_mean,
        data.texture_mean,
        data.perimeter_mean,
        data.area_mean,
        data.smoothness_mean,
        data.compactness_mean,
        data.concavity_mean,
        data.concave_points_mean,
        data.symmetry_mean,
        data.fractal_dimension_mean,
        data.radius_se,
        data.texture_se,
        data.perimeter_se,
        data.area_se,
        data.smoothness_se,
        data.compactness_se,
        data.concavity_se,
        data.concave_points_se,
        data.symmetry_se,
        data.fractal_dimension_se,
        data.radius_worst,
        data.texture_worst,
        data.perimeter_worst,
        data.area_worst,
        data.smoothness_worst,
        data.compactness_worst,
        data.concavity_worst,
        data.concave_points_worst,
        data.symmetry_worst,
        data.fractal_dimension_worst
    ]])

    # Scale the input
    scaled_input = scaler.transform(input_array)

    # Predict risk
    risk_probability = model.predict_proba(scaled_input)[0][1]

    return {"cancer_risk_probability": round(risk_probability, 4)}