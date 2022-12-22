import streamlit as st

st.set_page_config(layout="wide")

col1, col2= st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Tianyue Lyu")
    content = """ Hi，I am Tianyue! 
     I am a first year cs student at university of waterloo. """
    st.info(content)
