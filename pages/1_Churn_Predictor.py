import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import shap
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Churn Predictor", page_icon="🔮", layout="wide")

@st.cache_resource
def load_model():
    try:
        return joblib.load('src/best_churn_model.pkl')
    except Exception as e:
        st.error(f"Model loading failed: {e}")
        return None

@st.cache_resource
def load_explainer(_model):
    return shap.TreeExplainer(_model)

with st.spinner("Loading AI Model..."):
    model = load_model()
    explainer = load_explainer(model)

if model is None:
    st.stop()

st.title("🔮 Churn Predictor")
st.markdown("**Predict which customers will churn & get personalized retention strategy**")
st.divider()

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

def create_shap_chart(input_df):
    shap_values = explainer.shap_values(input_df)
    if isinstance(shap_values, list):
        sv = shap_values[1][0]
    else:
        sv = shap_values[0]
    feature_names = input_df.columns.tolist()
    shap_df = pd.DataFrame({
        'Feature': feature_names,
        'SHAP Value': sv
    }).sort_values('SHAP Value', key=abs, ascending=False).head(10)
    colors = ['#ff4444' if v > 0 else '#44bb44' for v in shap_df['SHAP Value']]
    fig = go.Figure(go.Bar(
        x=shap_df['SHAP Value'],
        y=shap_df['Feature'],
        orientation='h',
        marker_color=colors,
        text=[f"{v:+.3f}" for v in shap_df['SHAP Value']],
        textposition='outside'
    ))
    fig.update_layout(
        title="Why This Customer Will Churn (Live SHAP)",
        xaxis_title="SHAP Value (Red = Increases Churn, Green = Decreases Churn)",
        height=400,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

def get_churn_reasons():
    reasons = []
    if tenure < 3:
        reasons.append(("📅 New Customer", "Tenure < 3 months — new customers have highest churn risk", "HIGH"))
    if complain == 1:
        reasons.append(("😤 Active Complaint", "Unresolved complaint — complained customers churn 3x more", "HIGH"))
    if satisfaction_score <= 2:
        reasons.append(("😞 Low Satisfaction", f"Satisfaction score {satisfaction_score}/5 — very dissatisfied customer", "HIGH"))
    if cashback_amount < 100:
        reasons.append(("💸 Low Cashback", f"Only Rs.{cashback_amount} cashback — low incentive to stay", "MEDIUM"))
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

def get_health_score(prob):
    return int((1 - prob) * 100)

if predict_btn:
    with st.spinner("Analyzing customer profile..."):
        input_df = get_input()
        prob = model.predict_proba(input_df)[0][1]
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

    # Row 1 — Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Churn Probability", f"{prob*100:.1f}%")
    col2.metric("Risk Segment", risk)
    col3.metric("Health Score", f"{health_score}/100")
    col4.metric("ROI if Retained", f"{roi:.0f}%")

    st.divider()

    # Row 2 — Gauge + Reasons
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

    # Row 3 — LIVE SHAP
    st.subheader("🧠 Live SHAP Explanation — Why This Customer?")
    st.markdown("*Real-time explanation from XGBoost model showing exactly which factors drive this prediction*")
    with st.spinner("Calculating SHAP values..."):
        shap_fig = create_shap_chart(input_df)
    st.plotly_chart(shap_fig, use_container_width=True)
    st.caption("Red bars = factors INCREASING churn risk | Green bars = factors DECREASING churn risk")

    st.divider()

    # Row 4 — Health Score
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

    # Row 5 — Retention Strategy
    st.subheader("💡 Recommended Retention Strategy")
    for action in strategy:
        st.markdown(f"- {action}")

    st.divider()

    # Row 6 — ROI Calculator
    st.subheader("💰 ROI Calculator")
    col4, col5, col6 = st.columns(3)
    col4.metric("Campaign Cost", f"₹{campaign_cost:,}")
    col5.metric("Revenue Saved", f"₹{revenue_saved:,.0f}")
    col6.metric("ROI", f"{roi:.0f}%")

    st.divider()

    # Row 7 — Priority Score
    st.subheader("🎯 Customer Priority Score")
    st.markdown("*Where does this customer rank in your retention queue?*")

    priority_score = annual_revenue * prob

    if priority_score >= 20000:
        priority_label = "PRIORITY 1 — Contact Immediately"
        priority_color = "red"
        priority_action = "High value customer with high churn risk — every day of delay costs money"
    elif priority_score >= 5000:
        priority_label = "PRIORITY 2 — Contact This Week"
        priority_color = "orange"
        priority_action = "Medium priority — schedule retention outreach within 7 days"
    else:
        priority_label = "PRIORITY 3 — Standard Follow-up"
        priority_color = "green"
        priority_action = "Low urgency — include in regular engagement campaigns"

    col1, col2, col3 = st.columns(3)
    col1.metric("Annual Revenue", f"₹{annual_revenue:,}")
    col2.metric("Churn Probability", f"{prob*100:.1f}%")
    col3.metric("Priority Score", f"{priority_score:,.0f}")

    st.markdown(
        f"<h3 style='color:{priority_color}'>{priority_label}</h3>",
        unsafe_allow_html=True)
    st.info(priority_action)

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

st.divider()
st.markdown("""
<div style='text-align: center; color: gray; padding: 10px;'>
    Built by <b>Amruth</b> | Python • XGBoost • SHAP • Streamlit | 
    <a href='https://github.com/Amruth011/customer-churn-prediction-retention-roi' target='_blank'>GitHub</a>
</div>
""", unsafe_allow_html=True)