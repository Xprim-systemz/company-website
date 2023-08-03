
import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')




st.header("The Best Company")
company_info="""Lesamie is a company based in Paris and is specialized in the development of 
software and provision of services in the financial, Agriculcultural and real estate sectors of the 
french economy. we also operate in countries across sub saharan africa, with a regional office in lagos, Nigeria"""

st.write(company_info)
df=pd.read_csv("data.csv",sep=",")

st.subheader("Our Team")
col1,space1,col2,space2,col3=st.columns([1.5,0.5,1.5,0.5,1.5])
with col1:
    for index,row in df[:4].iterrows():
        st.subheader(f"{row['first name']}" + f" {row['last name']}")
        st.write(row["role"])
        st.image("images/"+ row["image"])

with col2:
    for index,row in df[4:8].iterrows():
        st.subheader(f"{row['first name']}" + f" {row['last name']}")
        st.write(row["role"])
        st.image("images/"+ row["image"])

with col3:
    for index,row in df[8:12].iterrows():
        st.subheader(f"{row['first name']}" + f" {row['last name']}")
        st.write(row["role"])
        st.image("images/"+ row["image"])