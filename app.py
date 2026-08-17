import streamlit as st
from login import login
from dashboard import dashboard,show_dashboard
from predict import predict_customer
from analytics import analytic_page
from reports import report_summary

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

page = dashboard()

if page == "Dashboard":
    show_dashboard()

elif page == "Predict Customer":
    predict_customer()

elif page == "Analytics":
    analytic_page()

elif page == "Reports":
    report_summary()
    

    

