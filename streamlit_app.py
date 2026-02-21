import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🛒",
    layout="wide"
)

# ============================================
# HEADER
# ============================================
st.title("🛒 Customer Churn Prediction & Retention ROI")
st.markdown("**End-to-End ML System to Predict, Explain & Prevent Customer Churn**")
st.divider()

# ============================================
# KEY METRICS
# ============================================
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", "5,630")
col2.metric("Churn Rate", "16.84%")
col3.metric("Annual Loss", "₹47,40,000")
col4.metric("Potential Savings", "₹16,20,000")

st.divider()

# ============================================
# CHARTS ROW
# ============================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Customer Churn Distribution")
    fig_pie = go.Figure(data=[go.Pie(
        labels=['Retained', 'Churned'],
        values=[4682, 948],
        hole=0.4,
        marker_colors=['#44bb44', '#ff4444'],
        textinfo='label+percent'
    )])
    fig_pie.update_layout(
        height=350,
        showlegend=True,
        annotations=[dict(text='5,630', x=0.5, y=0.5, font_size=20, showarrow=False)]
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.subheader("💰 Revenue Impact Analysis")
    fig_bar = go.Figure(data=[
        go.Bar(
            x=['Annual Loss', 'Campaign Cost', 'Revenue Saved', 'Net Profit'],
            y=[4740000, 475500, 1620000, 1144500],
            marker_color=['#ff4444', '#ffaa00', '#44bb44', '#4444ff'],
            text=['₹47.4L', '₹4.75L', '₹16.2L', '₹11.4L'],
            textposition='auto'
        )
    ])
    fig_bar.update_layout(
        height=350,
        yaxis_title="Amount (₹)",
        showlegend=False
    )
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# ============================================
# BUSINESS PROBLEM
# ============================================
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

# ============================================
# MODEL PERFORMANCE
# ============================================
st.subheader("🤖 Model Performance")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Best Model", "XGBoost")
col2.metric("AUC Score", "0.9989")
col3.metric("Accuracy", "98.76%")
col4.metric("Cross Val AUC", "0.9871 ✅")

st.divider()

# ============================================
# CHURN DRIVERS
# ============================================
st.subheader("🔍 Top Churn Drivers")
col1, col2, col3 = st.columns(3)
with col1:
    st.error("📅 **#1 — New Customers**\n\nTenure < 3 months customers churn 3x more than loyal customers")
with col2:
    st.error("😤 **#2 — Complaints**\n\nCustomers who complained churn 3x more than satisfied customers")
with col3:
    st.warning("💸 **#3 — Low Cashback**\n\nCustomers with low cashback have significantly higher churn risk")

st.divider()

# ============================================
# NAVIGATION GUIDE
# ============================================
st.subheader("🗺️ Navigation Guide")
col1, col2 = st.columns(2)
with col1:
    st.info("🔮 **Churn Predictor** — Predict churn for any customer + retention strategy + health score")
    st.info("🎯 **Priority Score** — Who to contact first based on revenue × churn risk")
with col2:
    st.info("🔄 **What-If Simulator** — Simulate impact of retention actions in real time")
    st.info("💰 **Budget Optimizer** — Allocate retention budget for maximum ROI")

st.info("🔬 **Model Transparency** — How the model works, accuracy metrics & feature importance")

st.divider()

# ============================================
# FOOTER
# ============================================
st.markdown("""
<div style='text-align: center; color: gray; padding: 10px;'>
    Built by <b>Amruth</b> | Python • XGBoost • SHAP • Streamlit | 
    <a href='https://github.com/Amruth011/customer-churn-prediction-retention-roi' target='_blank'>GitHub</a>
</div>
""", unsafe_allow_html=True)