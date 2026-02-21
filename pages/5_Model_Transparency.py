import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Model Transparency", page_icon="🔬", layout="wide")

st.title("🔬 Model Transparency & Performance")
st.markdown("*How does the model work? How accurate is it?*")
st.divider()

# Model comparison
st.subheader("🤖 Model Comparison")
model_df = pd.DataFrame({
    'Model': ['Logistic Regression', 'Gradient Boosting', 'Random Forest', 'XGBoost ⭐'],
    'AUC Score': [0.8687, 0.9428, 0.9988, 0.9989],
    'Accuracy': [87.03, 91.03, 98.31, 98.76]
})

fig = go.Figure(data=[
    go.Bar(
        x=model_df['Model'],
        y=model_df['AUC Score'],
        marker_color=['#aaaaaa', '#aaaaaa', '#aaaaaa', '#ff4444'],
        text=[f"{v:.4f}" for v in model_df['AUC Score']],
        textposition='auto'
    )
])
fig.update_layout(
    title="AUC Score Comparison — XGBoost Wins!",
    yaxis_title="AUC Score",
    yaxis=dict(range=[0.8, 1.0]),
    height=400
)
st.plotly_chart(fig, use_container_width=True)
st.table(model_df.set_index('Model'))
st.divider()

# Confusion matrix
st.subheader("📊 Confusion Matrix — XGBoost")
st.markdown("Shows how many customers were correctly predicted:")

col1, col2 = st.columns(2)
with col1:
    confusion_data = pd.DataFrame({
        '': ['Actual: Not Churned', 'Actual: Churned'],
        'Predicted: Not Churned': [932, 10],
        'Predicted: Churned': [4, 180]
    })
    st.table(confusion_data.set_index(''))

with col2:
    st.metric("True Negatives (Correct)", "932")
    st.metric("True Positives (Caught Churners)", "180")
    st.metric("False Positives (Wrong Alarm)", "4")
    st.metric("False Negatives (Missed Churners)", "10")
    st.warning("10 missed churners = ₹50,000 revenue at risk")

st.divider()

# Feature importance
st.subheader("🔍 Top 10 Features Driving Churn")
st.markdown("Based on SHAP values from XGBoost model:")

features = pd.DataFrame({
    'Feature': [
        'Tenure', 'Complain', 'NumberOfAddress',
        'CashbackAmount', 'order_frequency',
        'MaritalStatus', 'WarehouseToHome',
        'cashback_per_order', 'CityTier', 'SatisfactionScore'
    ],
    'Importance': [0.35, 0.25, 0.12, 0.10, 0.08, 0.04, 0.03, 0.01, 0.01, 0.01]
})

fig2 = px.bar(
    features,
    x='Importance',
    y='Feature',
    orientation='h',
    color='Importance',
    color_continuous_scale='Reds',
    title='Feature Importance (SHAP Values)'
)
fig2.update_layout(height=450, yaxis={'categoryorder': 'total ascending'})
st.plotly_chart(fig2, use_container_width=True)
st.divider()

# Cross validation
st.subheader("✅ Cross Validation Results")
st.markdown("Proves model is stable — not just lucky on one test:")

cv_df = pd.DataFrame({
    'Fold': ['Fold 1', 'Fold 2', 'Fold 3', 'Fold 4', 'Fold 5'],
    'AUC Score': [0.9930, 0.9826, 0.9897, 0.9875, 0.9828]
})

fig3 = go.Figure(data=[
    go.Scatter(
        x=cv_df['Fold'],
        y=cv_df['AUC Score'],
        mode='lines+markers+text',
        text=[f"{v:.4f}" for v in cv_df['AUC Score']],
        textposition='top center',
        line=dict(color='#ff4444', width=3),
        marker=dict(size=10)
    )
])
fig3.update_layout(
    title="Cross Validation AUC Scores — Consistent Performance!",
    yaxis=dict(range=[0.97, 1.0]),
    height=350
)
st.plotly_chart(fig3, use_container_width=True)

col1, col2, col3 = st.columns(3)
col1.metric("Mean AUC", "0.9871")
col2.metric("Std Deviation", "0.0040")
col3.metric("Stability", "✅ Excellent")
st.divider()

# Key insights
st.subheader("💡 Key Model Insights")
st.markdown("""
| Insight | Finding |
|---|---|
| #1 Churn Driver | **Tenure** — new customers (< 3 months) churn most |
| #2 Churn Driver | **Complaints** — complained customers churn 3x more |
| #3 Churn Driver | **Number of Addresses** — shopping across platforms |
| Best Retention Action | Resolve complaints immediately |
| Highest Risk Segment | New customers with complaints |
| Model Confidence | 98.76% accuracy on test data |
""")

# ============================================
# FOOTER
# ============================================
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; padding: 10px;'>
    Built by <b>Amruth</b> | Python • XGBoost • SHAP • Streamlit | 
    <a href='https://github.com/Amruth011/customer-churn-prediction-retention-roi' target='_blank'>GitHub</a>
</div>
""", unsafe_allow_html=True)