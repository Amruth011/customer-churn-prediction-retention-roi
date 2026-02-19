# 🛒 Customer Churn Prediction & Retention ROI Analysis

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![XGBoost](https://img.shields.io/badge/XGBoost-AUC%200.9989-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)
![MIT License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Live Demo
👉 **[Click here to try the live app](https://customer-churn-prediction-retention-roi-9gkae6bppwug3sjpykbcgd.streamlit.app/)**

---

## 📋 Business Problem
An e-commerce platform is losing **₹47,40,000/year** due to **16.84% customer churn rate**.

**Goal:** Predict which customers will churn next quarter & recommend targeted retention strategies to save **₹14,25,000/year**.

---

## ❓ Key Business Questions
1. Which customers are most likely to churn?
2. What are the main drivers of churn?
3. What retention strategies should we use for different segments?
4. What is the ROI of our retention campaigns?

---

## 📊 Results

| Metric | Result |
|---|---|
| Total Customers | 5,630 |
| Churn Rate | 16.84% |
| Best Model | XGBoost |
| AUC Score | 0.9989 |
| Cross Validation AUC | 0.9871 |
| Accuracy | 98.76% |
| High Risk Customers | 937 |
| Revenue Saved | ₹14,25,000 |
| Campaign ROI | ~200% |

---

## 🔍 Key Insights (SHAP)
- **Tenure** is #1 churn driver — new customers leave the fastest
- **Complaints** increase churn probability by 3x
- **Low cashback** customers are more likely to churn
- **Engineered feature** `is_new_customer` showed 0.449 correlation with churn

---

## 🛠️ Tech Stack
- **Python** — Core language
- **Pandas & NumPy** — Data manipulation
- **Matplotlib & Seaborn** — Visualizations
- **Scikit-learn** — ML pipeline
- **XGBoost** — Best performing model
- **SHAP** — Model explainability
- **Streamlit** — Interactive dashboard
- **GitHub** — Version control

---

## 📁 Project Structure
```
customer-churn-prediction-retention-roi/
│
├── data/
│   └── raw/                    # Raw dataset
├── notebooks/
│   └── EDA.ipynb               # Complete analysis notebook
├── src/
│   └── best_churn_model.pkl    # Trained XGBoost model
├── reports/
│   └── figures/                # Saved visualizations
├── streamlit_app.py            # Live dashboard
├── requirements.txt            # Dependencies
└── README.md
```

---

## 🚀 How to Run Locally
```bash
# Clone repo
git clone https://github.com/Amruth011/customer-churn-prediction-retention-roi.git
cd customer-churn-prediction-retention-roi

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run streamlit_app.py
```

---

## 💰 Business Impact
By targeting **937 high-risk customers** with personalized retention campaigns:

- Campaign Cost: **₹4,68,500**
- Revenue Saved: **₹14,05,000**
- **ROI: 200%** — Every ₹1 spent returns ₹3

---

## 👤 Author
**Amruth** — Data Science Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-Amruth011-black)](https://github.com/Amruth011)
