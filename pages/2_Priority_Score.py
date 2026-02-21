import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Priority Score", page_icon="🎯", layout="wide")

st.title("🎯 Customer Priority Score")
st.markdown("*Who should your retention team call FIRST?*")
st.markdown("**Formula: Priority Score = Annual Revenue × Churn Probability**")
st.divider()

st.subheader("📊 How Priority Score Works")
example_data = pd.DataFrame({
    'Customer': ['Customer A', 'Customer B', 'Customer C'],
    'Annual Revenue (₹)': [50000, 5000, 1000],
    'Churn Probability': ['90%', '95%', '85%'],
    'Priority Score': [45000, 4750, 850],
    'Action': ['Call Today', 'Call This Week', 'Email Campaign']
})
st.table(example_data.set_index('Customer'))
st.warning("Customer B has higher churn probability but Customer A should be contacted FIRST — revenue at risk is 10x higher!")
st.divider()

st.subheader("🔢 Calculate Your Customer Priority Score")
col1, col2 = st.columns(2)
with col1:
    rev = st.number_input("Customer Annual Revenue (₹)", 0, 500000, 5000, 1000)
with col2:
    churn_prob = st.slider("Churn Probability (%)", 0, 100, 50)

priority_score = rev * (churn_prob / 100)

if priority_score >= 20000:
    label = "🔴 PRIORITY 1 — Contact Immediately"
    color = "red"
    reason = "High value customer with high churn risk — every day of delay costs money"
elif priority_score >= 5000:
    label = "🟡 PRIORITY 2 — Contact This Week"
    color = "orange"
    reason = "Medium priority — schedule retention outreach within 7 days"
else:
    label = "🟢 PRIORITY 3 — Standard Follow-up"
    color = "green"
    reason = "Low urgency — include in regular engagement campaigns"

col1, col2, col3 = st.columns(3)
col1.metric("Annual Revenue", f"₹{rev:,}")
col2.metric("Churn Probability", f"{churn_prob}%")
col3.metric("Priority Score", f"{priority_score:,.0f}")

st.divider()
st.markdown(f"<h2 style='color:{color}'>{label}</h2>", unsafe_allow_html=True)
st.info(reason)
st.divider()

# Plotly bar chart comparing 3 customers
st.subheader("📈 Priority Score Comparison")
fig = go.Figure(data=[
    go.Bar(
        x=['Customer A\n₹50,000 | 90%', 'Customer B\n₹5,000 | 95%', 'Customer C\n₹1,000 | 85%'],
        y=[45000, 4750, 850],
        marker_color=['#ff4444', '#ffaa00', '#44bb44'],
        text=[45000, 4750, 850],
        textposition='auto'
    )
])
fig.update_layout(
    title="Priority Score — Who to Contact First",
    yaxis_title="Priority Score",
    height=400
)
st.plotly_chart(fig, use_container_width=True)
st.caption("Higher bar = Contact first regardless of churn probability")

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