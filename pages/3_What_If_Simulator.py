import streamlit as st
import pandas as pd
import joblib
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
st.markdown("*See how changing customer experience impacts churn probability*")
st.divider()

st.subheader("👤 Current Customer Profile")
col1, col2, col3 = st.columns(3)
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
    annual_revenue = st.number_input("Annual Revenue (₹)", 0, 500000, 5000, 1000)
    coupon = st.slider("Coupons Used", 0, 16, 0)

def make_prediction(sat, comp, cash, coup):
    return pd.DataFrame([{
        'Tenure': tenure,
        'PreferredLoginDevice': 2,
        'CityTier': 3,
        'WarehouseToHome': 30,
        'PreferredPaymentMode': 1,
        'Gender': 1,
        'HourSpendOnApp': 1,
        'NumberOfDeviceRegistered': 2,
        'PreferedOrderCat': 3,
        'SatisfactionScore': sat,
        'MaritalStatus': 2,
        'NumberOfAddress': 2,
        'Complain': comp,
        'OrderAmountHikeFromlastYear': 11,
        'CouponUsed': coup,
        'OrderCount': order_count,
        'DaySinceLastOrder': day_since,
        'CashbackAmount': cash,
        'engagement_score': 1 * order_count,
        'order_frequency': order_count / (day_since + 1),
        'cashback_per_order': cash / (order_count + 1),
        'is_new_customer': 1 if tenure < 3 else 0,
        'high_risk': 1 if (comp == 1 and sat <= 2) else 0,
        'device_loyalty': 2
    }])

current_prob = model.predict_proba(
    make_prediction(satisfaction, complain, cashback, coupon))[0][1]

st.divider()
st.subheader("🎮 Simulate Retention Actions")

col1, col2 = st.columns(2)
with col1:
    new_sat = st.slider("Improve Satisfaction Score", 1, 5, satisfaction)
    new_complain = st.selectbox("Resolve Complaint?", [complain, 0],
        format_func=lambda x: "Unresolved" if x==1 else "Resolved")
with col2:
    new_cash = st.slider("Increase Cashback (₹)", 0, 325, cashback)
    new_coupon = st.slider("Offer More Coupons", 0, 16, coupon)

new_prob = model.predict_proba(
    make_prediction(new_sat, new_complain, new_cash, new_coupon))[0][1]

reduction = current_prob - new_prob
revenue_impact = reduction * annual_revenue

st.divider()
st.subheader("📊 Simulation Results")
col3, col4, col5 = st.columns(3)
col3.metric("Before Intervention", f"{current_prob*100:.1f}%")
col4.metric("After Intervention", f"{new_prob*100:.1f}%",
           delta=f"{-reduction*100:.1f}%")
col5.metric("Revenue Protected", f"₹{revenue_impact:,.0f}")

if reduction > 0:
    st.success(f"✅ Reduced churn by {reduction*100:.1f}% — protecting ₹{revenue_impact:,.0f}!")
elif reduction == 0:
    st.warning("⚠️ No change — try different interventions")
else:
    st.error("❌ These changes increased churn risk — reconsider strategy")