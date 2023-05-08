import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2= st.columns(2)

with col1:
    st.title("VLOOK（贩卖小尾巴）")
    content = """ hand-made crafts """
    st.header(content)
with col2:
    st.image("images/photo.png", width=500)

content2 = """
Take a look of our products below! 
"""
st.write(content2)


st.header("""Signature Series""")
st.image("images/img_1.png", width=800)

st.header("""Next-Gen Selection""")
st.image("images/img_2.png",width=800)

st.header("""Participated Exhibition""")
col3, col4= st.columns(2)

with col3:
    st.image("images/img_3.png", width=500)

with col4:
    st.image("images/img_4.png", width=300)





