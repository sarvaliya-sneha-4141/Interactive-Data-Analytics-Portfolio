import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title("🧹 Data Cleaning Project")

    # Simulate raw data
    np.random.seed(42)
    data = {
        "ID": range(1, 11),
        "Age": [25, 30, np.nan, 45, 29, 34, np.nan, 40, 50, 60],
        "Salary": [50000, 60000, 55000, 65000, 70000, np.nan, 62000, 58000, 72000, 80000],
        "Department": ["HR", "IT", "IT", "Finance", "HR", "Finance", "Finance", "IT", "HR", None]
    }
    df = pd.DataFrame(data)

    st.subheader("Raw Data (with issues)")
    st.dataframe(df)

    # Handle missing values
    df["Age"].fillna(df["Age"].mean(), inplace=True)
    df["Salary"].fillna(df["Salary"].median(), inplace=True)
    df["Department"].fillna("Unknown", inplace=True)

    # Remove duplicates
    df = df.drop_duplicates()

    st.subheader("Cleaned Data")
    st.dataframe(df)
