import streamlit as st # type: ignore

st.title("This is Column")
st.write("Kelompok: 28")
st.markdown("""
- Noer Muhammad Ayub - 0110222142
- Rahmi Atika - 0110222279    
- Saskia Putri Ananda - 0110222159 
""") 

col1, col2 = st.columns(2)

col1.write("Ini kolom pertama")
col1.image("../../Praktikum01/assets/brian.jpg")


col1.write("Ini kolom kedua")
col1.image("../../Praktikum01/assets/doun.jpg")

