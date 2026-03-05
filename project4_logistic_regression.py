import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.title("🤖 Logistic Regression: Customer Churn Prediction")

    np.random.seed(42)
    df = pd.DataFrame({
        "Age": np.random.randint(20, 70, 200),
        "Monthly_Spend": np.random.randint(20, 200, 200),
        "Churn": np.random.choice([0, 1], size=200)
    })

    X = df[["Age", "Monthly_Spend"]]
    y = df["Churn"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    acc = accuracy_score(y_test, y_pred)
    st.write(f"Model Accuracy: {acc:.2f}")

    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig)