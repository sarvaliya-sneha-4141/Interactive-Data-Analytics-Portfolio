import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.title("🔍 Exploratory Data Analysis (EDA)")

    # Simulate dataset
    np.random.seed(42)
    df = pd.DataFrame({
        "Age": np.random.randint(20, 60, 100),
        "Salary": np.random.randint(30000, 100000, 100),
        "Department": np.random.choice(["HR", "IT", "Finance", "Marketing"], 100)
    })

    st.subheader("Sample Data")
    st.dataframe(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe())

    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots()
    numeric_df = df.select_dtypes(include=np.number)  # select only numeric columns
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)