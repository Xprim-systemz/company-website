import streamlit as st
from send_email import send_email

st.subheader("Contact Me")

with st.form(key="contactMe"):
    user_email=st.text_input("Enter your email")
    message=st.text_area("Type your message")
    message=f""" {message} \nFrom: {user_email}"""
    button=st.form_submit_button("Send Message")
    if button:
        send_email(message,user_email)
        st.info("Message Sent!")