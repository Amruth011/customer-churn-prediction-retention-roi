import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Churn Predictor", page_icon="🔮", layout="wide")

# ============================================
# LOAD MODEL
# ============================================
@st.cache_resource
def load_model():
    try:
        return joblib.load('src/best_churn_model.pkl')
    except Exception as e:
        st.error(f"Model loading failed: {e}")
        return None

with st.spinner("Loading AI Model..."):
    model = load_model()

if model is None:
    st.stop()

st.title("🔮 Churn Predictor")
st.markdown("**Predict which customers will churn & get personalized retention strategy**")
st.divider()

# ============================================
# SIDEBAR INPUTS
# ============================================
st.sidebar.header("📋 Customer Details")

if st.sidebar.button("📋 Load Sample HIGH RISK Customer"):
    st.session_state['sample'] = True
    st.rerun()

if st.sidebar.button("🔄 Reset to Default"):
    st.session_state['sample'] = False
    st.rerun()

sample = st.session_state.get('sample', False)

if sample:
    st.sidebar.success("✅ HIGH RISK Customer Loaded!")

tenure = st.sidebar.slider("Tenure (months)", 0, 61, 0 if sample else 10)
city_tier = st.sidebar.selectbox("City Tier", [1, 2, 3], index=2 if sample else 0)
warehouse_to_home = st.sidebar.slider("Warehouse to Home (km)", 5, 127, 30 if sample else 15)
hour_spend_on_app = st.sidebar.slider("Hours on App", 0, 5, 1 if sample else 3)
devices_registered = st.sidebar.slider("Devices Registered", 1, 6, 2 if sample else 3)
satisfaction_score = st.sidebar.slider("Satisfaction Score", 1, 5, 1 if sample else 3)
number_of_address = st.sidebar.slider("Number of Address", 1, 22, 2 if sample else 3)
complain = st.sidebar.selectbox("Complained?", [0, 1],
    index=1 if sample else 0,
    format_func=lambda x: "Yes" if x==1 else "No")
order_amount_hike = st.sidebar.slider("Order Amount Hike %", 11, 26, 11 if sample else 15)
coupon_used = st.sidebar.slider("Coupons Used", 0, 16, 0 if sample else 2)
order_count = st.sidebar.slider("Order Count", 1, 16, 1 if sample else 3)
day_since_last_order = st.sidebar.slider("Days Since Last Order", 0, 46, 20 if sample else 5)
cashback_amount = st.sidebar.slider("Cashback Amount (₹)", 0, 325, 50 if sample else 150)
preferred_login = st.sidebar.selectbox("Login Device", [0, 1, 2],
    format_func=lambda x: ["Mobile Phone", "Computer", "Phone"][x])
preferred_payment = st.sidebar.selectbox("Payment Mode", [0,1,2,3,4,5,6],
    format_func=lambda x: ["CC","COD","Debit Card","E wallet","UPI","Cash on Delivery","Credit Card"][x])
gender = st.sidebar.selectbox("Gender", [0, 1],
    format_func=lambda x: "Female" if x==0 else "Male")
marital_status = st.sidebar.selectbox("Marital Status", [0, 1, 2],
    format_func=lambda x: ["Divorced", "Married", "Single"][x])
order_cat = st.sidebar.selectbox("Preferred Order Category", [0,1,2,3,4,5],
    format_func=lambda x: ["Fashion","Grocery","Laptop","Mobile","Mobile Phone","Others"][x])
annual_revenue = st.sidebar.number_input("Customer Annual Revenue (₹)", 0, 500000, 5000, 1000)
predict_btn = st.sidebar.button("🔮 Predict Churn", type="primary")

# ============================================
# FEATURE ENGINEERING
# ============================================
def get_input():
    return pd.DataFrame([{
        'Tenure': tenure,
        'PreferredLoginDevice': preferred_login,
        'CityTier': city_tier,
        'WarehouseToHome': warehouse_to_home,
        'PreferredPaymentMode': preferred_payment,
        'Gender': gender,
        'HourSpendOnApp': hour_spend_on_app,
        'NumberOfDeviceRegistered': devices_registered,
        'PreferedOrderCat': order_cat,
        'SatisfactionScore': satisfaction_score,
        'MaritalStatus': marital_status,
        'NumberOfAddress': number_of_address,
        'Complain': complain,
        'OrderAmountHikeFromlastYear': order_amount_hike,
        'CouponUsed': coupon_used,
        'OrderCount': order_count,
        'DaySinceLastOrder': day_since_last_order,
        'CashbackAmount': cashback_amount,
        'engagement_score': hour_spend_on_app * order_count,
        'order_frequency': order_count / (day_since_last_order + 1),
        'cashback_per_order': cashback_amount / (order_count + 1),
        'is_new_customer': 1 if tenure < 3 else 0,
        'high_risk': 1 if (complain == 1 and satisfaction_score <= 2) else 0,
        'device_loyalty': devices_registered
    }])

# ============================================
# GAUGE CHART
# ============================================
def create_gauge(prob):
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=prob * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Churn Risk %", 'font': {'size': 24}},
        delta={'reference': 50, 'increasing': {'color': "red"}, 'decreasing': {'color': "green"}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1},
            'bar': {'color': "darkred" if prob >= 0.6 else "orange" if prob >= 0.3 else "green"},
            'steps': [
                {'range': [0, 30], 'color': '#90EE90'},
                {'range': [30, 60], 'color': '#FFD700'},
                {'range': [60, 100], 'color': '#FFB6C1'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': prob * 100
            }
        }
    ))
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=40, b=20))
    return fig

# ============================================
# TOP 3 CHURN REASONS
# ============================================
def get_churn_reasons():
    reasons = []
    if tenure < 3:
        reasons.append(("📅 New Customer", "Tenure < 3 months — new customers have highest churn risk", "HIGH"))
    if complain == 1:
        reasons.append(("😤 Active Complaint", "Unresolved complaint — complained customers churn 3x more", "HIGH"))
    if satisfaction_score <= 2:
        reasons.append(("😞 Low Satisfaction", f"Satisfaction score {satisfaction_score}/5 — very dissatisfied customer", "HIGH"))
    if cashback_amount < 100:
        reasons.append(("💸 Low Cashback", f"Only ₹{cashback_amount} cashback — low incentive to stay", "MEDIUM"))
    if day_since_last_order > 20:
        reasons.append(("🕐 Inactive", f"No order in {day_since_last_order} days — losing engagement", "MEDIUM"))
    if order_count <= 1:
        reasons.append(("📦 Low Orders", f"Only {order_count} order — not a regular customer", "MEDIUM"))
    if number_of_address > 5:
        reasons.append(("📍 Multiple Addresses", f"{number_of_address} addresses — possibly shopping across platforms", "LOW"))
    if hour_spend_on_app <= 1:
        reasons.append(("📱 Low App Usage", f"Only {hour_spend_on_app}h on app — low engagement", "LOW"))
    if not reasons:
        reasons.append(("✅ No Major Risk Factors", "This customer shows healthy engagement patterns", "LOW"))
    return reasons[:3]

# ============================================
# HEALTH SCORE
# ============================================
def get_health_score(prob):
    return int((1 - prob) * 100)

# ============================================
# MAIN PREDICTION
# ============================================
if predict_btn:
    with st.spinner("Analyzing customer profile..."):
        prob = model.predict_proba(get_input())[0][1]
        health_score = get_health_score(prob)
        reasons = get_churn_reasons()

    if prob >= 0.6:
        risk = "🔴 HIGH RISK"
        color = "red"
        strategy = [
            "📞 Immediate personal outreach within 24 hours",
            "🎟️ Offer 20-30% discount coupon",
            "🚚 Free delivery for next 3 months",
            "⭐ Assign priority customer support agent"
        ]
    elif prob >= 0.3:
        risk = "🟡 MEDIUM RISK"
        color = "orange"
        strategy = [
            "🎁 Send loyalty reward points",
            "🛍️ Personalized product recommendations",
            "⚡ Flash sale early access",
            "💰 Cashback on next 3 orders"
        ]
    else:
        risk = "🟢 LOW RISK"
        color = "green"
        strategy = [
            "📧 Regular engagement emails",
            "👥 Invite to referral program",
            "🎉 Seasonal offers and discounts"
        ]

    campaign_cost = 500
    revenue_saved = annual_revenue * 0.30
    roi = ((revenue_saved - campaign_cost) / campaign_cost) * 100

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Churn Probability", f"{prob*100:.1f}%")
    col2.metric("Risk Segment", risk)
    col3.metric("Health Score", f"{health_score}/100")
    col4.metric("ROI if Retained", f"{roi:.0f}%")

    st.divider()

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("📊 Churn Risk Gauge")
        st.plotly_chart(create_gauge(prob), use_container_width=True)
    with col2:
        st.subheader("🔍 Top 3 Churn Reasons")
        for title, desc, level in reasons:
            if level == "HIGH":
                st.error(f"**{title}**\n\n{desc}")
            elif level == "MEDIUM":
                st.warning(f"**{title}**\n\n{desc}")
            else:
                st.info(f"**{title}**\n\n{desc}")

    st.divider()

    st.subheader("💚 Customer Health Score")
    health_color = "green" if health_score >= 70 else "orange" if health_score >= 40 else "red"
    st.markdown(
        f"<h2 style='color:{health_color}'>Health Score: {health_score}/100</h2>",
        unsafe_allow_html=True)
    st.progress(health_score / 100)
    if health_score >= 70:
        st.success("✅ Healthy customer — low churn risk")
    elif health_score >= 40:
        st.warning("⚠️ At risk customer — needs attention")
    else:
        st.error("🚨 Critical customer — immediate action required")

    st.divider()

    st.subheader("💡 Recommended Retention Strategy")
    for action in strategy:
        st.markdown(f"- {action}")

    st.divider()

    st.subheader("💰 ROI Calculator")
    col4, col5, col6 = st.columns(3)
    col4.metric("Campaign Cost", f"₹{campaign_cost:,}")
    col5.metric("Revenue Saved", f"₹{revenue_saved:,.0f}")
    col6.metric("ROI", f"{roi:.0f}%")

else:
    st.info("👈 Fill in customer details in the sidebar and click **Predict Churn**")
    if sample:
        st.success("✅ Sample HIGH RISK customer loaded! Click Predict Churn now.")
    st.subheader("📈 Business Impact Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Customers", "5,630")
    col2.metric("Churn Rate", "16.84%")
    col3.metric("Annual Loss", "₹47,40,000")
    col4.metric("Potential Savings", "₹16,20,000")

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