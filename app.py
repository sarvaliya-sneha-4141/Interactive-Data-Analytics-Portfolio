import streamlit as st
import importlib
st.write("✅ Streamlit is running")
# Project dictionary
projects = {
    "🧹 Project 1: Data Cleaning": "project1_cleaning",
    "🔍 Project 2: Exploratory Data Analysis (EDA)": "project2_eda",
    "📈 Project 3: Linear Regression": "project3_linear_regression",
    "🤖 Project 4: Logistic Regression": "project4_logistic_regression",
    "📊 Project 5: Hypothesis Testing": "project5_hypothesis",
    "👥 Project 6: Clustering (K-Means)": "project6_clustering",
    "📊 Project 7: Visualization Dashboard": "project7_visualization"
}

# Sidebar navigation
st.sidebar.title("My Data Analyst Portfolio")
choice = st.sidebar.radio("Select a Project", list(projects.keys()))

# Load selected project
module_name = projects[choice]
module = importlib.import_module(module_name)

if hasattr(module, "app"):
    module.app()
else:
    st.error(f"{module_name}.py is missing an app() function!")