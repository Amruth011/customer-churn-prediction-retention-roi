import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="What-If Simulator", page_icon="🔄", layout="wide")

@st.cache_resource
def load_model():
    try:
        return joblib.load('src/best_churn_model.pkl')
    except Exception as e:
        st.error(f"Model loading failed: {e}")
        return None

model = load_model()
if model is None:
    st.stop()

st.title("🔄 What-If Retention Simulator")
st.markdown("*Simulate exactly how each retention action impacts churn probability*")
st.divider()

# ============================================
# CURRENT CUSTOMER PROFILE
# ============================================
st.subheader("👤 Step 1: Set Current Customer Profile")

col1, col2, col3, col4 = st.columns(4)
with col1:
    tenure = st.slider("Tenure (months)", 0, 61, 1)
    satisfaction = st.slider("Satisfaction Score", 1, 5, 1)
    complain = st.selectbox("Complained?", [1, 0],
        format_func=lambda x: "Yes" if x==1 else "No")
with col2:
    cashback = st.slider("Cashback Amount (₹)", 0, 325, 50)
    order_count = st.slider("Order Count", 1, 16, 1)
    day_since = st.slider("Days Since Last Order", 0, 46, 20)
with col3:
    hour_spend = st.slider("Hours on App", 0, 5, 1)
    devices = st.slider("Devices Registered", 1, 6, 2)
    coupon = st.slider("Coupons Used", 0, 16, 0)
with col4:
    annual_revenue = st.number_input("Annual Revenue (₹)", 0, 500000, 5000, 1000)
    city_tier = st.selectbox("City Tier", [1, 2, 3], index=2)
    number_of_address = st.slider("Number of Address", 1, 22, 2)

def make_prediction(ten, sat, comp, cash, coup, orders, days, hours, dev, addr):
    return pd.DataFrame([{
        'Tenure': ten,
        'PreferredLoginDevice': 2,
        'CityTier': city_tier,
        'WarehouseToHome': 30,
        'PreferredPaymentMode': 1,
        'Gender': 1,
        'HourSpendOnApp': hours,
        'NumberOfDeviceRegistered': dev,
        'PreferedOrderCat': 3,
        'SatisfactionScore': sat,
        'MaritalStatus': 2,
        'NumberOfAddress': addr,
        'Complain': comp,
        'OrderAmountHikeFromlastYear': 11,
        'CouponUsed': coup,
        'OrderCount': orders,
        'DaySinceLastOrder': days,
        'CashbackAmount': cash,
        'engagement_score': hours * orders,
        'order_frequency': orders / (days + 1),
        'cashback_per_order': cash / (orders + 1),
        'is_new_customer': 1 if ten < 3 else 0,
        'high_risk': 1 if (comp == 1 and sat <= 2) else 0,
        'device_loyalty': dev
    }])

current_prob = model.predict_proba(
    make_prediction(tenure, satisfaction, complain, cashback,
                   coupon, order_count, day_since, hour_spend,
                   devices, number_of_address))[0][1]

# Current status
st.divider()
st.subheader("📊 Current Churn Probability")
col1, col2, col3 = st.columns(3)
col1.metric("Current Churn Risk", f"{current_prob*100:.1f}%")
col2.metric("Health Score", f"{int((1-current_prob)*100)}/100")
if current_prob >= 0.6:
    col3.metric("Risk Level", "🔴 HIGH RISK")
    st.error(f"🚨 This customer has {current_prob*100:.1f}% chance of churning — immediate action needed!")
elif current_prob >= 0.3:
    col3.metric("Risk Level", "🟡 MEDIUM RISK")
    st.warning(f"⚠️ This customer has {current_prob*100:.1f}% chance of churning — schedule outreach")
else:
    col3.metric("Risk Level", "🟢 LOW RISK")
    st.success(f"✅ This customer has {current_prob*100:.1f}% chance of churning — keep engaging")

st.divider()

# ============================================
# SIMULATE RETENTION ACTIONS
# ============================================
st.subheader("🎮 Step 2: Simulate Retention Actions")
st.markdown("*Adjust ALL factors below to see exact impact on churn probability:*")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("**😊 Experience**")
    new_sat = st.slider("Improve Satisfaction", 1, 5, satisfaction,
        help="What if we improve customer satisfaction?")
    new_complain = st.selectbox("Resolve Complaint?", [complain, 0],
        format_func=lambda x: "Unresolved" if x==1 else "Resolved",
        help="What if we resolve their complaint?")

with col2:
    st.markdown("**💰 Incentives**")
    new_cash = st.slider("Increase Cashback (₹)", 0, 325, cashback,
        help="What if we offer more cashback?")
    new_coupon = st.slider("Offer More Coupons", 0, 16, coupon,
        help="What if we give more coupons?")

with col3:
    st.markdown("**📱 Engagement**")
    new_hours = st.slider("Increase App Usage (hrs)", 0, 5, hour_spend,
        help="What if customer spends more time on app?")
    new_orders = st.slider("Increase Order Count", 1, 16, order_count,
        help="What if customer orders more?")

with col4:
    st.markdown("**⏱️ Recency**")
    new_days = st.slider("Days Since Last Order", 0, 46, day_since,
        help="What if customer ordered more recently?")
    new_tenure = st.slider("Projected Tenure", 0, 61, tenure,
        help="What if customer stays longer?")

# Calculate new probability
new_prob = model.predict_proba(
    make_prediction(new_tenure, new_sat, new_complain, new_cash,
                   new_coupon, new_orders, new_days, new_hours,
                   devices, number_of_address))[0][1]

reduction = current_prob - new_prob
revenue_impact = reduction * annual_revenue

st.divider()

# ============================================
# RESULTS
# ============================================
st.subheader("📊 Step 3: Simulation Results")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Before Intervention", f"{current_prob*100:.1f}%")
col2.metric("After Intervention", f"{new_prob*100:.1f}%",
           delta=f"{-reduction*100:.1f}%")
col3.metric("Risk Reduction", f"{reduction*100:.1f}%")
col4.metric("Revenue Protected", f"₹{revenue_impact:,.0f}")

# Comparison chart
fig = go.Figure(data=[
    go.Bar(
        x=['Before Intervention', 'After Intervention'],
        y=[current_prob * 100, new_prob * 100],
        marker_color=['#ff4444', '#44bb44' if reduction > 0 else '#ff4444'],
        text=[f"{current_prob*100:.1f}%", f"{new_prob*100:.1f}%"],
        textposition='auto',
        width=0.4
    )
])
fig.update_layout(
    title="Churn Probability Before vs After Retention Actions",
    yaxis_title="Churn Probability (%)",
    yaxis=dict(range=[0, 100]),
    height=400
)
st.plotly_chart(fig, use_container_width=True)

if reduction > 0.1:
    st.success(f"✅ Excellent! Retention actions reduced churn by {reduction*100:.1f}% — protecting ₹{revenue_impact:,.0f}!")
elif reduction > 0:
    st.info(f"ℹ️ Small improvement of {reduction*100:.1f}% — try stronger interventions for more impact")
elif reduction == 0:
    st.warning("⚠️ No change — try different interventions")
else:
    st.error("❌ These changes increased churn risk — reconsider your strategy")

st.divider()

# ============================================
# INTERVENTION EFFECTIVENESS
# ============================================
st.subheader("💡 Individual Intervention Impact")
st.markdown("*See which single action has the biggest impact:*")

interventions = {
    "Resolve Complaint": make_prediction(tenure, satisfaction, 0, cashback, coupon, order_count, day_since, hour_spend, devices, number_of_address),
    "Improve Satisfaction (→5)": make_prediction(tenure, 5, complain, cashback, coupon, order_count, day_since, hour_spend, devices, number_of_address),
    "Increase Cashback (→₹300)": make_prediction(tenure, satisfaction, complain, 300, coupon, order_count, day_since, hour_spend, devices, number_of_address),
    "Increase Orders (→5)": make_prediction(tenure, satisfaction, complain, cashback, coupon, 5, day_since, hour_spend, devices, number_of_address),
    "Recent Order (→5 days)": make_prediction(tenure, satisfaction, complain, cashback, coupon, order_count, 5, hour_spend, devices, number_of_address),
    "More App Usage (→4hrs)": make_prediction(tenure, satisfaction, complain, cashback, 5, order_count, day_since, 4, devices, number_of_address),
}

impact_data = []
for action, df in interventions.items():
    new_p = model.predict_proba(df)[0][1]
    impact = (current_prob - new_p) * 100
    impact_data.append({'Action': action, 'Churn Reduction': round(impact, 1)})

impact_df = pd.DataFrame(impact_data).sort_values('Churn Reduction', ascending=False)

fig2 = go.Figure(go.Bar(
    x=impact_df['Churn Reduction'],
    y=impact_df['Action'],
    orientation='h',
    marker_color=['#44bb44' if v > 0 else '#ff4444' for v in impact_df['Churn Reduction']],
    text=[f"{v:+.1f}%" for v in impact_df['Churn Reduction']],
    textposition='outside'
))
fig2.update_layout(
    title="Which Retention Action Has Biggest Impact?",
    xaxis_title="Churn Reduction (%)",
    height=400
)
st.plotly_chart(fig2, use_container_width=True)

best_action = impact_df.iloc[0]
st.success(f"🏆 Most effective action: **{best_action['Action']}** — reduces churn by {best_action['Churn Reduction']:.1f}%")

st.divider()
st.markdown("""
<div style='text-align: center; color: gray; padding: 10px;'>
    Built by <b>Amruth</b> | Python • XGBoost • SHAP • Streamlit | 
    <a href='https://github.com/Amruth011/customer-churn-prediction-retention-roi' target='_blank'>GitHub</a>
</div>
""", unsafe_allow_html=True)