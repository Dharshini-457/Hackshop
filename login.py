import streamlit as st
import portfolio as pt

def login():
    try:
        with st.form("Login_form"):
            st.title("Login Page!!")
            user_name=st.text_input("User Name")
            password=st.text_input("Password",type="password")
            if st.form_submit_button("Login"):
                if user_name=="abcd" and password=="12345":
                    st.success("Login successful!!")
                    st.balloons()
                    pt.port()
                else:
                    st.error("Ivalid username or password!!")
    except(ValueError):
        st.write("Try a valid Data")

login()