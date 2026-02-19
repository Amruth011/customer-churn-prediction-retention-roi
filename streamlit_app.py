import streamlit as st
import pandas as pd
import numpy as np
import joblib
import warnings
warnings.filterwarnings('ignore')

# Page config
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🛒",
    layout="wide"
)

# Load model
@st.cache_resource
def load_model():
    return joblib.load('src/best_churn_model.pkl')

model = load_model()

# Title
st.title("🛒 Customer Churn Prediction & Retention ROI")
st.markdown("**Predict which customers will churn & recommend retention strategies**")
st.divider()

# Sidebar inputs
st.sidebar.header("📋 Customer Details")

tenure = st.sidebar.slider("Tenure (months)", 0, 61, 10)
city_tier = st.sidebar.selectbox("City Tier", [1, 2, 3])
warehouse_to_home = st.sidebar.slider("Warehouse to Home (km)", 5, 127, 15)
hour_spend_on_app = st.sidebar.slider("Hours on App", 0, 5, 3)
devices_registered = st.sidebar.slider("Devices Registered", 1, 6, 3)
satisfaction_score = st.sidebar.slider("Satisfaction Score", 1, 5, 3)
number_of_address = st.sidebar.slider("Number of Address", 1, 22, 3)
complain = st.sidebar.selectbox("Complained?", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
order_amount_hike = st.sidebar.slider("Order Amount Hike %", 11, 26, 15)
coupon_used = st.sidebar.slider("Coupons Used", 0, 16, 2)
order_count = st.sidebar.slider("Order Count", 1, 16, 3)
day_since_last_order = st.sidebar.slider("Days Since Last Order", 0, 46, 5)
cashback_amount = st.sidebar.slider("Cashback Amount (₹)", 0, 325, 150)
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

# Feature engineering (same as training)
engagement_score = hour_spend_on_app * order_count
order_frequency = order_count / (day_since_last_order + 1)
cashback_per_order = cashback_amount / (order_count + 1)
is_new_customer = 1 if tenure < 3 else 0
high_risk = 1 if (complain == 1 and satisfaction_score <= 2) else 0
device_loyalty = devices_registered

# Build input
input_data = pd.DataFrame([{
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
    'engagement_score': engagement_score,
    'order_frequency': order_frequency,
    'cashback_per_order': cashback_per_order,
    'is_new_customer': is_new_customer,
    'high_risk': high_risk,
    'device_loyalty': device_loyalty
}])

# Predict
if st.sidebar.button("🔮 Predict Churn", type="primary"):

    prob = model.predict_proba(input_data)[0][1]
    pred = model.predict(input_data)[0]

    # Risk segment
    if prob >= 0.6:
        risk = "🔴 HIGH RISK"
        color = "red"
        strategy = """
        - Immediate personal outreach
        - 20-30% discount coupon
        - Free delivery for 3 months
        - Priority customer support
        """
    elif prob >= 0.3:
        risk = "🟡 MEDIUM RISK"
        color = "orange"
        strategy = """
        - Loyalty reward points
        - Personalized recommendations
        - Flash sale early access
        - Cashback on next 3 orders
        """
    else:
        risk = "🟢 LOW RISK"
        color = "green"
        strategy = """
        - Regular engagement emails
        - Referral program
        - Seasonal offers
        """

    # Display results
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Churn Probability", f"{prob*100:.1f}%")

    with col2:
        st.metric("Risk Segment", risk)

    with col3:
        avg_revenue = 5000
        campaign_cost = 500
        revenue_saved = avg_revenue * 0.30
        roi = ((revenue_saved - campaign_cost) / campaign_cost) * 100
        st.metric("ROI if Retained", f"{roi:.0f}%")

    st.divider()

    # Churn probability bar
    st.subheader("📊 Churn Risk Score")
    st.progress(float(prob))
    st.markdown(f"<h2 style='color:{color}'>{risk} — {prob*100:.1f}% chance of churning</h2>",
                unsafe_allow_html=True)

    st.divider()

    # Retention strategy
    st.subheader("💡 Recommended Retention Strategy")
    st.markdown(strategy)

    st.divider()

    # ROI Calculator
    st.subheader("💰 ROI Calculator")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric("Campaign Cost", f"₹{campaign_cost:,}")
    with col5:
        st.metric("Revenue Saved", f"₹{revenue_saved:,.0f}")
    with col6:
        st.metric("ROI", f"{roi:.0f}%")

else:
    st.info("👈 Fill in customer details in the sidebar and click **Predict Churn**")
    
    # Show business summary
    st.subheader("📈 Business Impact Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Customers", "5,630")
    col2.metric("Churn Rate", "16.84%")
    col3.metric("Annual Loss", "₹47,40,000")
    col4.metric("Potential Savings", "₹14,25,000")