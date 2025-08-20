import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data/SampleSuperstore.csv", encoding="latin1")

# Binary target: 1 = profitable, 0 = not profitable
df["HighProfit"] = (df["Profit"] > 0).astype(int)

# Features and target
features = ["Sales", "Quantity", "Discount"]
X = df[features]   
y = df["HighProfit"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("✅ Model Accuracy:", acc)

# Example prediction
new_data = pd.DataFrame([[200, 3, 0.35]], columns=features)

pred = model.predict(new_data)
print("Prediction (1=Profit, 0=Loss):", pred)