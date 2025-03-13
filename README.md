# 🏡 House Price Prediction API  

This API predicts house prices based on various features such as median income, house age, number of rooms, and location details. The API is built using **FastAPI** and is deployed on **Render**.  

## 🚀 Deployment  
- **Backend (FastAPI) hosted on Render:** https://house-price-prediction-tu3t.onrender.com
- **Frontend hosted on Netlify:** https://houseprice-prediction.netlify.app/

💡 **You can use this API directly through the frontend by visiting the Netlify-hosted website.**  

---

## 📌 API Endpoints  

### 1️⃣ **POST `/predict`**  
This endpoint takes input features as JSON and returns the predicted house price.  

#### 🔹 **Request Format (JSON)**  
```json
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
```  

#### 🔹 **Response Format (JSON)**  
```json
{
    "predicted_price": 1.51234
}
```  

---

## 🛠 How to Use the API  

### 🔹 **1. Using the Frontend**  
The easiest way to use this API is through the web interface:  
🔗 **https://houseprice-prediction.netlify.app/**  

1. Enter the required values in the form.  
2. Click **Predict Price** and get the predicted house price instantly.  

### 🔹 **2. Using Postman**  
1. Open Postman and create a new `POST` request.  
2. Enter the API URL:  
   ```
   https://house-price-prediction-tu3t.onrender.com/predict
   ```
3. In the **Body** tab, select **raw** and choose **JSON** format.  
4. Paste the request JSON (see above).  
5. Click **Send** and view the response.  

  
---

  
---

## 🔧 Tech Stack  
- **Backend:** FastAPI, Python, XGBoost  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** Render (Backend), Netlify (Frontend)  
