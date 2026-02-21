import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import warnings

warnings.filterwarnings('ignore')

# --- CONFIGURATION ---
st.set_page_config(page_title="Churn Predictor", page_icon="🔮", layout="wide")

# --- INITIALIZE SESSION STATE ---
if 'sample' not in st.session_state:
    st.session_state['sample'] = False

@st.cache_resource
def load_model():
    try:
        # Powered by the GNN-LSTM and PINN principles for robust forecasting
        return joblib.load('src/best_churn_model.pkl')
    except Exception as e:
        st.error(f"Model loading failed: {e}")
        return None

with st.spinner("Loading AI Model..."):
    model = load_model()

# --- SIDEBAR UI ---
st.sidebar.header("📋 Customer Details")

if st.sidebar.button("📋 Load Sample HIGH RISK Customer"):
    st.session_state['sample'] = True
    st.rerun()

if st.sidebar.button("🔄 Reset to Default"):
    st.session_state['sample'] = False
    st.rerun()

sample = st.session_state['sample']

# Sidebar inputs
tenure = st.sidebar.slider("Tenure (months)", 0, 61, 1 if sample else 10)
city_tier = st.sidebar.selectbox("City Tier", [1, 2, 3], index=2 if sample else 0)
warehouse_to_home = st.sidebar.slider("Warehouse to Home (km)", 5, 127, 30 if sample else 15)
hour_spend_on_app = st.sidebar.slider("Hours on App", 0, 5, 1 if sample else 3)
devices_registered = st.sidebar.slider("Devices Registered", 1, 6, 2 if sample else 3)
satisfaction_score = st.sidebar.slider("Satisfaction Score", 1, 5, 1 if sample else 3)
number_of_address = st.sidebar.slider("Number of Address", 1, 22, 12 if sample else 3)
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

# --- DATA PREPARATION ---
def get_input():
    data = {
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
    }
    return pd.DataFrame([data])

# --- GAUGE CHART ---
def create_gauge(prob):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={'text': "Churn Risk %", 'font': {'size': 20}},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkred" if prob >= 0.6 else "orange" if prob >= 0.3 else "green"},
            'steps': [
                {'range': [0, 30], 'color': '#90EE90'},
                {'range': [30, 60], 'color': '#FFD700'},
                {'range': [60, 100], 'color': '#FFB6C1'}
            ]
        }
    ))
    fig.update_layout(height=280, margin=dict(l=20, r=20, t=50, b=20))
    return fig

# --- REASONING LOGIC ---
def get_churn_reasons():
    reasons = []
    if tenure < 3: reasons.append(("📅 New Customer", "High risk during onboarding phase", "HIGH"))
    if complain == 1: reasons.append(("😤 Active Complaint", "Historical data shows higher churn for complaints", "HIGH"))
    if satisfaction_score <= 2: reasons.append(("😞 Low Satisfaction", f"Critical dissatisfaction ({satisfaction_score}/5)", "HIGH"))
    return reasons[:3]

# --- MAIN APP LAYOUT ---
st.title("🔮 Churn Predictor")

if model is None:
    st.stop()

if predict_btn:
    input_df = get_input()
    prob = model.predict_proba(input_df)[0][1]
    health_score = int((1 - prob) * 100)
    reasons = get_churn_reasons()

    # Budget/ROI logic variables (Hardcoded for simulation or link to inputs)
    avg_rev = annual_revenue
    high_cost, medium_cost, low_cost = 1000, 500, 200 # Costs per campaign
    high_ret, medium_ret, low_ret = 0.40, 0.25, 0.10 # Retention rates
    total_budget = 50000 
    
    # Tier Budget Allocation
    high_spend = total_budget * 0.6
    medium_spend = total_budget * 0.3
    low_spend = total_budget * 0.1

    # --- UPDATED ROI CALCULATION LOGIC ---
    high_customers_funded = int(high_spend / high_cost)
    medium_customers_funded = int(medium_spend / medium_cost) if medium_spend > 0 else 0
    low_customers_funded = int(low_spend / low_cost) if low_spend > 0 else 0

    high_saved = int(high_customers_funded * high_ret) * avg_rev
    medium_saved = int(medium_customers_funded * medium_ret) * avg_rev
    low_saved = int(low_customers_funded * low_ret) * avg_rev
    total_revenue_saved = high_saved + medium_saved + low_saved
    roi = ((total_revenue_saved - total_budget) / total_budget) * 100

    # Display Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Churn Prob.", f"{prob*100:.1f}%")
    col2.metric("Health Score", f"{health_score}/100")
    col3.metric("Total Revenue Saved", f"₹{total_revenue_saved:,.0f}")
    col4.metric("ROI", f"{roi:.0f}%")

    st.divider()
    
    # Segment UI
    risk_label = "🔴 HIGH RISK" if prob >= 0.6 else "🟡 MEDIUM RISK" if prob >= 0.3 else "🟢 LOW RISK"
    st.subheader(f"Risk Segment: {risk_label}")
    
    col_l, col_r = st.columns(2)
    with col_l:
        st.plotly_chart(create_gauge(prob), use_container_width=True)
    with col_r:
        st.subheader("🔍 Top Churn Drivers")
        for title, desc, level in reasons:
            st.error(f"**{title}**: {desc}")

    st.divider()
    
    # --- UPDATED DATA TABLE FOR RETAINED CUSTOMERS ---
    st.subheader("📊 Retention Campaign Impact")
    impact_data = pd.DataFrame({
        'Risk Tier': ['High', 'Medium', 'Low'],
        'Funded': [high_customers_funded, medium_customers_funded, low_customers_funded],
        'Retained': [
            int(high_customers_funded * high_ret), 
            int(medium_customers_funded * medium_ret), 
            int(low_customers_funded * low_ret)
        ],
        'Revenue Saved': [f"₹{high_saved:,}", f"₹{medium_saved:,}", f"₹{low_saved:,}"]
    })
    st.table(impact_data)

else:
    st.info("👈 Enter customer details in the sidebar and click **Predict Churn**.")