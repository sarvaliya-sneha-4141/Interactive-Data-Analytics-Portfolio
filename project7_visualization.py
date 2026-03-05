import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.title("📊 Interactive Visualization Dashboard")

    np.random.seed(42)
    df = pd.DataFrame({
        "Category": np.random.choice(["A", "B", "C"], 100),
        "Value": np.random.randint(10, 100, 100),
        "Score": np.random.randint(1, 50, 100)
    })

    st.subheader("Data Sample")
    st.dataframe(df.head())

    choice = st.selectbox(
        "Choose chart type",
        ["Bar Chart", "Line Chart", "Histogram", "Pie Chart", "Scatter Plot", "Box Plot", "Area Chart"]
    )

    # BAR CHART
    if choice == "Bar Chart":
        st.subheader("Average Value by Category")
        st.bar_chart(df.groupby("Category")["Value"].mean())

    # LINE CHART
    elif choice == "Line Chart":
        st.subheader("Line Chart of Value")
        st.line_chart(df["Value"])

    # HISTOGRAM
    elif choice == "Histogram":
        st.subheader("Value Distribution")
        fig, ax = plt.subplots()
        ax.hist(df["Value"], bins=10, color="skyblue")
        st.pyplot(fig)

    # PIE CHART
    elif choice == "Pie Chart":
        st.subheader("Category Distribution")
        fig, ax = plt.subplots()
        counts = df["Category"].value_counts()
        ax.pie(counts, labels=counts.index, autopct="%1.1f%%")
        ax.set_title("Category Share")
        st.pyplot(fig)

    # SCATTER PLOT
    elif choice == "Scatter Plot":
        st.subheader("Value vs Score")
        fig, ax = plt.subplots()
        ax.scatter(df["Value"], df["Score"])
        ax.set_xlabel("Value")
        ax.set_ylabel("Score")
        ax.set_title("Scatter Plot")
        st.pyplot(fig)

    # BOX PLOT
    elif choice == "Box Plot":
        st.subheader("Box Plot of Value by Category")
        fig, ax = plt.subplots()
        df.boxplot(column="Value", by="Category", ax=ax)
        st.pyplot(fig)

    # AREA CHART
    elif choice == "Area Chart":
        st.subheader("Area Chart")
        st.area_chart(df[["Value", "Score"]])