import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def app():
    st.title("📈 Linear Regression: Sales vs. Advertising Spend")

    np.random.seed(42)
    ad_spend = np.random.randint(1000, 5000, 50)
    sales = 50 + 5 * ad_spend + np.random.normal(0, 2000, 50)
    df = pd.DataFrame({"Ad Spend ($)": ad_spend, "Sales ($)": sales})

    X = df[["Ad Spend ($)"]]
    y = df["Sales ($)"]
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)

    st.subheader("Simulated Data")
    st.dataframe(df.head())

    fig, ax = plt.subplots()
    ax.scatter(ad_spend, sales, label="Actual")
    ax.plot(ad_spend, predictions, color="red", label="Regression Line")
    ax.set_xlabel("Ad Spend ($)")
    ax.set_ylabel("Sales ($)")
    ax.legend()
    st.pyplot(fig)

    st.subheader("Model Performance")
    st.write(f"R² Score: {model.score(X, y):.3f}")
    st.write(f"Equation: Sales = {model.intercept_:.2f} + {model.coef_[0]:.2f} * Ad Spend")