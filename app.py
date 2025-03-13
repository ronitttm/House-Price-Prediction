from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# Load trained model & scaler
with open("xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)  # Load the same StandardScaler used in training



# Initialize FastAPI app
app = FastAPI()

# ✅ Allow CORS for all origins (for testing, restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["https://your-frontend-url.com"] in production
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allows OPTIONS method
    allow_headers=["*"],
)


# Define input format
class HouseFeatures(BaseModel):
    MedInc: float	
    HouseAge: float		
    AveRooms: float		
    AveBedrms: float		
    Population: float		
    AveOccup: float		
    Latitude: float		
    Longitude: float

# Prediction endpoint
@app.post("/predict")
def predict_price(data: HouseFeatures):
        # Convert input data to NumPy array
        input_data = np.array([[data.MedInc, data.HouseAge, data.AveRooms, data.AveBedrms, 
                                data.Population, data.AveOccup, data.Latitude, data.Longitude]])
        
        # Apply the same StandardScaler used in training
        input_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_scaled)[0]
        
        return {"predicted_price": float(prediction)}



