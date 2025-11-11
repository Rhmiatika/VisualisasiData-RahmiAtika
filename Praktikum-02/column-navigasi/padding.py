import streamlit as st # type: ignore
from PIL import Image # type: ignore

img = Image.open("../../Praktikum01/assets/brian.jpg")
st.title("Padding")
# Defining Padding with columns
col1, padding, col2, = st.columns((10,2,10))
with col1:
    col1.image("../../Praktikum01/assets/desix-bg.jpg")
    col2.image("../../Praktikum01/assets/desix.jpg")