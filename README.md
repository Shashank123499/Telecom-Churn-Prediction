# 📞 Telecom Customer Churn Analysis & Prediction

An interactive **Telecom Customer Churn Analysis and Prediction Dashboard** built using Python, Streamlit, Pandas, Plotly, Scikit-learn, and XGBoost.<br>

The application helps analyze customer churn patterns, predict whether a customer is likely to churn, identify high-risk customer segments, and generate a downloadable PDF business report.

---

## 🚀 Project Overview

Customer churn is one of the major challenges faced by telecom companies.<br>

This project uses Machine Learning and Data Analytics to identify customers who are likely to leave a telecom service.<br>

The application provides:

- 🔐 User authentication<br>
- 📊 Interactive customer dashboard<br>
- 🤖 Real-time churn prediction<br>
- 📈 Interactive churn analytics<br>
- 📑 Business analysis report<br>
- 📥 Downloadable PDF report<br>
- 💡 Business recommendations<br>

The goal is to help telecom companies identify high-risk customers and take proactive actions to improve customer retention.

---

## 🎯 Project Objectives

The main objectives of this project are:<br>

1. Analyze telecom customer data.<br>
2. Identify important factors associated with customer churn.<br>
3. Build a machine learning model to predict churn.<br>
4. Create an interactive Streamlit dashboard.<br>
5. Provide business insights from customer data.<br>
6. Generate a professional PDF analysis report.<br>

---

# 📂 Dataset

The dataset used in this project was obtained from **Kaggle**.<br>

The dataset contains information about telecom customers, including demographic information, services, billing information, contract details, and churn status.

### Dataset Features

1. Customer ID<br>
2. Gender<br>
3. Senior Citizen<br>
4. Partner<br>
5. Dependents<br>
6. Tenure<br>
7. Phone Service<br>
8. Multiple Lines<br>
9. Internet Service<br>
10. Online Security<br>
11. Online Backup<br>
12. Device Protection<br>
13. Tech Support<br>
14. Streaming TV<br>
15. Streaming Movies<br>
16. Contract<br>
17. Paperless Billing<br>
18. Payment Method<br>
19. Monthly Charges<br>
20. Total Charges<br>
21. Churn<br>

---

## 🎯 Target Variable

**Churn**<br>

- `Yes` → Customer has churned<br>
- `No` → Customer has remained with the company<br>

---

# ✨ Application Features

## 🔐 1. User Authentication

The application contains a login system to control access to the dashboard.<br>

Features include:<br>

- Login interface<br>
- Session-based authentication<br>
- Protected application pages<br>

---

## 📊 2. Dashboard

The dashboard provides an overview of the telecom customer base.<br>

### Key Performance Indicators<br>

- 👥 Total Customers<br>
- ❌ Churned Customers<br>
- ✅ Retained Customers<br>
- 📈 Overall Churn Rate<br>

The dashboard provides a quick summary of the current customer base and churn situation.<br>

---

## 🤖 3. Customer Churn Prediction<br>

The application provides real-time customer churn prediction.<br>

Users can enter customer information such as:<br>

- Gender<br>
- Partner<br>
- Dependents<br>
- Tenure<br>
- Internet Service<br>
- Contract<br>
- Payment Method<br>
- Monthly Charges<br>
- Total Charges<br>
- Senior Citizen<br>
- Online Security<br>
- Online Backup<br>
- Device Protection<br>
- Tech Support<br>
- Streaming Services<br>

The application then predicts whether the customer is likely to:<br>

### ⚠️ Churn

or<br>

### ✅ Stay

The model also provides the **churn probability**.<br>

### Machine Learning Model

The prediction system uses:<br>

**XGBoost Classifier**<br>

A saved preprocessing pipeline is used to transform the customer input before making predictions.<br>

---

# 📈 4. Churn Analytics

The analytics page provides interactive visualizations to understand customer churn patterns.<br>

### Analytics Included

- 📄 Contract Type vs Churn<br>
- 🌐 Internet Service vs Churn<br>
- 💳 Payment Method vs Churn<br>
- 📅 Tenure vs Churn<br>
- 💰 Monthly Charges vs Churn<br>
- 🔗 Contract + Internet Service vs Churn<br>
- 📊 Correlation Matrix<br>

These visualizations help identify customer groups with higher churn risk.<br>

---

# 📑 5. Churn Analysis Report

The application generates a business-oriented churn analysis report.<br>

The report includes:<br>

### 📊 Executive Summary

- Total customers<br>
- Churned customers<br>
- Retained customers<br>
- Overall churn rate<br>

### 🔍 Key Findings

Important patterns discovered from the analysis.<br>

### 💡 Business Recommendations

Strategies that telecom companies can use to reduce churn.<br>

### 🎯 Conclusion

Overall interpretation of the analysis.<br>

### 📥 PDF Report

Users can generate and download a professional PDF report.<br>

---


# 💡 Key Business Insights

The analysis produced several important insights.<br>

### 📄 Contract Type

Month-to-month customers have the highest churn rate at approximately **42.71%**.<br>

Customers with one-year contracts have a churn rate of approximately **11.27%**, while two-year contract customers have a much lower churn rate of approximately **2.83%**.<br>

---

### 📅 Customer Tenure

Customers with **0–12 months of tenure** have the highest churn rate at approximately **47.68%**.<br>

Churn decreases significantly as customer tenure increases.<br>

Customers with **61–72 months of tenure** have a much lower churn rate of approximately **6.61%**.<br>

---

### 💰 Monthly Charges

Customers paying between **61–90 per month** have the highest churn rate at approximately **33.91%**.<br>

Customers paying between **91–120 per month** also have a high churn rate of approximately **32.78%**.<br>

---

### 🌐 Contract + Internet Service

The highest churn rate is observed among customers with:<br>

**Month-to-month contracts + Fiber Optic internet**<br>

with a churn rate of approximately **54.60%**.v

This customer segment represents an important target for customer retention strategies.<br>

---

# 🧠 Machine Learning Workflow

The project follows the following Machine Learning workflow:<br>

```text<br>
Data Collection<br>
      ↓<br>
Data Cleaning<br>
      ↓<br>
Exploratory Data Analysis<br>
      ↓<br>
Feature Engineering<br>
      ↓<br>
Data Preprocessing<br>
      ↓<br>
Handling Class Imbalance<br>
      ↓<br>
Model Training<br>
      ↓<br>
Model Evaluation<br>
      ↓<br>
Model Serialization<br>
      ↓<br>
Streamlit Deployment<br>
