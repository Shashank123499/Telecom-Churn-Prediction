import streamlit as st

def login():

     st.title("📱 Telecom Customer Retention System")

     st.header("Login")
     username = st.text_input("Enter Username")
     password = st.text_input("Enter Password",type = "password")
     if st.button("Login"):

        if username == "admin" and password == "1234":

            st.session_state.logged_in = True

            st.rerun()

        else:

            st.error("Invalid Username or Password")

        