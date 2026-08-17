import streamlit as st
import pandas as pd
import pickle 

@st.cache_resource
def load_model():
    model = pickle.load(open("churn-Prediction.pkl", "rb"))
    processor = pickle.load(open("processor.pkl", "rb"))
    return model, processor

def predict_customer():
    # Load saved model and processor
    model,processor = load_model()

    st.title("📞 Telecom Churn Prediction")

    st.write("Enter customer details below:")
    col1, col2 = st.columns(2)

    with col1:
     gender = st.selectbox("Gender", ["Male", "Female"])
     partner = st.selectbox("Partner", ["Yes", "No"])
     dependents = st.selectbox("Dependents", ["Yes", "No"])
     phone_service = st.selectbox("Phone Service", ["Yes", "No"])
     multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )
     internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )
     online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )
     online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )
     device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )
     tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    with col2:
     streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

     streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

     contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

     paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

     payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

     tenure = st.number_input("Tenure (Months)", min_value=0)

     monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0
    )

     total_charges = st.number_input(
        "Total Charges",
        min_value=0.0
    )

     senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

# Prediction Button

    if st.button("Predict Churn"):

     input_df = pd.DataFrame({
        'gender': ['gender'],
        'Partner': ['partner'],
        'Dependents': ['dependents'],
        'PhoneService': ['phone_service'],
        'MultipleLines': ['multiple_lines'],
        'InternetService': ['internet_service'],
        'OnlineSecurity': ['online_security'],
        'OnlineBackup': ['online_backup'],
        'DeviceProtection': ['device_protection'],
        'TechSupport': ['tech_support'],
        'StreamingTV': ['streaming_tv'],
        'StreamingMovies': ['streaming_movies'],
        'Contract': ['contract'],
        'PaperlessBilling': ['paperless_billing'],
        'PaymentMethod': ['payment_method'],
        'tenure': ['tenure'],
        'MonthlyCharges': ['monthly_charges'],
        'TotalCharges': ['total_charges'],
        'SeniorCitizen': ['senior_citizen']
    })

     transformed_data = processor.transform(input_df)

     prediction = model.predict(transformed_data)
     probability = model.predict_proba(transformed_data)

     confidence = probability[0][1] * 100

     st.metric(
        "Churn Probability",
        f"{confidence:.2f}%"
    )

     if prediction[0] == 1:
        st.error("⚠ Customer is likely to churn.")
     else:
        st.success("✅ Customer is likely to stay.")