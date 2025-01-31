import joblib
from flask import Flask, request, jsonify
import numpy as np
import pandas as pd

# Load your pre-trained model
model = joblib.load('xgboost_model.pkl')

# Initialize the Flask app
app = Flask(__name__)

# Define an endpoint for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data as a JSON
    data = request.get_json()
    
    # Convert the data to a DataFrame (this may vary based on your input data format)
    input_data = pd.DataFrame(data)
    
    # Make prediction using the model
    predictions = model.predict(input_data)
    
    # Return the predictions as JSON
    return jsonify({'predictions': predictions.tolist()})

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
