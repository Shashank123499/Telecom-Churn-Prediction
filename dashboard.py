import streamlit as st
import pandas as pd
import plotly.express as px

def dashboard():

    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "Choose Module",
        [
            "Dashboard",
            "Predict Customer",
            "Analytics",
            "Reports"
        ]
    )

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    return page

@st.cache_data
def load_data():
    return pd.read_csv("Telco-Customer-Churn.csv")


def show_dashboard():

     st.title("📊 Telecom Customer Churn Dashboard")
     st.markdown("Interactive Dashboard for Customer Churn Analysis")
     
     dataset = load_data()
     st.sidebar.header("Dashboaed Filters")

     gender = st.sidebar.multiselect(
        "Gender", dataset["gender"].unique(), default = dataset["gender"].unique()
     )

     contract = st.sidebar.multiselect(
        "Contract Type", dataset["Contract"].unique(), default = dataset["Contract"].unique()
     )

     internet_service = st.sidebar.multiselect(
        "Internet Service", dataset["InternetService"].unique(), default = dataset["InternetService"].unique()
     )

     filtered_data = dataset[
              (dataset["gender"].isin(gender))&
              (dataset["Contract"].isin(contract))&
              (dataset["InternetService"].isin(internet_service))
     ]
    
     total_customer = len(filtered_data)
     churn_customer = len(filtered_data[filtered_data["Churn"] == "Yes"])
     retain_customer = len(filtered_data[filtered_data["Churn"] == "No"])
     if filtered_data.empty:
        st.warning("No data found for the selected filters.")
        return
     churn_rate = round((churn_customer/total_customer)*100,2)

     col1,col2,col3,col4 = st.columns(4)

     with col1 :
       st.metric("👥 Total Customers",total_customer)

     with col2:
        st.metric("❌ Churn Customers",churn_customer)

     with col3:
        st.metric("✅ Retained Customers",retain_customer)

     with col4:
        st.metric("📈 Churn Rate",churn_rate)


     chart1 = px.pie(
     filtered_data,
     names="Churn",
     title="Customer Churn Distribution"
     )

     st.plotly_chart(chart1,width = 'stretch')

     chart2 = px.histogram(
     filtered_data,x = "Contract",color = "Churn",barmode = "group",
     title="Customers by Contract Type"
     )

     st.plotly_chart(chart2,width = 'stretch')

     chart3 = px.histogram(
     filtered_data,
    x="MonthlyCharges",
    color="Churn",
    title="Monthly Charges Distribution"
    )
     st.plotly_chart(chart3, width = 'stretch')

     row1_col1,row1_col2 = st.columns(2)

     with row1_col1:

        chart4 =  px.histogram(
                filtered_data,x = "gender",barmode = "group",color = "Churn",
                title = "Churn By Gender")
        st.plotly_chart(chart4,width = 'stretch')

     with row1_col2:

        chart5 =  px.histogram(
                        filtered_data,x = "Contract",barmode = "group",color = "Churn",
                        title = "Churn by Contract")
        st.plotly_chart(chart5, width = 'stretch')

     row2_col1,row2_col2 = st.columns(2)

     with row2_col1:

        chart6 = px.histogram(filtered_data,x = "OnlineSecurity",color = "Churn",barmode = "group",
             title = "Churn by Security")
        st.plotly_chart(chart6, width = 'stretch')

     with row2_col2:

        chart7 = px.histogram(filtered_data,x = "tenure",color = "Churn",barmode = "group",
             title = "Churn by Tenure ")
        st.plotly_chart(chart7, width = 'stretch')


     row3_col1,row3_col2 = st.columns(2)

     with row3_col1:

        chart8 = px.histogram(filtered_data,x = "SeniorCitizen",color = "Churn",barmode = "group",
             title = "Churn by Citizen")
        st.plotly_chart(chart8, width = 'stretch')

     with row3_col2:

        chart9 = px.histogram(filtered_data,x = "InternetService",color = "Churn",barmode = "group",
             title = "Churn by Serivces")
        st.plotly_chart(chart9, width = 'stretch')


     row4_col1,row4_col2 = st.columns(2)

     with row4_col1:

        chart10 = px.histogram(filtered_data,x = "TotalCharges",color = "Churn",barmode = "group",
             title = "Churn by TotalCharges")
        st.plotly_chart(chart10, width = 'stretch')

     with row4_col2:

        chart11 = px.histogram(filtered_data,x = "PaymentMethod",color = "Churn",barmode = "group",
             title = "Churn by Payment Method")
        st.plotly_chart(chart11, width = 'stretch')


     st.subheader("📌 Business Insights")

     st.success("""
     • Month-to-month customers show the highest churn.

     • Customers without Online Security churn more frequently.

     • New customers (low tenure) are more likely to leave.

     • Higher Monthly Charges are associated with increased churn.
     """)
        
        
        

        
        
        

        
        
        

     