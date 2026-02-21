import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Cohort Analysis", page_icon="📅", layout="wide")

st.title("📅 Cohort Analysis")
st.markdown("*When do customers churn? Which tenure group is most at risk?*")
st.divider()

# ============================================
# LOAD DATA
# ============================================
@st.cache_data
def load_data():
    try:
        df = pd.read_excel('data/raw/E Commerce Dataset.xlsx', sheet_name='E Comm')
        return df
    except Exception as e:
        st.error(f"Data loading failed: {e}")
        return None

with st.spinner("Loading dataset..."):
    df = load_data()

if df is None:
    st.stop()

# ============================================
# FEATURE ENGINEERING
# ============================================
df['Churn'] = df['Churn'].astype(int)

df['TenureGroup'] = pd.cut(
    df['Tenure'],
    bins=[-1, 3, 6, 12, 24, 100],
    labels=['0-3 months', '3-6 months', '6-12 months', '12-24 months', '24+ months']
)

# ============================================
# KEY METRICS
# ============================================
st.subheader("📊 Churn Rate by Tenure Group")

cohort = df.groupby('TenureGroup').agg(
    Total=('Churn', 'count'),
    Churned=('Churn', 'sum')
).reset_index()
cohort['Churn Rate %'] = (cohort['Churned'] / cohort['Total'] * 100).round(2)
cohort['Retained'] = cohort['Total'] - cohort['Churned']

# Bar chart
fig1 = go.Figure(data=[
    go.Bar(
        x=cohort['TenureGroup'].astype(str),
        y=cohort['Churn Rate %'],
        marker_color=['#ff4444' if x > 20 else '#ffaa00' if x > 10 else '#44bb44'
                     for x in cohort['Churn Rate %']],
        text=[f"{v:.1f}%" for v in cohort['Churn Rate %']],
        textposition='auto'
    )
])
fig1.update_layout(
    title="Churn Rate by Customer Tenure Group",
    xaxis_title="Tenure Group",
    yaxis_title="Churn Rate (%)",
    height=400
)
st.plotly_chart(fig1, use_container_width=True)

# Table
st.subheader("📋 Cohort Summary Table")
display_cohort = cohort.copy()
display_cohort.columns = ['Tenure Group', 'Total Customers', 'Churned', 'Churn Rate %', 'Retained']
st.table(display_cohort.set_index('Tenure Group'))

st.divider()

# ============================================
# CHURN BY COMPLAINT & TENURE
# ============================================
st.subheader("😤 Complaint Impact by Tenure Group")

complaint_cohort = df.groupby(['TenureGroup', 'Complain'])['Churn'].mean().reset_index()
complaint_cohort['Churn Rate %'] = (complaint_cohort['Churn'] * 100).round(2)
complaint_cohort['Complained'] = complaint_cohort['Complain'].map({0: 'No Complaint', 1: 'Complained'})

fig2 = px.bar(
    complaint_cohort,
    x='TenureGroup',
    y='Churn Rate %',
    color='Complained',
    barmode='group',
    color_discrete_map={'No Complaint': '#44bb44', 'Complained': '#ff4444'},
    title="Churn Rate by Tenure Group & Complaint Status"
)
fig2.update_layout(height=400)
st.plotly_chart(fig2, use_container_width=True)
st.info("💡 Complained customers churn significantly more across ALL tenure groups!")

st.divider()

# ============================================
# SATISFACTION BY TENURE
# ============================================
st.subheader("😊 Satisfaction Score by Tenure Group")

sat_cohort = df.groupby('TenureGroup').agg(
    Avg_Satisfaction=('SatisfactionScore', 'mean'),
    Churn_Rate=('Churn', 'mean')
).reset_index()
sat_cohort['Avg_Satisfaction'] = sat_cohort['Avg_Satisfaction'].round(2)
sat_cohort['Churn_Rate %'] = (sat_cohort['Churn_Rate'] * 100).round(2)

fig3 = go.Figure()
fig3.add_trace(go.Bar(
    x=sat_cohort['TenureGroup'].astype(str),
    y=sat_cohort['Avg_Satisfaction'],
    name='Avg Satisfaction Score',
    marker_color='#4444ff',
    yaxis='y'
))
fig3.add_trace(go.Scatter(
    x=sat_cohort['TenureGroup'].astype(str),
    y=sat_cohort['Churn_Rate %'],
    name='Churn Rate %',
    mode='lines+markers',
    line=dict(color='#ff4444', width=3),
    marker=dict(size=10),
    yaxis='y2'
))
fig3.update_layout(
    title="Satisfaction Score vs Churn Rate by Tenure",
    yaxis=dict(title='Avg Satisfaction Score', range=[0, 5]),
    yaxis2=dict(title='Churn Rate %', overlaying='y', side='right', range=[0, 50]),
    height=400,
    legend=dict(x=0.7, y=1.1)
)
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ============================================
# CASHBACK BY TENURE
# ============================================
st.subheader("💰 Cashback Amount by Tenure Group")

cash_cohort = df.groupby(['TenureGroup', 'Churn']).agg(
    Avg_Cashback=('CashbackAmount', 'mean')
).reset_index()
cash_cohort['Status'] = cash_cohort['Churn'].map({0: 'Retained', 1: 'Churned'})
cash_cohort['Avg_Cashback'] = cash_cohort['Avg_Cashback'].round(2)

fig4 = px.bar(
    cash_cohort,
    x='TenureGroup',
    y='Avg_Cashback',
    color='Status',
    barmode='group',
    color_discrete_map={'Retained': '#44bb44', 'Churned': '#ff4444'},
    title="Average Cashback — Churned vs Retained by Tenure Group"
)
fig4.update_layout(height=400)
st.plotly_chart(fig4, use_container_width=True)
st.info("💡 Retained customers consistently receive higher cashback across all tenure groups!")

st.divider()

# ============================================
# CITY TIER ANALYSIS
# ============================================
st.subheader("🏙️ Churn Rate by City Tier")

city_cohort = df.groupby('CityTier').agg(
    Total=('Churn', 'count'),
    Churned=('Churn', 'sum')
).reset_index()
city_cohort['Churn Rate %'] = (city_cohort['Churned'] / city_cohort['Total'] * 100).round(2)

fig5 = go.Figure(data=[
    go.Bar(
        x=[f"Tier {t}" for t in city_cohort['CityTier']],
        y=city_cohort['Churn Rate %'],
        marker_color=['#ff4444' if x > 20 else '#ffaa00' if x > 10 else '#44bb44'
                     for x in city_cohort['Churn Rate %']],
        text=[f"{v:.1f}%" for v in city_cohort['Churn Rate %']],
        textposition='auto'
    )
])
fig5.update_layout(
    title="Churn Rate by City Tier",
    xaxis_title="City Tier",
    yaxis_title="Churn Rate (%)",
    height=350
)
st.plotly_chart(fig5, use_container_width=True)

st.divider()

# ============================================
# KEY INSIGHTS
# ============================================
st.subheader("💡 Key Cohort Insights")

highest_churn = cohort.loc[cohort['Churn Rate %'].idxmax()]
lowest_churn = cohort.loc[cohort['Churn Rate %'].idxmin()]

col1, col2, col3 = st.columns(3)
col1.error(f"🔴 Highest Risk Group\n\n**{highest_churn['TenureGroup']}**\n\n{highest_churn['Churn Rate %']:.1f}% churn rate")
col2.success(f"🟢 Lowest Risk Group\n\n**{lowest_churn['TenureGroup']}**\n\n{lowest_churn['Churn Rate %']:.1f}% churn rate")
col3.info(f"📊 Overall Churn Rate\n\n**16.84%**\n\nAcross all 5,630 customers")

st.divider()
st.markdown("""
<div style='text-align: center; color: gray; padding: 10px;'>
    Built by <b>Amruth</b> | Python • XGBoost • SHAP • Streamlit | 
    <a href='https://github.com/Amruth011/customer-churn-prediction-retention-roi' target='_blank'>GitHub</a>
</div>
""", unsafe_allow_html=True)