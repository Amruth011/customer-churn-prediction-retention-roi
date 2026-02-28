# 🛒 Customer Churn Prediction & Retention ROI

> **End-to-End ML System to Predict, Explain & Prevent Customer Churn**
> 
> *Not just a model. A complete business decision system.*

[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://python.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-AUC%200.9989-brightgreen)](https://xgboost.readthedocs.io)
[![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)](https://customer-churn-prediction-retention-roi-9gkae6bppwug3sjpykbcgd.streamlit.app/)
[![SHAP](https://img.shields.io/badge/SHAP-Explainable%20AI-orange)](https://shap.readthedocs.io)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 🚀 Live Demo

### 👉 [Try the Live App](https://customer-churn-prediction-retention-roi-9gkae6bppwug3sjpykbcgd.streamlit.app/)

![Home Page](assets/home.gif)

---

## 📌 The Problem

An e-commerce platform was silently losing **₹47,40,000 every year**.

The churn rate was **16.84%** — nearly 1 in 6 customers leaving — and the business had **no system** to:
- Predict who will leave before they do
- Understand **why** they leave
- Act before it's too late

This project builds that system from scratch.

---

## 🎯 What This Project Does

| Stage | What Happens |
|---|---|
| **Data** | 5,630 e-commerce customers analyzed |
| **Engineering** | 6 new features engineered from raw data |
| **Modeling** | 4 ML models tested, XGBoost selected |
| **Explainability** | Live SHAP explanations for every prediction |
| **Business** | ROI calculator, budget optimizer, priority scoring |
| **Deployment** | 7-page interactive Streamlit dashboard, live on the web |

---

## 📊 Model Performance

| Metric | Value |
|---|---|
| Model | XGBoost |
| AUC Score | **0.9989** |
| Accuracy | **98.76%** |
| Cross-Validation AUC | 0.9871 |
| Test Samples | 1,126 |
| Churn Cases Detected | 190 |

> All metrics computed from real model + real test data. Nothing hardcoded.

---

## 🖥️ The 7-Page Dashboard

### 1. 🏠 Home — The Story

The dashboard opens with a business narrative: Problem → Approach → Result. Not a raw ML dump — a story a business stakeholder can immediately understand.

![Home Page](assets/home.gif)

---

### 2. 🔮 Churn Predictor — Predict + Explain in One Shot

Enter any customer's details → get churn probability, risk gauge, live SHAP explanation, ROI calculation, and priority score — all in one click.

**What makes this different:** Most projects stop at a prediction score. This one tells you **why** the model predicted what it did, using real SHAP values computed live from the actual XGBoost model.

![Churn Predictor](assets/predictor.gif)

**Features:**
- Load Sample HIGH RISK customer button for instant demo
- Churn probability gauge (0–100%)
- Live SHAP waterfall chart — top 10 features color-coded red/green
- ROI calculator — revenue at risk in rupees
- Priority Score — who to call first based on revenue × churn probability

---

### 3. 🎯 Customer Priority Score — Who to Call First

Not all churning customers are equal. A customer with ₹50,000 annual revenue at 90% churn risk is more urgent than one with ₹1,000 revenue at 95% risk.

**Formula: Priority Score = Annual Revenue × Churn Probability**

![Priority Score](assets/priority.gif)

**Priority Levels:**
- 🔴 Priority 1 (Score ≥ 20,000) — Contact immediately
- 🟡 Priority 2 (Score ≥ 5,000) — Contact this week
- 🟢 Priority 3 (Score < 5,000) — Standard follow-up

---

### 4. 🔄 What-If Retention Simulator — Simulate Before You Act

Before spending money on retention, test what actually works. Adjust 12 customer parameters and see in real-time how each retention action reduces churn probability.

![What-If Simulator](assets/whatif.gif)

**12 Parameters:**
Tenure, Cashback Amount, Hours on App, Annual Revenue, Satisfaction Score, Order Count, Devices Registered, City Tier, Complained, Days Since Last Order, Coupons Used, Number of Address

**Output:** Before vs After churn probability comparison with best action recommendation.

---

### 5. 💰 Retention Budget Optimizer — Maximize ROI

Given a fixed budget, how do you allocate it across 937 high-risk customers to get maximum revenue saved?

![Budget Optimizer](assets/budget.gif)

**How it works:**
- Allocates budget starting from highest ROI segment first
- Shows exact budget split: High Risk vs Medium Risk
- Calculates projected revenue saved and campaign ROI
- Shows what happens if budget is too small (minimum ₹500 per customer warning)

---

### 6. 🔬 Model Transparency — Real Metrics, Nothing Hidden

Every metric on this page is computed live from the actual XGBoost model and real test data. Nothing is hardcoded.

![Model Transparency](assets/model.gif)

**What's shown:**
- AUC: 0.9989, Accuracy: 98.76% (from 1,126 test samples)
- ROC Curve with actual FPR/TPR values
- Confusion Matrix (real TP, TN, FP, FN counts)
- Feature Importance from `model.feature_importances_`
- Precision, Recall, F1 from classification report
- Class imbalance note — model handles 16.84% minority class

---

### 7. 📅 Cohort Analysis — When Do Customers Actually Churn?

This is the feature no other student churn project has. Instead of just predicting individual customers, this page analyzes churn patterns across customer segments.

![Cohort Analysis](assets/cohort.gif)

**Key Finding from Real Data:**
- Customers in **0-3 months tenure** churn at **41.9%**
- Customers in **3-6 months** drop to **7.5%**
- Customers in **6-12 months** drop to **5.7%**
- Loyal customers (24+ months) churn at only **~2%**

This means **new customer onboarding is the #1 retention priority** — a finding that changes business strategy.

**5 Charts:**
- Churn Rate by Tenure Group
- Complaint Impact by Tenure
- Satisfaction vs Churn Rate
- Cashback by Tenure and Churn Status
- City Tier Churn Analysis

---

### 8. 📦 Batch Customer Analysis — Production-Scale Predictions

Upload a CSV of any number of customers → get predictions, risk scores, and priority rankings for all of them at once. Download results instantly.

![Batch Analysis](assets/batch.gif)

**Features:**
- Download sample CSV template
- Upload your own customer data (any size)
- Batch prediction with churn probability for every customer
- Risk distribution pie chart
- Churn probability histogram
- Priority-sorted results table
- Download full results as CSV
- Download HIGH RISK customers only as separate CSV
- Revenue at risk calculation across entire batch

---

## 🔍 Key Business Insights from the Data

1. **Tenure is #1 churn driver** — New customers (0-3 months) churn 6x more than loyal customers
2. **Complaints 3x churn probability** — One unresolved complaint dramatically increases risk
3. **Low cashback = high churn** — Customers receiving less cashback leave faster
4. **City Tier 3 customers** have higher churn than Tier 1 — underserved markets need attention
5. **Inactive customers** (high days since last order) are at elevated risk regardless of satisfaction

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.9+ |
| ML Model | XGBoost, Scikit-learn |
| Explainability | SHAP (TreeExplainer) |
| Dashboard | Streamlit |
| Data | Pandas, NumPy |
| Visualization | Plotly (interactive charts) |
| Data Source | openpyxl (Excel reader) |
| Deployment | Streamlit Cloud |
| Containerization | Docker |
| Version Control | GitHub |

---

## 📁 Project Structure

```
customer-churn-prediction-retention-roi/
│
├── streamlit_app.py              # Home page — business story
├── pages/
│   ├── 1_Churn_Predictor.py      # Predict + SHAP + Priority Score
│   ├── 2_Priority_Score.py       # Revenue-weighted priority ranking
│   ├── 3_What_If_Simulator.py    # 12-factor retention simulator
│   ├── 4_Budget_Optimizer.py     # ROI-maximizing budget allocation
│   ├── 5_Model_Transparency.py   # Real metrics from test data
│   ├── 6_Cohort_Analysis.py      # Tenure-based churn patterns
│   └── 7_Batch_Analysis.py       # CSV upload batch predictions
│
├── data/
│   └── raw/
│       ├── E Commerce Dataset.xlsx   # Original dataset
│       ├── test_data.csv             # Held-out test set (for real metrics)
│       └── sample_upload.csv         # Sample CSV for batch upload demo
│
├── src/
│   └── best_churn_model.pkl      # Trained XGBoost model
│
├── notebooks/
│   └── EDA.ipynb                 # 14-section analysis notebook
│
├── assets/                       # GIF demos for README
│   ├── home.gif
│   ├── predictor.gif
│   ├── priority.gif
│   ├── whatif.gif
│   ├── budget.gif
│   ├── model.gif
│   ├── cohort.gif
│   └── batch.gif
│
├── .streamlit/
│   └── config.toml               # Dark theme + red primary color
│
├── Dockerfile                    # Docker containerization
├── .dockerignore
├── requirements.txt
└── README.md
```

---

## 🚀 Run Locally

**Clone and install:**
```bash
git clone https://github.com/Amruth011/customer-churn-prediction-retention-roi.git
cd customer-churn-prediction-retention-roi
pip install -r requirements.txt
```

**Run:**
```bash
streamlit run streamlit_app.py
```

Open `http://localhost:8501`

---

## 🐳 Docker

```bash
docker build -t churn-prediction-app .
docker run -p 8501:8501 churn-prediction-app
```

Open `http://localhost:8501`

---

## 📈 Business Impact

By targeting **937 high-risk customers** with data-driven retention campaigns:

| Metric | Value |
|---|---|
| High Risk Customers Identified | 937 |
| Annual Revenue at Risk | ₹47,40,000 |
| Campaign Cost (₹500/customer) | ₹4,68,500 |
| Revenue Saved (30% retention rate) | ₹14,22,000 |
| **Campaign ROI** | **224%** |
| **Every ₹1 spent returns** | **₹3.2** |

---

## 💡 What Makes This Different from Other Churn Projects

| Feature | This Project | Typical Student Project |
|---|---|---|
| Live SHAP explanations | ✅ Real-time per prediction | ❌ Static feature importance chart |
| Cohort Analysis | ✅ 5 interactive charts | ❌ Not included |
| What-If Simulator | ✅ 12 factors, live update | ❌ Not included |
| Batch CSV Upload | ✅ Any size, downloadable results | ❌ Not included |
| Real Model Metrics | ✅ Computed from test data | ❌ Often hardcoded |
| Business ROI Calculator | ✅ Revenue × risk thinking | ❌ Not included |
| Priority Score System | ✅ Revenue-weighted ranking | ❌ Not included |
| Docker Ready | ✅ Dockerfile included | ❌ Not included |
| 7-Page Dashboard | ✅ Full business system | ❌ Single page form |

---

## 👤 Author

**Amruth Kumar M**  
B.Tech AI & Data Science — REVA University, Bengaluru  
Data Science Intern @ iStudio

[![GitHub](https://img.shields.io/badge/GitHub-Amruth011-black)](https://github.com/Amruth011)

---

## 📄 License

MIT License — free to use, modify and distribute.

---

*Built with Python, XGBoost, SHAP, and Streamlit*
