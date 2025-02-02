import streamlit as st
import requests

response=requests.post("http://localhost:8000 ")

with st.form("Chat API"):
    st.text_area("Ask the question")
