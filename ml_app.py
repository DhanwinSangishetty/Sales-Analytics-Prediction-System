import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st
import joblib
import os

# ----------------------------
# Load or Train Model
# ----------------------------
model_file = "profit_model.pkl"
features = ["Sales", "Quantity", "Discount"]

if os.path.exists(model_file):
    # Load pre-trained model
    model = joblib.load(model_file)
    accuracy = joblib.load("accuracy.pkl")
else:
    # Load data from SQLite
    conn = sqlite3.connect("sales.db")
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()

    # Preprocess
    X = df[features]
    y = (df["Profit"] > 0).astype(int)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Evaluate accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Save model and accuracy
    joblib.dump(model, model_file)
    joblib.dump(accuracy, "accuracy.pkl")

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Sales Profit/Loss Predictor", page_icon="📊", layout="centered")

st.title("📊 Sales Profit/Loss Predictor")
st.write(f"✅ Model trained with accuracy: **{accuracy:.2f}**")

# User Inputs
st.subheader("Enter Sales Data")
sales = st.number_input("Sales Amount ($)", min_value=0.0, step=10.0, value=200.0)
quantity = st.number_input("Quantity", min_value=1, step=1, value=3)
discount = st.number_input("Discount (0 to 1)", min_value=0.0, max_value=1.0, step=0.01, value=0.1)

# Predict button
if st.button("Predict"):
    new_data = pd.DataFrame([[sales, quantity, discount]], columns=features)
    prediction = model.predict(new_data)[0]
    if prediction == 1:
        st.success("💰 Prediction: PROFIT ✅")
    else:
        st.error("📉 Prediction: LOSS ❌")