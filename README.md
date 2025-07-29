
# 🌾 Crop Prediction using Machine Learning | IBM Cloud + Hugging Face Deployment

## 🚀 Live Demo

You can try the deployed project here:  
👉 [Crop Prediction App on Hugging Face](https://huggingface.co/spaces/siddhiii/Crop_Prediction)


---

## 📌 Project Overview
This project is an intelligent crop prediction system that uses machine learning models to suggest the most suitable crop based on soil, weather, and environmental parameters like temperature, humidity, pH, and rainfall. The model is deployed on IBM Cloud using Hugging Face for accessible API-based predictions.

✅ Goal: Help farmers and agri-based platforms make data-driven decisions  
🚀 Tools Used: IBM Cloud, Hugging Face, Python (Pandas, Scikit-Learn), Jupyter, Flask API

---

## 🔍 Problem Statement
Crop selection is crucial for maximizing yield and sustainable agriculture. Traditional methods rely on experience or guesswork, which often leads to poor results. This project leverages data science to predict the optimal crop suited for specific environmental conditions.

---

## 📊 Features

- ✅ ML-based crop recommendation system  
- ✅ Trained model using scikit-learn (Random Forest Classifier)  
- ✅ Clean, preprocessed dataset with real agricultural inputs  
- ✅ Hosted API on Hugging Face via IBM Cloud  
- ✅ Easy-to-use REST API endpoint for real-time predictions

---

## 💡 Dataset Used
The dataset contains agricultural records with the following attributes:

- `N` (Nitrogen content in soil)
- `P` (Phosphorous)
- `K` (Potassium)
- `temperature` (°C)
- `humidity` (%)
- `pH` level
- `rainfall` (mm)
- `label` (recommended crop)

> 📂 Source: Kaggle [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

---

## 🧠 ML Model

- **Algorithm:** Random Forest Classifier  
- **Accuracy:** ~98%  
- **Evaluation:** Confusion Matrix, Accuracy Score  
- **Libraries Used:** `pandas`, `numpy`, `scikit-learn`, `joblib`, `flask`

---
## Model Screenshots


<!-- First Row -->
<p align="center">
  <img src="Screenshot%20(78).png" alt="Screenshot 78" width="30%" />
  <img src="Screenshot%20(79).png" alt="Screenshot 79" width="30%" />
  <img src="Screenshot%20(80).png" alt="Screenshot 80" width="30%" />
</p>

<!-- Second Row -->
<p align="center">
  <img src="Screenshot%20(81).png" alt="Screenshot 81" width="30%" />
  <img src="Screenshot%20(83).png" alt="Screenshot 83" width="30%" />
  <img src="Screenshot%20(84).png" alt="Screenshot 84" width="30%" />
</p>




## ☁️ IBM Cloud + Hugging Face Deployment

- Trained ML model exported using `joblib`
- API built using Flask and tested locally
- Deployed via Hugging Face Spaces and IBM Cloud trial environment

---

## 📦 How to Run Locally

```bash
git clone https://github.com/yourusername/crop-prediction-ibm.git
cd crop-prediction-ibm
pip install -r requirements.txt
python app.py
