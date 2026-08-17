import pandas as pd
import streamlit as st
import plotly.express as px

st.title("📈 Analytics")

@st.cache_data
def load_data():
    return pd.read_csv("Telco-Customer-Churn.csv")

def analytic_page():
  dataset = load_data()
  st.metric("Rows",dataset.shape[0])
  st.metric("Columns",dataset.shape[1])

  st.subheader("📊 Statistical Summary")
  st.write(dataset.describe())

  missing_values = dataset.isnull().sum()
  st.dataframe(missing_values)

  if missing_values.sum() == 0:
    st.success("✅ No missing values found in the dataset.")

  else:
    missing_df = missing_values.reset_index()
    missing_df.columns = ["Columns","Missing Values"]

    fig = px.bar(
        missing_df,
        x="Columns",
        y="Missing Values",
        title="Missing Values"
    )

    st.plotly_chart(fig, width = 'stretch')

  st.subheader("📌 Correlation Matrix")

  numeric_data = dataset.select_dtypes(include = 'number')

  correlation = numeric_data.corr()
  st.dataframe(correlation)

  fig2 = px.imshow(correlation,
                   text_auto = '.2f', title = "Correlation Matrix",aspect = "auto")
  st.plotly_chart(fig2, width = 'stretch')

  st.subheader("📌 Churn Distribution")

  churn_count = dataset["Churn"].value_counts()
  churn_count = churn_count.reset_index()
  churn_count.columns = ["Churn","Customers"]

  fig3 = px.histogram(churn_count, x = "Churn",y = "Customers"
         ,color = "Churn",
         title="Customer Churn Distribution")
  st.plotly_chart(fig3,width = 'stretch')

  st.subheader("👥 Customer Demographics")

  gender_count = dataset["gender"].value_counts().reset_index()
  gender_count.columns = ["Gender","Customers"]

  fig4 = px.bar(gender_count,x = "Gender",y = "Customers",color = "Gender",title = "Customer Distribution by Gender ")
  st.plotly_chart(fig4,width = 'stretch')

  senior_count = dataset["SeniorCitizen"].value_counts().reset_index()
  senior_count.columns = ["Senior Citizen", "Customers"]

  senior_count["Senior Citizen"] = senior_count["Senior Citizen"].replace({
    0: "No",
    1: "Yes"
  })

  fig5 = px.pie(
    senior_count,
    names="Senior Citizen",
    values="Customers",
    title="Senior Citizen Distribution"
)

  st.plotly_chart(fig5,width = 'stretch')

  churn_numeric = dataset["Churn"].map({"Yes":1,"No":0})

  st.subheader("🌐 Payment Method vs Churn")

  payment_churn_rate =(
  churn_numeric.groupby(dataset["PaymentMethod"]).mean()*100
  ).reset_index()

  payment_churn_rate.columns = ["Payment Method","Churn Rate"]

  fig8 = px.bar(
     payment_churn_rate,
     x = "Payment Method",
     y = "Churn Rate",title = "Churn by Payment Method",
     text = "Churn Rate"
  )
  st.plotly_chart(fig8,width = 'stretch')

  st.subheader("📄 Tenure vs Churn")

  dataset["TenureGroup"] = pd.cut(
    dataset["tenure"],
    bins=[0, 12, 24, 36, 48, 60, 72],
    labels=[
        "0-12 Months",
        "13-24 Months",
        "25-36 Months",
        "37-48 Months",
        "49-60 Months",
        "61-72 Months"
    ]
  )

  tenure_churn_rate =(
    churn_numeric.groupby(dataset["TenureGroup"]).mean()*100
    ).reset_index()
  
  tenure_churn_rate.columns = ["Tenure","Churn Rate"]
  
  fig9 = px.bar(
       tenure_churn_rate,
       x = "Tenure",
       y = "Churn Rate",title = "Churn by Tenure",
       text = "Churn Rate"
    )
  st.plotly_chart(fig9,width = 'stretch')

  st.subheader("💰 Monthly Charges vs Churn")

  dataset["monthlycharges_group"] = pd.cut(
     dataset["MonthlyCharges"],
     bins = [0,30,60,90,120],
     labels = [
     "0-30",
     "31-60",
     "61-90",
     "91-120"
     ]
  )

  monthlycharge_churn_rate = (
  churn_numeric.groupby(dataset["monthlycharges_group"]).mean()*100
  ).reset_index()

  monthlycharge_churn_rate.columns = ["Monthly Charges","Churn Rate"]

  fig10 = px.bar(
     monthlycharge_churn_rate,
     x = "Monthly Charges",
     y = "Churn Rate",
     title = "Churn Rate by Monthly Charges",text = "Churn Rate"
  )
  st.plotly_chart(fig10,width = "stretch")

  st.subheader("📄 Contract + Internet Service vs Churn")

  dataset["Contract_Internet"] =(
     dataset["Contract"]+ "-" + dataset["InternetService"]
  )

  combine_churn_rate = (
     churn_numeric.groupby(dataset["Contract_Internet"]).mean()*100
  ).reset_index()

  combine_churn_rate.columns = ["Contract + Internet","Churn Rate"]

  fig11 = px.bar(
     combine_churn_rate,
     x = "Contract + Internet",
     y = "Churn Rate",
     title = "Churn Rate by Contract and Internet Service",text = "Churn Rate"
  )
  st.plotly_chart(fig11,width = "stretch")

  return

