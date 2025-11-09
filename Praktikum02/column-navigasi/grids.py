import streamlit as st # type: ignore
from PIL import Image # type: ignore
img = Image.open("../../Praktikum01/assets/brian.jpg")
st.title("Grid")

# Defining no. of columns with size
cols = st.columns((1, 1, 1, 1))
cols[0].image("../../Praktikum01/assets/doun.jpg")
cols[1].image("../../Praktikum01/assets/ujeans.jpg")
cols[2].image("../../Praktikum01/assets/piri.jpg")
cols[3].image("../../Praktikum01/assets/brian.jpg")