import streamlit as st 
from PIL import Image


img = Image.open("logo.jpg")

st.image(img, width=600)

st.title("Real-time-Price-Monitoring-Altert-System")

st.header("Daily Price Tracking")
st.header("Historical Storage")
st.header("Price Comparision")
st.header("Alert Syste for Price Charge ")
st.header("Autamated Pipeline")

st.markdown("### Database Connective")

st.success("Proceed Successfully")

st.info("Find the Formal informatiom")

st.warning("you are going to high risk scenerio")

st.error("Account has been blocked for 24 hours")