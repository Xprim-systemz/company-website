import streamlit as st

st.subheader("Contact Me")

with st.form(key="contactMe"):
    user_email=st.text_input("Enter your email")
    message=st.text_area("Type your message")
    button=st.form_submit_button("Send Message")
    if button:
        st.write("good")