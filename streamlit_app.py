import streamlit as st

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Customer Churn Prediction & Retention ROI")
st.markdown("**End-to-End ML System to Predict, Explain & Prevent Customer Churn**")
st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", "5,630")
col2.metric("Churn Rate", "16.84%")
col3.metric("Annual Loss", "₹47,40,000")
col4.metric("Potential Savings", "₹16,20,000")

st.divider()

st.subheader("📋 Business Problem")
st.markdown("""
An e-commerce platform is losing **₹47,40,000/year** due to **16.84% customer churn rate**.

**This system answers 4 key business questions:**
1. 🔮 **Who** will churn next quarter?
2. 🔍 **Why** are they churning?
3. 💡 **What** retention strategies should we use?
4. 💰 **What is the ROI** of retention campaigns?
""")

st.divider()

st.subheader("🤖 Model Performance")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Best Model", "XGBoost")
col2.metric("AUC Score", "0.9989")
col3.metric("Accuracy", "98.76%")
col4.metric("Cross Val AUC", "0.9871 ✅")

st.divider()

st.subheader("🗺️ Navigation Guide")
col1, col2 = st.columns(2)
with col1:
    st.info("🔮 **Churn Predictor** — Predict churn for any customer + retention strategy")
    st.info("🎯 **Priority Score** — Who to contact first based on revenue × churn risk")
with col2:
    st.info("🔄 **What-If Simulator** — Simulate impact of retention actions in real time")
    st.info("💰 **Budget Optimizer** — Allocate retention budget for maximum ROI")

st.divider()
st.caption("Built with Python | XGBoost | SHAP | Streamlit | GitHub")