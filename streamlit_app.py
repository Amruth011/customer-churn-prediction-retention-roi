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

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🔮 Churn Predictor",
    "🎯 Priority Score",
    "🔄 What-If Simulator",
    "💰 Budget Optimizer"
])

# ============================================
# SIDEBAR INPUTS
# ============================================
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
annual_revenue = st.sidebar.number_input("Customer Annual Revenue (₹)", 0, 500000, 5000, 1000)

predict_btn = st.sidebar.button("🔮 Predict Churn", type="primary")

# ============================================
# FEATURE ENGINEERING
# ============================================
def get_input():
    engagement_score = hour_spend_on_app * order_count
    order_frequency = order_count / (day_since_last_order + 1)
    cashback_per_order = cashback_amount / (order_count + 1)
    is_new_customer = 1 if tenure < 3 else 0
    high_risk = 1 if (complain == 1 and satisfaction_score <= 2) else 0
    device_loyalty = devices_registered

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
        'engagement_score': engagement_score,
        'order_frequency': order_frequency,
        'cashback_per_order': cashback_per_order,
        'is_new_customer': is_new_customer,
        'high_risk': high_risk,
        'device_loyalty': device_loyalty
    }])

# ============================================
# TAB 1: CHURN PREDICTOR
# ============================================
with tab1:
    if predict_btn:
        input_data = get_input()
        prob = model.predict_proba(input_data)[0][1]

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

        col1, col2, col3 = st.columns(3)
        col1.metric("Churn Probability", f"{prob*100:.1f}%")
        col2.metric("Risk Segment", risk)
        campaign_cost = 500
        revenue_saved = annual_revenue * 0.30
        roi = ((revenue_saved - campaign_cost) / campaign_cost) * 100
        col3.metric("ROI if Retained", f"{roi:.0f}%")

        st.divider()
        st.subheader("📊 Churn Risk Score")
        st.progress(float(prob))
        st.markdown(
            f"<h2 style='color:{color}'>{risk} — {prob*100:.1f}% chance of churning</h2>",
            unsafe_allow_html=True
        )
        st.divider()
        st.subheader("💡 Recommended Retention Strategy")
        st.markdown(strategy)
        st.divider()
        st.subheader("💰 ROI Calculator")
        col4, col5, col6 = st.columns(3)
        col4.metric("Campaign Cost", f"₹{campaign_cost:,}")
        col5.metric("Revenue Saved", f"₹{revenue_saved:,.0f}")
        col6.metric("ROI", f"{roi:.0f}%")

    else:
        st.info("👈 Fill in customer details in the sidebar and click **Predict Churn**")
        st.subheader("📈 Business Impact Summary")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Customers", "5,630")
        col2.metric("Churn Rate", "16.84%")
        col3.metric("Annual Loss", "₹47,40,000")
        col4.metric("Potential Savings", "₹16,20,000")

# ============================================
# TAB 2: PRIORITY SCORE
# ============================================
with tab2:
    st.subheader("🎯 Customer Priority Score")
    st.markdown("*Who should your retention team call FIRST?*")
    st.markdown("**Formula: Priority Score = Annual Revenue × Churn Probability**")
    st.divider()

    if predict_btn:
        input_data = get_input()
        prob = model.predict_proba(input_data)[0][1]
        priority_score = annual_revenue * prob

        if priority_score >= 20000:
            priority_label = "🔴 PRIORITY 1 — Contact Immediately"
            priority_color = "red"
            priority_reason = "High value customer with high churn risk — every day of delay costs money"
        elif priority_score >= 5000:
            priority_label = "🟡 PRIORITY 2 — Contact This Week"
            priority_color = "orange"
            priority_reason = "Medium priority — schedule retention outreach within 7 days"
        else:
            priority_label = "🟢 PRIORITY 3 — Standard Follow-up"
            priority_color = "green"
            priority_reason = "Low urgency — include in regular engagement campaigns"

        col1, col2, col3 = st.columns(3)
        col1.metric("Annual Revenue", f"₹{annual_revenue:,}")
        col2.metric("Churn Probability", f"{prob*100:.1f}%")
        col3.metric("Priority Score", f"{priority_score:,.0f}")
        st.divider()
        st.markdown(
            f"<h2 style='color:{priority_color}'>{priority_label}</h2>",
            unsafe_allow_html=True
        )
        st.info(priority_reason)
        st.caption("Higher Priority Score = Contact First = Save More Revenue")

    else:
        st.info("👈 Fill sidebar details & click Predict Churn to see Priority Score")
        st.subheader("📊 How Priority Score Works")
        example_data = pd.DataFrame({
            'Customer': ['Customer A', 'Customer B', 'Customer C'],
            'Annual Revenue (₹)': [50000, 5000, 1000],
            'Churn Probability': ['90%', '95%', '85%'],
            'Priority Score': [45000, 4750, 850],
            'Action': ['Call Today', 'Call This Week', 'Email Campaign']
        })
        st.table(example_data.set_index('Customer'))
        st.warning("Customer B has higher churn probability but Customer A should be contacted FIRST because revenue at risk is 10x higher!")

# ============================================
# TAB 3: WHAT-IF SIMULATOR
# ============================================
with tab3:
    st.subheader("🔄 What-If Retention Simulator")
    st.markdown("*See how changing customer experience impacts churn probability*")
    st.divider()

    if predict_btn:
        input_data = get_input()
        current_prob = model.predict_proba(input_data)[0][1]

        st.markdown("### Current Churn Probability")
        st.progress(float(current_prob))
        st.metric("Current Risk", f"{current_prob*100:.1f}%")
        st.divider()
        st.markdown("### 🎮 Simulate Retention Actions")

        col1, col2 = st.columns(2)
        with col1:
            new_satisfaction = st.slider(
                "Improve Satisfaction Score", 1, 5, satisfaction_score)
            new_complain = st.selectbox(
                "Resolve Complaint?", [complain, 0],
                format_func=lambda x: "Complaint Unresolved" if x==1 else "Complaint Resolved")
        with col2:
            new_cashback = st.slider(
                "Increase Cashback (₹)", 0, 325, cashback_amount)
            new_coupon = st.slider(
                "Offer More Coupons", 0, 16, coupon_used)

        new_input = pd.DataFrame([{
            'Tenure': tenure,
            'PreferredLoginDevice': preferred_login,
            'CityTier': city_tier,
            'WarehouseToHome': warehouse_to_home,
            'PreferredPaymentMode': preferred_payment,
            'Gender': gender,
            'HourSpendOnApp': hour_spend_on_app,
            'NumberOfDeviceRegistered': devices_registered,
            'PreferedOrderCat': order_cat,
            'SatisfactionScore': new_satisfaction,
            'MaritalStatus': marital_status,
            'NumberOfAddress': number_of_address,
            'Complain': new_complain,
            'OrderAmountHikeFromlastYear': order_amount_hike,
            'CouponUsed': new_coupon,
            'OrderCount': order_count,
            'DaySinceLastOrder': day_since_last_order,
            'CashbackAmount': new_cashback,
            'engagement_score': hour_spend_on_app * order_count,
            'order_frequency': order_count / (day_since_last_order + 1),
            'cashback_per_order': new_cashback / (order_count + 1),
            'is_new_customer': 1 if tenure < 3 else 0,
            'high_risk': 1 if (new_complain == 1 and new_satisfaction <= 2) else 0,
            'device_loyalty': devices_registered
        }])

        new_prob = model.predict_proba(new_input)[0][1]
        reduction = current_prob - new_prob
        revenue_impact = reduction * annual_revenue

        st.divider()
        st.markdown("### 📊 Simulation Results")
        col3, col4, col5 = st.columns(3)
        col3.metric("Before Intervention", f"{current_prob*100:.1f}%")
        col4.metric("After Intervention", f"{new_prob*100:.1f}%",
                   delta=f"{-reduction*100:.1f}%")
        col5.metric("Revenue Protected", f"₹{revenue_impact:,.0f}")

        if reduction > 0:
            st.success(f"✅ Retention actions reduced churn by {reduction*100:.1f}% — protecting ₹{revenue_impact:,.0f}!")
        elif reduction == 0:
            st.warning("⚠️ No change — try different interventions")
        else:
            st.error("❌ These changes increased churn risk — reconsider strategy")

    else:
        st.info("👈 Fill sidebar details & click Predict Churn to use the simulator")
        st.subheader("💡 What This Simulator Does")
        st.markdown("""
- Set current customer details in sidebar
- Click Predict Churn
- Adjust **satisfaction, complaints, cashback, coupons**
- See in **real time** how much churn probability drops
- Calculate exact **revenue protected** by each action
        """)

# ============================================
# TAB 4: BUDGET OPTIMIZER
# ============================================
with tab4:
    st.subheader("💰 Retention Budget Optimizer")
    st.markdown("*How do I allocate my retention budget for maximum ROI?*")
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        total_budget = st.number_input(
            "Total Retention Budget (₹)", 10000, 10000000, 500000, 10000)
    with col2:
        high_risk_customers = st.number_input("High Risk Customers", 1, 10000, 937)
        medium_risk_customers = st.number_input("Medium Risk Customers", 1, 10000, 14)

    avg_rev = st.slider("Average Customer Revenue (₹/year)", 1000, 50000, 5000, 1000)

    if st.button("🧮 Optimize Budget", type="primary"):
        high_cost, medium_cost, low_cost = 500, 300, 100
        high_retention, medium_retention, low_retention = 0.30, 0.25, 0.15

        high_spend = min(total_budget, high_risk_customers * high_cost)
        remaining = total_budget - high_spend
        medium_spend = min(remaining, medium_risk_customers * medium_cost)
        remaining = remaining - medium_spend
        low_customers = max(0, int(remaining / low_cost))
        low_spend = low_customers * low_cost

        high_saved = int(high_risk_customers * high_retention) * avg_rev
        medium_saved = int(medium_risk_customers * medium_retention) * avg_rev
        low_saved = int(low_customers * low_retention) * avg_rev
        total_saved = high_saved + medium_saved + low_saved
        total_spent = high_spend + medium_spend + low_spend
        roi = ((total_saved - total_spent) / total_spent) * 100

        st.subheader("📊 Optimized Budget Allocation")
        col3, col4, col5 = st.columns(3)
        col3.metric("Total Budget", f"₹{total_budget:,}")
        col4.metric("Total Revenue Saved", f"₹{total_saved:,}")
        col5.metric("Overall ROI", f"{roi:.0f}%")
        st.divider()

        allocation_df = pd.DataFrame({
            'Segment': ['🔴 High Risk', '🟡 Medium Risk', '🟢 Low Risk'],
            'Customers': [high_risk_customers, medium_risk_customers, low_customers],
            'Cost Per Customer': [f'₹{high_cost}', f'₹{medium_cost}', f'₹{low_cost}'],
            'Total Spend': [f'₹{high_spend:,}', f'₹{medium_spend:,}', f'₹{low_spend:,}'],
            'Customers Retained': [
                int(high_risk_customers * high_retention),
                int(medium_risk_customers * medium_retention),
                int(low_customers * low_retention)
            ],
            'Revenue Saved': [f'₹{high_saved:,}', f'₹{medium_saved:,}', f'₹{low_saved:,}']
        })
        st.table(allocation_df)
        st.divider()

        if roi > 100:
            st.success(f"✅ Every ₹1 spent returns ₹{total_saved/total_spent:.1f} — Strong business case!")
        elif roi > 0:
            st.warning("⚠️ Positive ROI but consider allocating more to High Risk segment")
        else:
            st.error("❌ Budget too low — focus on High Risk customers only")

    else:
        st.info("👆 Enter your budget details and click **Optimize Budget**")
        st.subheader("💡 How Budget Optimizer Works")
        st.markdown("""
- Enter your **total retention budget**
- Enter number of customers in each risk segment
- Optimizer allocates budget starting from **highest ROI segment first**
- Shows exact **revenue saved per segment**
- Gives **overall ROI** of your retention campaign
        """)