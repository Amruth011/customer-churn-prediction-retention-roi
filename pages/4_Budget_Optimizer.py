import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Budget Optimizer", page_icon="💰", layout="wide")

st.title("💰 Retention Budget Optimizer")
st.markdown("*How do I allocate my retention budget for maximum ROI?*")
st.divider()

col1, col2 = st.columns(2)
with col1:
    total_budget = st.number_input("Total Retention Budget (₹)", 10000, 10000000, 600000, 10000)
with col2:
    high_risk_count = st.number_input("High Risk Customers", 1, 10000, 937)
    medium_risk_count = st.number_input("Medium Risk Customers", 1, 10000, 14)

avg_rev = st.slider("Average Customer Revenue (₹/year)", 1000, 50000, 5000, 1000)

if st.button("🧮 Optimize Budget", type="primary"):
    with st.spinner("Optimizing budget allocation..."):
        high_cost, medium_cost, low_cost = 500, 300, 100
        high_ret, medium_ret, low_ret = 0.30, 0.25, 0.15

        high_spend = min(total_budget, high_risk_count * high_cost)
        remaining = total_budget - high_spend
        medium_spend = min(remaining, medium_risk_count * medium_cost)
        remaining -= medium_spend
        low_customers = max(0, int(remaining / low_cost))
        low_spend = low_customers * low_cost

        high_customers_funded = int(high_spend / high_cost)
        medium_customers_funded = int(medium_spend / medium_cost) if medium_spend > 0 else 0
        low_customers_funded = int(low_spend / low_cost) if low_spend > 0 else 0

        high_saved = int(high_customers_funded * high_ret) * avg_rev
        medium_saved = int(medium_customers_funded * medium_ret) * avg_rev
        low_saved = int(low_customers_funded * low_ret) * avg_rev
        total_saved = high_saved + medium_saved + low_saved
        total_spent = high_spend + medium_spend + low_spend
        roi = ((total_saved - total_spent) / total_spent) * 100

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Budget", f"₹{total_budget:,}")
        col2.metric("Total Spent", f"₹{total_spent:,}")
        col3.metric("Revenue Saved", f"₹{total_saved:,}")
        col4.metric("Overall ROI", f"{roi:.0f}%")
        st.divider()

        df = pd.DataFrame({
            'Segment': ['🔴 High Risk', '🟡 Medium Risk', '🟢 Low Risk'],
            'Customers': [high_risk_count, medium_risk_count, low_customers],
            'Cost/Customer': [f'₹{high_cost}', f'₹{medium_cost}', f'₹{low_cost}'],
            'Total Spend': [f'₹{high_spend:,}', f'₹{medium_spend:,}', f'₹{low_spend:,}'],
            'Retained': [
                int(high_customers_funded * high_ret),
                int(medium_customers_funded * medium_ret),
                int(low_customers_funded * low_ret)
            ],
            'Revenue Saved': [f'₹{high_saved:,}', f'₹{medium_saved:,}', f'₹{low_saved:,}']
        })
        st.table(df.set_index('Segment'))
        st.divider()

        fig = go.Figure(data=[
            go.Bar(name='Total Spend',
                   x=['🔴 High Risk', '🟡 Medium Risk', '🟢 Low Risk'],
                   y=[high_spend, medium_spend, low_spend],
                   marker_color=['#ff4444', '#ffaa00', '#44bb44']),
            go.Bar(name='Revenue Saved',
                   x=['🔴 High Risk', '🟡 Medium Risk', '🟢 Low Risk'],
                   y=[high_saved, medium_saved, low_saved],
                   marker_color=['#ff9999', '#ffdd99', '#99dd99'])
        ])
        fig.update_layout(
            title="Budget Spend vs Revenue Saved by Segment",
            barmode='group',
            height=400,
            yaxis_title="Amount (₹)"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.divider()

        if roi > 100:
            st.success(f"✅ Every ₹1 spent returns ₹{total_saved/total_spent:.1f} — Strong business case!")
        elif roi > 0:
            st.warning("⚠️ Positive ROI — consider allocating more to High Risk segment")
        else:
            st.error("❌ Budget too low — focus on High Risk customers only")

else:
    st.info("👆 Enter budget details and click **Optimize Budget**")
    st.markdown("""
**How it works:**
- Allocates budget starting from **highest ROI segment first**
- High Risk → ₹500/customer
- Medium Risk → ₹300/customer
- Low Risk → ₹100/customer
    """)