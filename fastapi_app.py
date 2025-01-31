from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

# Load the model
model = pickle.load(open('xgboost_model.pkl', 'rb'))

app = FastAPI()

class PlayerData(BaseModel):
    player_data: list  # Replace with the structure of your input data

@app.post('/predict')
def predict(player_data: PlayerData):
    try:
        # Ensure the player data is the correct format (convert to a 2D array if needed)
        prediction = model.predict([player_data.player_data])  # Adjust as needed
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error making prediction: {str(e)}")
