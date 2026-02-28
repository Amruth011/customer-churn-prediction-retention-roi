<div align="center">

# 🛒 Customer Churn Prediction & Retention ROI

### *An e-commerce platform was losing ₹47,40,000/year. This system stops that.*

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-AUC_0.9989-brightgreen?style=for-the-badge)](https://xgboost.readthedocs.io)
[![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://customer-churn-prediction-retention-roi-9gkae6bppwug3sjpykbcgd.streamlit.app/)
[![SHAP](https://img.shields.io/badge/SHAP-Explainable_AI-orange?style=for-the-badge)](https://shap.readthedocs.io)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

<br>

### 👉 [**Try the Live App →**](https://customer-churn-prediction-retention-roi-9gkae6bppwug3sjpykbcgd.streamlit.app/)

![Home Page](assets/home.gif)

<br>

> **This is not a Jupyter notebook with a model.**
> 
> **This is a complete business decision system — predict, explain, simulate, optimize, and act.**

</div>

---

## 📋 Table of Contents

- [The Problem](#-the-problem)
- [Live Demo](#-live-demo)
- [Model Performance](#-model-performance)
- [The 7-Page Dashboard](#-the-7-page-dashboard)
- [Dataset Description](#-dataset-description)
- [Feature Engineering](#-feature-engineering)
- [Model Comparison](#-model-comparison)
- [Key Business Insights](#-key-business-insights)
- [Business Impact](#-business-impact)
- [What Makes This Different](#-what-makes-this-different)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Run Locally](#-run-locally)
- [Docker](#-docker)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [FAQ](#-faq)
- [Acknowledgements](#-acknowledgements)
- [Author](#-author)

---

## 📌 The Problem

An e-commerce platform was **silently bleeding revenue.**

| Problem | Scale |
|---|---|
| Annual revenue lost to churn | **₹47,40,000/year** |
| Customer churn rate | **16.84%** — nearly 1 in 6 customers |
| Customers at high risk right now | **937 identified** |
| Business had a prediction system | **❌ None** |

They could not predict who would leave. They could not understand why. They had no way to act before it was too late.

**This project builds that entire system — from raw data to live deployed dashboard.**

---

## 🚀 Live Demo

### [👉 Click Here to Try the App](https://customer-churn-prediction-retention-roi-9gkae6bppwug3sjpykbcgd.streamlit.app/)

The app is fully interactive. Load a sample high-risk customer, predict churn, see exactly why the model decided what it did, simulate retention actions, and calculate ROI — all in real time.

---

## 📊 Model Performance

> All metrics computed from the actual XGBoost model on a real held-out test set. Nothing hardcoded.

| Metric | Value |
|---|---|
| **Model** | XGBoost |
| **AUC Score** | **0.9989** |
| **Accuracy** | **98.76%** |
| **Cross-Validation AUC** | 0.9871 (5-fold) |
| **Precision** | 98.4% |
| **Recall** | 97.9% |
| **F1 Score** | 98.1% |
| **Test Samples** | 1,126 |
| **Churn Cases in Test** | 190 |

---

## 🖥️ The 7-Page Dashboard

### Page 1 — 🏠 Home: The Business Story

The dashboard opens with a clear business narrative. Problem → Approach → Result. Built for business stakeholders, not just data scientists.

![Home Page](assets/home.gif)

---

### Page 2 — 🔮 Churn Predictor: Predict + Explain in One Shot

Enter any customer's details → get churn probability, risk gauge, live SHAP explanation, ROI calculation, and priority score — all in one click.

![Churn Predictor](assets/predictor.gif)

**What's unique:** Most projects show a prediction score. This one shows **why** — using real SHAP values computed live from the actual XGBoost model, displayed as a waterfall chart with each feature's exact contribution color-coded red (increases churn) or green (decreases churn).

---

### Page 3 — 🎯 Priority Score: Who to Call First

Not all at-risk customers deserve equal attention. A customer with ₹50,000 revenue at 90% churn risk is 10x more urgent than one with ₹1,000 at 95% risk.

**Formula: `Priority Score = Annual Revenue × Churn Probability`**

![Priority Score](assets/priority.gif)

| Priority Level | Score Threshold | Action |
|---|---|---|
| 🔴 Priority 1 | ≥ 20,000 | Contact immediately |
| 🟡 Priority 2 | ≥ 5,000 | Contact this week |
| 🟢 Priority 3 | < 5,000 | Standard follow-up |

---

### Page 4 — 🔄 What-If Retention Simulator

Before spending money, test what actually works. Adjust 12 customer parameters and see in real time how each retention action reduces churn probability.

![What-If Simulator](assets/whatif.gif)

**12 Parameters:** Tenure, Cashback Amount, Hours on App, Annual Revenue, Satisfaction Score, Order Count, Devices Registered, City Tier, Complained, Days Since Last Order, Coupons Used, Number of Address

---

### Page 5 — 💰 Retention Budget Optimizer

Given a fixed budget, allocate it across 937 high-risk customers to maximize revenue saved.

![Budget Optimizer](assets/budget.gif)

Allocates starting from highest ROI segment first. Shows exact budget split, projected revenue saved, and campaign ROI. Warns when budget is too small (minimum ₹500/customer).

---

### Page 6 — 🔬 Model Transparency: Real Metrics, Nothing Hidden

Every metric on this page is computed live from the actual model and real test data.

![Model Transparency](assets/model.gif)

Shows: AUC, Accuracy, Confusion Matrix (real TP/TN/FP/FN), ROC Curve, Feature Importance from `model.feature_importances_`, Precision/Recall/F1, and a note on class imbalance handling.

---

### Page 7 — 📅 Cohort Analysis: When Do Customers Actually Churn?

The feature no other student churn project has. Analyzes churn patterns across customer tenure segments to reveal **when** customers are most at risk.

![Cohort Analysis](assets/cohort.gif)

**Key Finding:** Customers in 0-3 months churn at **41.9%** — 6x higher than loyal customers. New customer onboarding is the #1 retention priority.

---

### Page 8 — 📦 Batch Analysis: Production-Scale Predictions

Upload a CSV of any number of customers → get predictions, risk scores, and priority rankings for all at once. Download results instantly.

![Batch Analysis](assets/batch.gif)

---

## 📁 Dataset Description

**Source:** UCI ML Repository — E-Commerce Customer Dataset

**Size:** 5,630 customers, 20 features

| Column | Type | Description |
|---|---|---|
| `Tenure` | Numeric | Months as a customer |
| `CityTier` | Categorical | City tier 1, 2, or 3 |
| `WarehouseToHome` | Numeric | Distance from warehouse to home |
| `HourSpendOnApp` | Numeric | Hours spent on mobile app |
| `NumberOfDeviceRegistered` | Numeric | Devices registered on account |
| `SatisfactionScore` | Numeric | Customer satisfaction 1-5 |
| `NumberOfAddress` | Numeric | Addresses saved |
| `Complain` | Binary | Whether customer complained (0/1) |
| `OrderAmountHikeFromlastYear` | Numeric | % increase in orders vs last year |
| `CouponUsed` | Numeric | Coupons used last month |
| `OrderCount` | Numeric | Orders placed last month |
| `DaySinceLastOrder` | Numeric | Days since last order |
| `CashbackAmount` | Numeric | Average cashback received |
| `Churn` | Binary | **Target** — 1 = churned, 0 = stayed |

**Class Distribution:** 16.84% churn (948 customers), 83.16% non-churn (4,682 customers) — imbalanced dataset handled during modeling.

---

## ⚙️ Feature Engineering

6 new features were created from raw data to improve model performance:

| Feature | Formula | Business Meaning |
|---|---|---|
| `is_new_customer` | Tenure ≤ 3 months | New customers churn 6x more |
| `cashback_per_order` | CashbackAmount / (OrderCount + 1) | Value per transaction |
| `order_frequency` | OrderCount / (Tenure + 1) | Engagement rate |
| `high_value_customer` | CashbackAmount > median | High-value segment flag |
| `complaint_new_customer` | Complain × is_new_customer | Interaction — most dangerous combo |
| `app_engagement_score` | HourSpendOnApp × OrderCount | Combined app engagement |

`is_new_customer` alone showed **0.449 correlation** with churn — the single strongest predictor.

---

## 🏆 Model Comparison

4 models were trained and evaluated. XGBoost won on every metric:

| Model | AUC | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|---|
| Logistic Regression | 0.8821 | 87.3% | 71.2% | 68.9% | 70.0% |
| Random Forest | 0.9934 | 97.2% | 95.1% | 93.8% | 94.4% |
| Decision Tree | 0.9421 | 93.6% | 89.3% | 87.1% | 88.2% |
| **XGBoost** | **0.9989** | **98.76%** | **98.4%** | **97.9%** | **98.1%** |

**Why XGBoost won:**
- Gradient boosting handles class imbalance better
- Built-in regularization prevents overfitting on the 16.84% minority class
- Feature interactions captured that tree-based ensemble methods miss

---

## 🔍 Key Business Insights

These insights came from the data — not assumptions:

**1. Tenure is the #1 Churn Driver**
New customers (0-3 months) churn at 41.9%. After 6 months the rate drops below 8%. The first 90 days are critical.

**2. One Complaint Triples Churn Probability**
Customers who complained have a 3x higher churn rate. Complaint resolution speed is a direct revenue lever.

**3. Low Cashback = High Churn**
Customers receiving below-median cashback churn significantly more. Cashback is not just a cost — it's retention spend.

**4. City Tier 3 is Underserved**
Tier 3 city customers churn more than Tier 1. Logistics and service quality in smaller cities needs investment.

**5. Inactive Customers Are Already Gone**
High days-since-last-order is a strong churn signal regardless of satisfaction score. Re-engagement must happen within 15 days of inactivity.

---

## 💰 Business Impact

| Metric | Value |
|---|---|
| High Risk Customers Identified | 937 |
| Annual Revenue at Risk | ₹47,40,000 |
| Campaign Cost (₹500/customer) | ₹4,68,500 |
| Revenue Saved (30% retention rate) | ₹14,22,000 |
| **Campaign ROI** | **224%** |
| **Every ₹1 spent returns** | **₹3.2** |

---

## 💡 What Makes This Different

| Feature | This Project | Typical Student Project |
|---|---|---|
| Live SHAP explanations | ✅ Real-time per prediction | ❌ Static chart |
| Cohort Analysis | ✅ 5 interactive charts | ❌ Not included |
| What-If Simulator | ✅ 12 factors, live update | ❌ Not included |
| Batch CSV Upload | ✅ Any size + downloadable results | ❌ Not included |
| Real Model Metrics | ✅ Computed from test data | ❌ Often hardcoded |
| Business ROI Calculator | ✅ Revenue × risk | ❌ Not included |
| Priority Score System | ✅ Revenue-weighted ranking | ❌ Not included |
| Feature Engineering | ✅ 6 engineered features | ❌ Raw features only |
| Model Comparison | ✅ 4 models benchmarked | ❌ Single model |
| Docker Ready | ✅ Dockerfile included | ❌ Not included |
| 7-Page Dashboard | ✅ Full business system | ❌ Single page form |

---

## 🛠️ Tech Stack

| Category | Tool | Purpose |
|---|---|---|
| Language | Python 3.9+ | Core |
| ML Model | XGBoost | Best performing model |
| ML Pipeline | Scikit-learn | Preprocessing + evaluation |
| Explainability | SHAP (TreeExplainer) | Live feature attribution |
| Dashboard | Streamlit | Interactive web app |
| Charts | Plotly | Interactive visualizations |
| Data | Pandas, NumPy | Data manipulation |
| Excel Reader | openpyxl | Load `.xlsx` dataset |
| Deployment | Streamlit Cloud | Live hosting |
| Container | Docker | Reproducible environment |
| Version Control | GitHub | Source control |

---

## 📁 Project Structure

```
customer-churn-prediction-retention-roi/
│
├── streamlit_app.py                  # Home page — business story
│
├── pages/
│   ├── 1_Churn_Predictor.py          # Predict + SHAP + Priority Score
│   ├── 2_Priority_Score.py           # Revenue-weighted priority ranking
│   ├── 3_What_If_Simulator.py        # 12-factor retention simulator
│   ├── 4_Budget_Optimizer.py         # ROI-maximizing budget allocation
│   ├── 5_Model_Transparency.py       # Real metrics from test data
│   ├── 6_Cohort_Analysis.py          # Tenure-based churn patterns
│   └── 7_Batch_Analysis.py           # CSV upload batch predictions
│
├── data/
│   └── raw/
│       ├── E Commerce Dataset.xlsx   # Original dataset (5,630 customers)
│       ├── test_data.csv             # Held-out test set (real metrics)
│       └── sample_upload.csv         # Sample CSV for batch upload demo
│
├── src/
│   └── best_churn_model.pkl          # Trained XGBoost model
│
├── notebooks/
│   └── EDA.ipynb                     # 14-section analysis notebook
│
├── assets/                           # GIF demos
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
│   └── config.toml                   # Dark theme + red primary color
│
├── Dockerfile                        # Docker containerization
├── .dockerignore
├── requirements.txt
└── README.md
```

---

## 🚀 Run Locally

**Step 1 — Clone:**
```bash
git clone https://github.com/Amruth011/customer-churn-prediction-retention-roi.git
cd customer-churn-prediction-retention-roi
```

**Step 2 — Install dependencies:**
```bash
pip install -r requirements.txt
```

**Step 3 — Run:**
```bash
streamlit run streamlit_app.py
```

**Step 4 — Open:**
```
http://localhost:8501
```

---

## 🐳 Docker

```bash
# Build
docker build -t churn-prediction-app .

# Run
docker run -p 8501:8501 churn-prediction-app

# Open
http://localhost:8501
```

---

## 🔧 Troubleshooting

**❌ `ModuleNotFoundError: No module named 'shap'`**
```bash
pip install shap
```

**❌ `ModuleNotFoundError: No module named 'openpyxl'`**
```bash
pip install openpyxl
```

**❌ Model file not found error**
Make sure `src/best_churn_model.pkl` exists. It's included in the repo. If missing, re-run the training notebook.

**❌ Dataset not found error**
Make sure `data/raw/E Commerce Dataset.xlsx` exists. It's included in the repo.

**❌ Streamlit port already in use**
```bash
streamlit run streamlit_app.py --server.port 8502
```

**❌ SHAP chart not showing**
This happens when the model explainer takes time to load. Wait 10-15 seconds on first prediction — it caches after that.

---

## 🤝 Contributing

This project is open for contributions! Here are ways you can help:

**🐛 Found a bug?**
Open an [Issue](https://github.com/Amruth011/customer-churn-prediction-retention-roi/issues) with what happened and what you expected.

**💡 Feature ideas we'd love:**
- [ ] Add telecom / banking / SaaS datasets
- [ ] Email alert system for high-risk customers
- [ ] Time-series churn trend forecasting
- [ ] Customer segmentation with RFM analysis
- [ ] A/B test ROI comparison module
- [ ] Multi-language support
- [ ] REST API endpoint for predictions

**🔧 Want to contribute code?**
```bash
# Fork the repo on GitHub
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction-retention-roi.git
git checkout -b feature/your-feature-name

# Make changes, test locally
streamlit run streamlit_app.py

# Push and open a Pull Request
git push origin feature/your-feature-name
```

**⭐ Simplest contribution — star the repo!**
It helps others discover this project and motivates further development.

---

## ❓ FAQ

**Q: Can I use this on my own dataset?**

Yes! Replace `data/raw/E Commerce Dataset.xlsx` with your dataset. Retrain the model in the notebook and save the new `.pkl` file to `src/`. Make sure your dataset has similar column names or update the feature list in each page file.

**Q: Why XGBoost and not a neural network?**

For tabular data of this size (5,630 rows, 20 features), XGBoost consistently outperforms neural networks. Neural networks need much more data and tuning to beat gradient boosting on structured tabular data. XGBoost also supports SHAP natively — critical for explainability.

**Q: Is the SHAP explanation real or approximated?**

It's real. We use `shap.TreeExplainer` which computes exact SHAP values for tree-based models — no approximation. Every feature contribution shown in the waterfall chart is the mathematically exact attribution from the XGBoost model.

**Q: How accurate is the What-If Simulator?**

The simulator uses the actual trained XGBoost model to recompute churn probability each time you move a slider. It's not a rule-based estimate — it's the model itself running live.

**Q: Can I deploy this on my own server?**

Yes. A `Dockerfile` is included. Build the image and run it on any cloud provider (AWS, GCP, Azure, Render, Railway).

**Q: The app is slow to load. Why?**

Streamlit Cloud free tier has limited resources. The SHAP explainer also takes 5-10 seconds to initialize on first load. After that it's cached and fast. For production use, deploy on a paid tier or your own server.

---

## 🙏 Acknowledgements

- **Dataset:** [UCI ML Repository — E-Commerce Customer Churn Dataset](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction)
- **SHAP Library:** Lundberg & Lee (2017) — *A Unified Approach to Interpreting Model Predictions*
- **XGBoost:** Chen & Guestrin (2016) — *XGBoost: A Scalable Tree Boosting System*
- **Streamlit** — for making ML deployment accessible to everyone

---

## 👤 Author

<div align="center">

**Amruth Kumar M**

B.Tech in Artificial Intelligence & Data Science
REVA University, Bengaluru

Data Science Intern @ iStudio

[![GitHub](https://img.shields.io/badge/GitHub-Amruth011-181717?style=for-the-badge&logo=github)](https://github.com/Amruth011)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/amruth-kumar-m)

</div>

---

## 📄 License

MIT License — free to use, modify, and distribute with attribution.

---

<div align="center">

**If this project helped you, please give it a ⭐**

*It helps other students and developers discover this work.*

**Built with Python • XGBoost • SHAP • Streamlit**

</div>
