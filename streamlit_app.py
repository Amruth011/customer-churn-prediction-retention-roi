import streamlit as st
import plotly.graph_objects as go
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
# PROJECT STORY
# ============================================
col1, col2, col3 = st.columns(3)
with col1:
    st.error("""
### 🔴 The Problem
An e-commerce platform was losing
## ₹47,40,000/year
due to **16.84% customer churn**

They had no system to:
- Predict who will leave
- Understand why they leave
- Act before they leave
    """)
with col2:
    st.warning("""
### 🟡 The Approach
Built an **end-to-end ML system**:

1. Analyzed 5,630 customers
2. Engineered 6 new features
3. Tested 4 ML models
4. XGBoost won with **AUC 0.9989**
5. Used SHAP to explain WHY
6. Built live business dashboard
    """)
with col3:
    st.success("""
### 🟢 The Result
Deployed a system that:

- Identifies **937 high risk** customers
- Shows **live SHAP** explanations
- Simulates retention actions
- Optimizes ₹5L budget → **224% ROI**
- Every ₹1 spent returns **₹3.2**
    """)

st.divider()

# ============================================
# KEY METRICS
# ============================================
st.subheader("📊 Business Impact at a Glance")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Customers", "5,630")
col2.metric("Churn Rate", "16.84%")
col3.metric("Annual Loss", "₹47,40,000")
col4.metric("Potential Savings", "₹16,20,000")
col5.metric("ROI", "224%")

st.divider()

# ============================================
# CHARTS
# ============================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Customer Distribution")
    fig_pie = go.Figure(data=[go.Pie(
        labels=['Retained (83.16%)', 'Churned (16.84%)'],
        values=[4682, 948],
        hole=0.4,
        marker_colors=['#44bb44', '#ff4444'],
        textinfo='label+percent'
    )])
    fig_pie.update_layout(
        height=350,
        showlegend=False,
        annotations=[dict(text='5,630\nCustomers', x=0.5, y=0.5,
                         font_size=14, showarrow=False)]
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.subheader("🤖 Model Comparison")
    fig_bar = go.Figure(data=[
        go.Bar(
            x=['Logistic\nRegression', 'Gradient\nBoosting', 'Random\nForest', 'XGBoost\n⭐'],
            y=[0.8687, 0.9428, 0.9988, 0.9989],
            marker_color=['#aaaaaa', '#aaaaaa', '#aaaaaa', '#ff4444'],
            text=['0.8687', '0.9428', '0.9988', '0.9989'],
            textposition='auto'
        )
    ])
    fig_bar.update_layout(
        height=350,
        yaxis_title="AUC Score",
        yaxis=dict(range=[0.8, 1.0]),
        showlegend=False
    )
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# ============================================
# WHAT MAKES THIS UNIQUE
# ============================================
st.subheader("🏆 What Makes This Project Different")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("""
**🧠 Live SHAP Explanations**

Not just predictions — explains
WHY each customer will churn
with real-time SHAP waterfall charts

*Most projects skip this entirely*
    """)
with col2:
    st.info("""
**💰 Business ROI Focus**

Every feature is tied to
real rupee impact:
- Priority Score = Revenue × Risk
- Budget Optimizer = 224% ROI
- What-If = Revenue Protected

*Thinks like a business, not just ML*
    """)
with col3:
    st.info("""
**📅 Cohort Analysis**

Answers WHEN customers churn
not just WHO will churn

Tenure-based risk analysis that
business teams actually use daily

*Unique — no other student project has this*
    """)

st.divider()

# ============================================
# NAVIGATION
# ============================================
st.subheader("🗺️ Explore the Dashboard")

col1, col2, col3 = st.columns(3)
with col1:
    st.success("🔮 **Churn Predictor**\n\nPredict any customer's churn probability with live SHAP explanation + health score + retention strategy")
    st.success("🎯 **Priority Score**\n\nWho to contact first? Combines revenue × churn risk to prioritize retention team's time")
with col2:
    st.warning("🔄 **What-If Simulator**\n\nSimulate impact of every retention action in real time — see revenue protected instantly")
    st.warning("💰 **Budget Optimizer**\n\nAllocate ₹5L retention budget across segments for maximum 224% ROI")
with col3:
    st.error("📅 **Cohort Analysis**\n\nWhen do customers churn? Tenure-based analysis with complaint & cashback breakdowns")
    st.error("🔬 **Model Transparency**\n\nReal confusion matrix, ROC curve & feature importance from actual test data")

st.divider()

# ============================================
# TECH STACK
# ============================================
st.subheader("🛠️ Tech Stack")
col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.info("**Python**\nCore language")
col2.info("**XGBoost**\nML Model")
col3.info("**SHAP**\nExplainability")
col4.info("**Streamlit**\nDashboard")
col5.info("**Plotly**\nCharts")
col6.info("**Pandas**\nData")

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