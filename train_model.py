import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Load the dataset
df = pd.read_csv("data/train.csv")  # Make sure this file exists

# Split features and target
X = df.drop(columns=["Reached.on.Time_Y.N"])
y = df["Reached.on.Time_Y.N"]

# One-hot encode categorical features
X = pd.get_dummies(X)

# Train/test split
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")
print("✅ Model trained and saved to model/model.pkl")
