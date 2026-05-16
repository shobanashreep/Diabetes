# Diabetes Prediction using Artificial Neural Network (ANN)

## Project Overview

This project is a Deep Learning based web application that predicts whether a person is likely to have diabetes based on medical parameters.

The model is built using TensorFlow and Keras and deployed using Streamlit.

---

## Features

- Predicts diabetes risk using patient medical data
- Interactive web interface using Streamlit
- Deep Learning model using ANN
- Real-time prediction
- Clean and beginner-friendly implementation

---

## Technologies Used

- Python
- TensorFlow
- Keras
- Streamlit
- NumPy
- Pandas
- Scikit-learn

---

## Dataset Information

The dataset contains medical diagnostic measurements such as:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

Target Output:
- 0 → No Diabetes
- 1 → Diabetes

---

## Model Architecture

Input Layer:
- 8 input features

Hidden Layers:
- Dense layer with 12 neurons (ReLU)
- Dense layer with 8 neurons (ReLU)

Output Layer:
- Dense layer with 1 neuron (Sigmoid)

Optimizer:
- Adam

Loss Function:
- Binary Crossentropy

---

## Project Structure

```text
diabetes_prediction_project/
│
├── train_model.ipynb
├── diabetes_model.keras
├── app.py
├── requirements.txt
└── README.md
