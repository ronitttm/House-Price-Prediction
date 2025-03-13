🏡 House Price Prediction API
This API predicts house prices based on various features such as median income, house age, number of rooms, and location details. The API is built using FastAPI and is deployed on Render.

🚀 Deployment
Backend (FastAPI) hosted on Render: House Price Prediction API
Frontend hosted on Netlify: House Price Prediction App
💡 You can use this API directly through the frontend by visiting the Netlify-hosted website.

📌 API Endpoints
1️⃣ POST /predict
This endpoint takes input features as JSON and returns the predicted house price.

🔹 Request Format (JSON)
json
Copy
Edit
{
    "MedInc": 3.5,
    "HouseAge": 20,
    "AveRooms": 5.2,
    "AveBedrms": 1.1,
    "Population": 1000,
    "AveOccup": 3.0,
    "Latitude": 37.5,
    "Longitude": -122.2
}
🔹 Response Format (JSON)
json
Copy
Edit
{
    "predicted_price": 150000.1234
}
🛠 How to Use the API
🔹 1. Using the Frontend
The easiest way to use this API is through the web interface:
🔗 House Price Prediction App

Enter the required values in the form.
Click Predict Price and get the predicted house price instantly.
🔹 2. Using Postman
Open Postman and create a new POST request.
Enter the API URL:
bash
Copy
Edit
https://house-price-prediction-tu3t.onrender.com/predict
In the Body tab, select raw and choose JSON format.
Paste the request JSON (see above).
Click Send and view the response.
🔹 3. Using cURL
sh
Copy
Edit
curl -X POST "https://house-price-prediction-tu3t.onrender.com/predict" \
     -H "Content-Type: application/json" \
     -d '{"MedInc": 3.5, "HouseAge": 20, "AveRooms": 5.2, "AveBedrms": 1.1, "Population": 1000, "AveOccup": 3.0, "Latitude": 37.5, "Longitude": -122.2}'
🖥 Frontend Integration
The frontend form submits data to this API using a fetch request:

js
Copy
Edit
const response = await fetch("https://house-price-prediction-tu3t.onrender.com/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
});
const result = await response.json();
console.log("Predicted Price: $" + result.predicted_price.toFixed(4));
