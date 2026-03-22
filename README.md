<div align="center">

# Customer Churn Prediction & Retention ROI

### *Most ML projects predict. This one prevents — and proves the business case.*

<br/>

[![Live App](https://img.shields.io/badge/🚀%20Live%20App-Try%20It%20Now-7C3AED?style=for-the-badge)](https://customer-churn-prediction-retention-roi-9gkae6bppwug3sjpykbcgd.streamlit.app/)
[![AUC Score](https://img.shields.io/badge/AUC-0.9989-22c55e?style=for-the-badge)](https://customer-churn-prediction-retention-roi-9gkae6bppwug3sjpykbcgd.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-Champion_Model-FF6600?style=for-the-badge)](https://xgboost.readthedocs.io)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)

<br/>

> A single data scientist built a complete churn intelligence system —  
> predicts who leaves, explains why, simulates every fix, and optimizes spend.  
> **End-to-end. Live. Production-grade.**

<br/>

<img src="assets/home.gif" width="100%" style="border-radius:12px;" />

<br/><br/>

</div>

---

## The Business Problem

An e-commerce platform was losing **₹47,40,000 every year** to churn — silently, with no system to detect it.

| Problem | Reality |
|---|---|
| Annual revenue lost to churn | **₹47,40,000** |
| Customers at high risk *right now* | **937 identified** |
| Churn rate | **16.84%** — nearly 1 in 6 customers |
| Did they have a prediction system? | **None.** |

This project builds that system from scratch — raw Excel data to a live, deployed, 8-page business dashboard.

---

## Results at a Glance

| Metric | Value |
|---|---|
| Model | XGBoost (4 benchmarked) |
| **AUC-ROC** | **0.9989** |
| **Accuracy** | **98.76%** |
| Cross-Val AUC | 0.9871 (5-fold) |
| Precision / Recall / F1 | 98.4% / 97.9% / 98.1% |
| High-risk customers surfaced | **937** |
| Annual revenue protected | **₹47,40,000** |
| Campaign ROI proven | **224%** — every ₹1 returns ₹3.20 |

---

## Live Demo

**[👉 Open the App](https://customer-churn-prediction-retention-roi-9gkae6bppwug3sjpykbcgd.streamlit.app/)** — no setup, fully interactive.

Load a high-risk customer profile → see the churn prediction → read the SHAP explanation → simulate retention actions → calculate ROI. All in real time.

---

## The 8-Page Dashboard

---

### 🏠 Page 1 — Home: The Business Story

Built for business stakeholders, not just data scientists. Opens with a clear problem → approach → result narrative so anyone walking in understands the stakes in 30 seconds.

![Home Page](assets/home.gif)

---

### 🔮 Page 2 — Churn Predictor: Predict + Explain in One Shot

Enter any customer's details → get churn probability, risk gauge, live SHAP waterfall explanation, and priority score — all in one click.

![Churn Predictor](assets/predictor.gif)

> **What's unique:** Most projects show a score. This one shows *why* — real SHAP values computed live from the XGBoost model, color-coded red (pushes toward churn) or green (pushes away from churn), with each feature's exact contribution.

---

### 🎯 Page 3 — Priority Score: Who to Call First

Not all at-risk customers deserve equal attention. A customer with ₹50,000 revenue at 90% churn risk is 10× more urgent than one at ₹1,000 with 95% risk.

**Formula: `Priority Score = Annual Revenue × Churn Probability`**

![Priority Score](assets/priority.gif)

| Priority Level | Score | Action |
|---|---|---|
| 🔴 Priority 1 | ≥ 20,000 | Contact immediately |
| 🟡 Priority 2 | ≥ 5,000 | Contact this week |
| 🟢 Priority 3 | < 5,000 | Standard follow-up |

---

### 🔄 Page 4 — What-If Retention Simulator

Before spending money, test what actually works. Adjust 12 customer parameters and see in real time how each retention action changes churn probability.

![What-If Simulator](assets/whatif.gif)

**12 Parameters:** Tenure · Cashback Amount · Hours on App · Annual Revenue · Satisfaction Score · Order Count · Devices Registered · City Tier · Complained · Days Since Last Order · Coupons Used · Number of Addresses

---

### 💰 Page 5 — Retention Budget Optimizer

Given a fixed budget, allocate it across the 937 high-risk customers to maximize total revenue saved — starting from the highest-ROI segment first.

![Budget Optimizer](assets/budget.gif)

> Shows exact budget split, projected revenue saved, and campaign ROI. Warns when budget is below the ₹500/customer minimum threshold.

---

### 🔬 Page 6 — Model Transparency: Real Metrics, Nothing Hidden

Every number on this page is computed live from the actual model on real held-out test data. No hardcoding, no cherry-picking.

![Model Transparency](assets/model.gif)

Shows: AUC · Accuracy · Confusion Matrix (real TP/TN/FP/FN) · ROC Curve · Feature Importance · Precision / Recall / F1 · Class imbalance handling note.

---

### 📅 Page 7 — Cohort Analysis: When Do Customers Actually Churn?

The feature no other student churn project has. Analyzes churn patterns across customer tenure segments to reveal *when* customers are most at risk.

![Cohort Analysis](assets/cohort.gif)

> **Key Finding:** Customers in the 0–3 month window churn at **41.9%** — 6× higher than loyal customers. New customer onboarding is the #1 retention priority.

---

### 📦 Page 8 — Batch Analysis: Production-Scale Predictions

Upload a CSV of any number of customers → get predictions, risk scores, and priority rankings for all of them at once. Download results instantly.

![Batch Analysis](assets/batch.gif)

---

## Key Findings

**1. The first 90 days are everything.**
New customers (0–3 months) churn at **41.9%** — 6× higher than loyal customers. Onboarding is the #1 retention lever.

**2. One complaint triples churn risk.**
Customers who complained have 3× higher churn probability. Complaint resolution speed is a direct revenue lever.

**3. Low cashback = high churn.**
Below-median cashback customers churn significantly more. Cashback is not a cost — it's retention spend.

**4. Inactive customers are already gone.**
High days-since-last-order is a leading churn indicator. Re-engagement must happen within 15 days of inactivity.

---

## Feature Engineering

6 features engineered from raw data — the strongest single predictor (`is_new_customer`) alone had **0.449 correlation** with churn.

| Feature | How | Why it matters |
|---|---|---|
| `is_new_customer` | Tenure ≤ 3 months | New customers churn 6× more |
| `cashback_per_order` | Cashback / (Orders + 1) | Value delivered per transaction |
| `order_frequency` | Orders / (Tenure + 1) | Engagement rate proxy |
| `high_value_customer` | Cashback > median | High-value segment flag |
| `complaint_new_customer` | Complain × is_new_customer | Interaction — most dangerous combo |
| `app_engagement_score` | HoursOnApp × Orders | Combined behavioral signal |

---

## Model Comparison

| Model | AUC | Accuracy | F1 |
|---|---|---|---|
| Logistic Regression | 0.8821 | 87.3% | 70.0% |
| Decision Tree | 0.9421 | 93.6% | 88.2% |
| Random Forest | 0.9934 | 97.2% | 94.4% |
| **XGBoost ✓** | **0.9989** | **98.76%** | **98.1%** |

XGBoost won on every metric. It handles class imbalance better, resists overfitting via built-in regularization, and supports exact SHAP values natively through `TreeExplainer`.

---

## What Makes This Different

| Feature | This Project | Typical Churn Project |
|---|---|---|
| SHAP explanations | ✅ Live per prediction (real values) | ❌ Static bar chart |
| Cohort analysis | ✅ 5 interactive charts | ❌ Not included |
| What-If Simulator | ✅ 12 factors, live model inference | ❌ Not included |
| Budget Optimizer | ✅ ROI-maximizing allocation | ❌ Not included |
| Real model metrics | ✅ Computed from test data | ❌ Often hardcoded |
| Batch prediction | ✅ CSV upload + download | ❌ Not included |
| Feature engineering | ✅ 6 domain-driven features | ❌ Raw features only |
| Model comparison | ✅ 4 algorithms benchmarked | ❌ Single model |
| Docker | ✅ Dockerfile included | ❌ Not included |
| Business ROI frame | ✅ Revenue × risk quantified | ❌ Not included |

---

## Tech Stack

**ML:** Python · XGBoost · Scikit-learn · SHAP (TreeExplainer)  
**App:** Streamlit · Plotly · Pandas · NumPy  
**Infra:** Docker · Streamlit Cloud · GitHub

---

## Run Locally

```bash
git clone https://github.com/Amruth011/customer-churn-prediction-retention-roi.git
cd customer-churn-prediction-retention-roi
pip install -r requirements.txt
streamlit run streamlit_app.py
# → http://localhost:8501
```

```bash
# Or with Docker
docker build -t churn-app .
docker run -p 8501:8501 churn-app
```

---

## Architecture

The system is built in two phases: an **offline training pipeline** that runs once in a notebook, and an **online inference layer** that serves the live Streamlit app.

```
╔══════════════════════════════════════════════════════════════════════╗
║                    OFFLINE  —  Training Pipeline                     ║
║                       (notebooks/EDA.ipynb)                          ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  📂 Raw Excel Data (5,630 customers, 20 features)                    ║
║         │                                                            ║
║         ▼                                                            ║
║  🔍 EDA & Data Quality                                               ║
║     • Null imputation  • Outlier detection  • Class imbalance check  ║
║         │                                                            ║
║         ▼                                                            ║
║  ⚙️  Feature Engineering  (6 new features created)                   ║
║     • is_new_customer  • cashback_per_order  • order_frequency       ║
║     • high_value_customer  • complaint_new_customer  • app_score     ║
║         │                                                            ║
║         ▼                                                            ║
║  🏆 Model Training & Selection  (4 models benchmarked)               ║
║     Logistic Reg → Decision Tree → Random Forest → XGBoost ✓        ║
║         │                                                            ║
║         ▼                                                            ║
║  💾 best_churn_model.pkl   +   test_data.csv (held-out)              ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
                              │
                              │  model.pkl loaded at startup
                              ▼
╔══════════════════════════════════════════════════════════════════════╗
║                     ONLINE  —  Streamlit App                         ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  👤 User Input (single customer or CSV upload)                       ║
║         │                                                            ║
║         ▼                                                            ║
║  🔮 XGBoost Inference  →  Churn Probability (0–100%)                 ║
║         │                                                            ║
║         ├──▶  🔍 SHAP TreeExplainer  →  Per-feature attribution      ║
║         │         (exact values, zero approximation)                 ║
║         │                                                            ║
║         ├──▶  🎯 Priority Score  =  Revenue × Churn Probability      ║
║         │                                                            ║
║         ├──▶  🔄 What-If Simulator  →  Live re-inference on sliders  ║
║         │                                                            ║
║         ├──▶  💰 Budget Optimizer  →  ROI-maximizing allocation      ║
║         │                                                            ║
║         └──▶  📦 Batch Predictions  →  CSV download                  ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
                              │
                              ▼
                    ☁️  Streamlit Cloud  /  🐳 Docker
```

---

## Project Structure

```
customer-churn-prediction-retention-roi/
│
│   streamlit_app.py              ← 🚪 Entry point — Home page & business story
│   requirements.txt              ← 📦 All dependencies
│   Dockerfile                    ← 🐳 Container for cloud deployment
│
├── pages/                        ← 📄 Each file = one dashboard page
│   │                                  (Streamlit auto-generates sidebar nav)
│   ├── 1_Churn_Predictor.py      ← 🔮 Predict + SHAP waterfall + priority score
│   ├── 2_Priority_Score.py       ← 🎯 Revenue-weighted ranking of 937 customers
│   ├── 3_What_If_Simulator.py    ← 🔄 12-factor live retention simulator
│   ├── 4_Budget_Optimizer.py     ← 💰 Allocate budget → maximize revenue saved
│   ├── 5_Model_Transparency.py   ← 🔬 Real AUC, confusion matrix, ROC from test data
│   ├── 6_Cohort_Analysis.py      ← 📅 Tenure-based churn patterns (0–3 mo = 41.9%)
│   └── 7_Batch_Analysis.py       ← 📦 CSV upload → bulk predictions + download
│
├── src/
│   └── best_churn_model.pkl      ← 🧠 Trained XGBoost model (loaded by all pages)
│
├── data/raw/
│   ├── E Commerce Dataset.xlsx   ← 📊 Source data: 5,630 customers, 20 features
│   ├── test_data.csv             ← 🔒 Held-out test set (used for real metrics)
│   └── sample_upload.csv         ← 📋 Demo file for batch upload page
│
├── notebooks/
│   └── EDA.ipynb                 ← 🔭 Full training pipeline: EDA → features → model
│
└── assets/                       ← 🎬 GIF demos used in this README
    ├── home.gif
    ├── predictor.gif
    ├── priority.gif
    ├── whatif.gif
    ├── budget.gif
    ├── model.gif
    ├── cohort.gif
    └── batch.gif
```

> **How it all connects:** `EDA.ipynb` trains the model and saves `best_churn_model.pkl` → every page in `pages/` loads that single `.pkl` at startup → `streamlit_app.py` is the home page that GitHub renders as the entry point.

---

## FAQ

**Can I use this on my own dataset?**  
Yes — swap the Excel file, retrain the notebook, save the new `.pkl` to `src/`.

**Why XGBoost over a neural network?**  
For tabular data at this scale, XGBoost consistently wins on accuracy and trains faster. It also supports exact SHAP values — critical for the explainability layer.

**Are the SHAP values real or approximated?**  
Real. `shap.TreeExplainer` computes exact values — no sampling, no approximation.

**Is the What-If Simulator running the real model?**  
Yes — every slider change re-runs live inference on the trained XGBoost model.

---

## Author

**Amruth Kumar M**  
B.Tech AI & Data Science · REVA University, Bengaluru  
Data Science Intern @ iStudio Technologies

[![Portfolio](https://img.shields.io/badge/🌐%20Portfolio-amruthportfolio.me-7C3AED?style=for-the-badge)](https://amruthportfolio.me)
[![GitHub](https://img.shields.io/badge/GitHub-Amruth011-181717?style=for-the-badge&logo=github)](https://github.com/Amruth011)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/amruth-kumar-m)

---

<div align="center">

*Built end-to-end by a final-year AI & Data Science student.*  
*Raw data → production ML system — no shortcuts.*

**[⭐ Star this repo](https://github.com/Amruth011/customer-churn-prediction-retention-roi)** if it was useful.

</div>
