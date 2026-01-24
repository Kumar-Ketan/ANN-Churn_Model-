📊 Customer Churn Prediction using ANN
📌 Project Overview

This project focuses on predicting customer churn (whether a customer will leave or stay with a company) using an Artificial Neural Network (ANN).
The model is trained on a churn dataset and deployed using Streamlit for interactive visualization and real-time predictions.

The application is divided into three major components:

Model Training

Model Prediction

Web App Deployment using Streamlit

🧠 Problem Statement

Customer churn is a critical business problem where companies aim to identify customers who are likely to stop using their services.
Early prediction of churn helps businesses:

Improve customer retention

Reduce revenue loss

Take proactive actions

⚙️ Project Structure
├── dataset/
│   └── Churn_Modelling.csv
├── saved_model/
│   ├── model.h5
│   └── preprocessor.pkl
├── model_training.ipynb
├── model_prediction.ipynb
├── app.py
└── README.md

🧩 Project Components
1️⃣ Model Training

Data preprocessing using:

Encoding categorical features

Feature scaling

ANN built and trained using TensorFlow / Keras

Model evaluated using accuracy and loss metrics

Trained model and preprocessing pipeline saved for reuse

2️⃣ Model Prediction

Loaded trained ANN model and preprocessor

Accepts new customer data

Predicts whether the customer:

Will Stay

Will Leave (Churn)

3️⃣ Streamlit Web App

Interactive UI for user input

Real-time churn prediction

Clean and simple visualization

Ready for deployment

🛠️ Tech Stack
👨‍💻 Programming Language

Python

📚 Libraries & Frameworks

NumPy

Pandas

Scikit-learn

TensorFlow / Keras

Pickle

🌐 Deployment & Visualization

Streamlit

📊 Dataset

Customer Churn Dataset (Banking churn dataset)

👤 Author:
Kumar Ketan
Btech Graduate | Python | SQL | AI & ML Enthusiast

⭐ Acknowledgement

Thanks to open-source datasets and libraries that made this project possible.


---

.

🚀 Connect With Me

📧 Email: kketan6204@gmail.com 
🔗 LinkedIn: https://www.linkedin.com/in/kumar-ketan-5456b531b/
🐙 GitHub: - https://github.com/Kumar-Ketan
Thanks for checking out this project!