import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def app():
    st.title("👥 Customer Segmentation with K-Means")

    np.random.seed(42)
    data = pd.DataFrame({
        "Age": np.random.randint(18, 70, 100),
        "Annual Income (k$)": np.random.randint(15, 120, 100)
    })

    kmeans = KMeans(n_clusters=3, random_state=42)
    data["Cluster"] = kmeans.fit_predict(data)

    st.subheader("Clustered Data")
    st.dataframe(data.head())

    fig, ax = plt.subplots()
    scatter = ax.scatter(data["Age"], data["Annual Income (k$)"], c=data["Cluster"], cmap="viridis")
    ax.set_xlabel("Age")
    ax.set_ylabel("Annual Income (k$)")
    ax.set_title("Customer Segmentation")
    st.pyplot(fig)