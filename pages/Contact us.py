import streamlit as st
from send_email import send_email
import pandas as pd

st.subheader("Contact Me")
df1=pd.read_csv("topics.csv")

with st.form(key="contactMe"):
    user_email=st.text_input("Enter your email")
    topics_series = []
    for index,rows in df1.iterrows():
        topics_series.append(rows["topic"])
    topics_series=pd.Series(topics_series)
    option = st.selectbox('Select topic you would like to discuss',topics_series)

    message=st.text_area("Type your message")
    message=f""" {message} \nFrom: {user_email}"""
    button=st.form_submit_button("Send Message")
    if button:
        send_email(message,option)
        st.info("Message Sent!")