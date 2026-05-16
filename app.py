import streamlit as st
import tensorflow as tf
import numpy as np

# Load trained model
model = tf.keras.models.load_model("diabetes_model.keras")

st.title("Diabetes Prediction App")

st.write("Enter Patient Details")

pregnancies = st.number_input("Pregnancies", min_value=0.0)
glucose = st.number_input("Glucose", min_value=0.0)
blood_pressure = st.number_input("Blood Pressure", min_value=0.0)
skin_thickness = st.number_input("Skin Thickness", min_value=0.0)
insulin = st.number_input("Insulin", min_value=0.0)
bmi = st.number_input("BMI", min_value=0.0)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=1.0)

if st.button("Predict"):

    input_data = np.array([
        [
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            diabetes_pedigree,
            age
        ]
    ])

    prediction = model.predict(input_data)

    st.write("Prediction Value :", prediction[0][0])

    if prediction[0][0] > 0.5:
        st.error("Person is likely Diabetic")
    else:
        st.success("Person is likely Not Diabetic")