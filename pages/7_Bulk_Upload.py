import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Bulk Upload", page_icon="📤", layout="wide")

@st.cache_resource
def load_model():
    try:
        return joblib.load('src/best_churn_model.pkl')
    except Exception as e:
        st.error("Model loading failed: " + str(e))
        return None

model = load_model()
if model is None:
    st.stop()

st.title("Bulk Churn Prediction")
st.markdown("*Upload a CSV of multiple customers — get predictions for all at once*")
st.divider()

st.subheader("How to Use")
col1, col2, col3 = st.columns(3)
col1.info("**Step 1**\n\nDownload the sample CSV to see the required format")
col2.info("**Step 2**\n\nFill in your customer data in the same format")
col3.info("**Step 3**\n\nUpload your CSV and get instant predictions!")

with open('data/raw/sample_upload.csv', 'rb') as f:
    st.download_button(
        label="Download Sample CSV Template",
        data=f,
        file_name="sample_customers.csv",
        mime="text/csv"
    )

st.divider()

st.subheader("Upload Your Customer Data")
uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=['csv'],
    help="CSV must have same columns as sample template"
)

def engineer_features(data):
    data = data.copy()
    data['engagement_score'] = data['HourSpendOnApp'] * data['OrderCount']
    data['order_frequency'] = data['OrderCount'] / (data['DaySinceLastOrder'] + 1)
    data['cashback_per_order'] = data['CashbackAmount'] / (data['OrderCount'] + 1)
    data['is_new_customer'] = (data['Tenure'] < 3).astype(int)
    data['high_risk'] = ((data['Complain'] == 1) & (data['SatisfactionScore'] <= 2)).astype(int)
    data['device_loyalty'] = data['NumberOfDeviceRegistered']
    return data

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully — " + str(len(df)) + " customers found!")

    st.subheader("Data Preview")
    st.dataframe(df.head(10), use_container_width=True)
    st.divider()

    if st.button("Predict Churn for All Customers", type="primary"):
        with st.spinner("Predicting churn for " + str(len(df)) + " customers..."):

            if 'AnnualRevenue' in df.columns:
                annual_revenue = df['AnnualRevenue'].copy()
            else:
                annual_revenue = pd.Series([5000] * len(df))

            df_features = engineer_features(df)

            if 'AnnualRevenue' in df_features.columns:
                df_features = df_features.drop('AnnualRevenue', axis=1)

            churn_probs = model.predict_proba(df_features)[:, 1]
            churn_pred = model.predict(df_features)

            results = df.copy()
            results['Churn_Probability'] = (churn_probs * 100).round(1)
            results['Churn_Predicted'] = churn_pred
            results['AnnualRevenue'] = annual_revenue
            results['Priority_Score'] = (annual_revenue * churn_probs).round(0)
            results['Health_Score'] = ((1 - churn_probs) * 100).round(0).astype(int)

            risk_labels = []
            for p in churn_probs:
                if p >= 0.6:
                    risk_labels.append('HIGH RISK')
                elif p >= 0.3:
                    risk_labels.append('MEDIUM RISK')
                else:
                    risk_labels.append('LOW RISK')
            results['Risk_Level'] = risk_labels

            action_map = {
                'HIGH RISK': 'Call Today — Personal Outreach',
                'MEDIUM RISK': 'Call This Week — Loyalty Offer',
                'LOW RISK': 'Email Campaign — Regular Engagement'
            }
            results['Recommended_Action'] = results['Risk_Level'].map(action_map)

        st.divider()
        st.subheader("Prediction Summary")

        high_risk_count = int((churn_probs >= 0.6).sum())
        medium_risk_count = int(((churn_probs >= 0.3) & (churn_probs < 0.6)).sum())
        low_risk_count = int((churn_probs < 0.3).sum())
        revenue_at_risk = float(annual_revenue[churn_probs >= 0.6].sum())
        avg_prob = float(churn_probs.mean() * 100)

        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Total Customers", len(df))
        col2.metric("High Risk", high_risk_count)
        col3.metric("Medium Risk", medium_risk_count)
        col4.metric("Low Risk", low_risk_count)
        col5.metric("Avg Churn Risk", str(round(avg_prob, 1)) + "%")

        st.metric("Total Revenue at Risk", "Rs." + str(round(revenue_at_risk, 0)))

        st.divider()

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Risk Distribution")
            fig_pie = go.Figure(data=[go.Pie(
                labels=['High Risk', 'Medium Risk', 'Low Risk'],
                values=[high_risk_count, medium_risk_count, low_risk_count],
                hole=0.4,
                marker_colors=['#ff4444', '#ffaa00', '#44bb44']
            )])
            fig_pie.update_layout(height=350)
            st.plotly_chart(fig_pie, use_container_width=True)

        with col2:
            st.subheader("Churn Probability Distribution")
            fig_hist = px.histogram(
                x=churn_probs * 100,
                nbins=20,
                color_discrete_sequence=['#ff4444'],
                labels={'x': 'Churn Probability (%)'}
            )
            fig_hist.update_layout(height=350)
            st.plotly_chart(fig_hist, use_container_width=True)

        st.divider()
        st.subheader("Customer Priority List")
        st.markdown("*Sorted by Priority Score — who to contact first:*")

        display_cols = [
            'Churn_Probability', 'Risk_Level', 'Health_Score',
            'Priority_Score', 'AnnualRevenue', 'Recommended_Action'
        ]
        priority_df = results[display_cols].sort_values(
            'Priority_Score', ascending=False
        ).reset_index(drop=True)
        priority_df.index += 1
        st.dataframe(priority_df, use_container_width=True)

        st.divider()
        st.subheader("Download Results")

        csv_output = results.to_csv(index=False)
        st.download_button(
            label="Download Full Predictions as CSV",
            data=csv_output,
            file_name="churn_predictions.csv",
            mime="text/csv"
        )

        high_risk_df = results[results['Risk_Level'] == 'HIGH RISK']
        if len(high_risk_df) > 0:
            csv_high = high_risk_df.to_csv(index=False)
            st.download_button(
                label="Download HIGH RISK Customers Only",
                data=csv_high,
                file_name="high_risk_customers.csv",
                mime="text/csv"
            )
            st.warning(str(len(high_risk_df)) + " HIGH RISK customers need immediate attention!")

else:
    st.info("Upload a CSV file to get started!")

    st.subheader("Required CSV Columns")
    required_cols = pd.DataFrame({
        'Column': [
            'Tenure', 'PreferredLoginDevice', 'CityTier',
            'WarehouseToHome', 'PreferredPaymentMode', 'Gender',
            'HourSpendOnApp', 'NumberOfDeviceRegistered', 'PreferedOrderCat',
            'SatisfactionScore', 'MaritalStatus', 'NumberOfAddress',
            'Complain', 'OrderAmountHikeFromlastYear', 'CouponUsed',
            'OrderCount', 'DaySinceLastOrder', 'CashbackAmount', 'AnnualRevenue'
        ],
        'Type': [
            'int', 'int (0-2)', 'int (1-3)', 'int', 'int (0-6)',
            'int (0/1)', 'int (0-5)', 'int (1-6)', 'int (0-5)',
            'int (1-5)', 'int (0-2)', 'int', 'int (0/1)',
            'int (11-26)', 'int', 'int', 'int', 'float', 'float'
        ],
        'Example': [
            1, 2, 3, 30, 1, 1, 1, 2, 3,
            1, 2, 2, 1, 11, 0, 1, 20, 50.0, 5000
        ]
    })
    st.table(required_cols.set_index('Column'))

st.divider()
st.markdown(
    "<div style='text-align: center; color: gray; padding: 10px;'>"
    "Built by <b>Amruth</b> | Python XGBoost SHAP Streamlit | "
    "<a href='https://github.com/Amruth011/customer-churn-prediction-retention-roi' target='_blank'>GitHub</a>"
    "</div>",
    unsafe_allow_html=True
)