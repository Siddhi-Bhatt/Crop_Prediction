import gradio as gr
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_fn(N, P, K, temperature, humidity, ph, rainfall):
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(features)[0]
    return prediction

gr.Interface(
    fn=predict_fn,
    inputs=[
        gr.Number(label="Nitrogen"),
        gr.Number(label="Phosphorus"),
        gr.Number(label="Potassium"),
        gr.Number(label="Temperature (°C)"),
        gr.Number(label="Humidity (%)"),
        gr.Number(label="pH Level"),
        gr.Number(label="Rainfall (mm)")
    ],
    outputs="text",
    title="🌱 Crop Recommendation Model",
    description="Predicts the most suitable crop based on soil and climate parameters"
).launch()
