# Telecom Customer Churn Analysis & Prediction
Interactive Telecom Customer Churn Analysis and Prediction Dashboard built with Python, Streamlit, Pandas, Plotly and XGBoost. The application provides customer churn prediction, interactive analytics, business insights, and downloadable PDF reports.<br>
# Project Overview

This project predicts whether a telecom customer is likely to leave (churn) or stay with the company using Machine Learning techniques.<br>
The objective is to help telecom companies identify at-risk customers and take proactive measures to improve customer retention.

# Dataset
This dataset obtained from kaggle.<br>
The dataset contains customer information such as:

1.customerID<br>
2.Gender<br>
3.Senior Citizen<br>
4.Tenure<br>
5.Monthly Charges<br>
6.Total Charges<br>
7.Contract Type<br>
8.Internet Service<br>
9.Dependents<br>
10.Payment Method<br>
11.MultipleLines<br>
12.OnlineSecurity<br>
13.OnlineBackup<br>
14.TechSupport<br>
15.DeviceProtection<br>
16.StreamingMovies<br>
17.StreamingTV<br>
18.PaperlessBilling<br>
19.Partner<br>
20.Churn Status<br>
# Target Variable:
Churn (Yes/No)

## Features
### 🔐 User Authentication
- Login system for accessing the application.

### 📊 Dashboard
- Total customers<br>
- Churned customers<br>
- Retained customers<br>
- Overall churn rate<br>
- Interactive customer overview<br>

### 🤖 Customer Churn Prediction
- Predict whether a customer is likely to churn.<br>
- Uses trained XGBoost machine learning model.<br>
- Uses preprocessing pipeline for transforming customer data.

### 📈 Churn Analytics
- Contract vs Churn<br>
- Internet Service vs Churn<br>
- Payment Method vs Churn<br>
- Tenure vs Churn<br>
- Monthly Charges vs Churn<br>
- Contract + Internet Service vs Churn<br>
- Correlation analysis<br>

### 📑 Churn Analysis Report
- Executive summary<br>
- Key findings<br>
- Business recommendations<br>
- Overall conclusion<br>
- Downloadable PDF report<br>

## Key Business Insights

- Month-to-month customers have the highest churn rate at approximately 42.71%.<br>
- Customers with 0-12 months of tenure have the highest churn rate at approximately 47.68%.<br>
- Customers paying 61-90 per month have the highest churn rate at approximately 33.91%.<br>
- Month-to-month Fiber Optic customers have the highest churn rate at approximately 54.60%.<br>
- Customers with 61-72 months of tenure have a much lower churn rate of approximately 6.61%.<br>

# Technologies Used
1.Python<br>
2.Pandas<br>
3.NumPy<br>
4.Matplotlib<br>
5.Seaborn<br>
6.Scikit-lear<br>n
7.XGBoost<br>

## Machine Learning Workflow

1. Data Collection<br>
2. Data Cleaning<br>
3. Exploratory Data Analysis<br>
4. Feature Engineering<br>
5. Data Preprocessing<br>
6. Handling Class Imbalance<br>
7. Model Training<br>
8. Model Evaluation<br>
9. Model Serialization<br>
10. Streamlit Deployment<br>

# Model Performance
Metric-Score<br>
Accuracy	83.81%<br>
Precision	78.79%<br>
Recall	93.58%<br>
F1 Score	85.55%<br>

Telecom-Churn-Prediction/<br>
│
├── .devcontainer/<br>
│
├── .gitignore<br>
├── LICENSE<br>
├── README.md<br>

├── requirements.txt<br>

│
├── app.py<br>
│
├── dashboard.py<br>
├── analytics.py<br>
├── predict.py<br>
├── reports.py<br>
├── login.py<br>

│
├── Churn.ipynb<br>

│
├── models/<br>
│   ├── churn-Prediction.pkl<br>
│   └── processor.pkl<br>

│
├── data/<br>
│   └── Telco-Customer-Churn.csv<br>

│
├── reports/<br>
│   ├── classification_report.txt<br>
│   ├── Model_Score.txt<br>
│   ├── confusion_matrix.png<br>
│   └── Actual_VS_Predicted.csv<br>



## Future Improvements

- Hyperparameter tuning
- Model explainability using SHAP<br>
- Real-time customer risk scoring<br>
- Improved authentication system<br>
- Cloud deployment<br>
- Automated model retraining<br>
- Customer retention recommendation system<br>
# Author
Shashank Awasthi<br>
Aspiring Data Scientist and Machine Learning Enthusiast.
