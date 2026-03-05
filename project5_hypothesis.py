import streamlit as st
import numpy as np
import scipy.stats as stats

def app():
    st.title("📊 Hypothesis Testing Example")

    np.random.seed(42)
    sample1 = np.random.normal(100, 15, 50)
    sample2 = np.random.normal(110, 15, 50)

    t_stat, p_val = stats.ttest_ind(sample1, sample2)

    st.subheader("Two-Sample T-Test")
    st.write(f"T-Statistic: {t_stat:.3f}, P-Value: {p_val:.3f}")

    if p_val < 0.05:
        st.success("Reject Null Hypothesis (Significant difference).")
    else:
        st.warning("Fail to Reject Null Hypothesis.")
