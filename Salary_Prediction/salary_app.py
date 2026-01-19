import streamlit as st
import pandas as pd
import pickle
import tensorflow as tf

# Load model & preprocessor
model = tf.keras.models.load_model("salary_model.h5")

with open("salary_preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)

st.title("Customer Salary Prediction")

credit_score = st.number_input("Credit Score", 300, 900, 600)
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 92, 40)
tenure = st.slider("Tenure", 0, 10, 3)
balance = st.number_input("Balance", value=60000.0)
num_products = st.slider("Number of Products", 1, 4, 2)
has_cr = st.selectbox("Has Credit Card", [0, 1])
active = st.selectbox("Is Active Member", [0, 1])

input_df = pd.DataFrame({
    "CreditScore": [credit_score],
    "Geography": [geography],
    "Gender": [gender],
    "Age": [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [num_products],
    "HasCrCard": [has_cr],
    "IsActiveMember": [active]
})

input_processed = preprocessor.transform(input_df)
salary_pred = model.predict(input_processed)[0][0]

st.subheader(f"Estimated Salary: ₹ {salary_pred:,.0f}")
