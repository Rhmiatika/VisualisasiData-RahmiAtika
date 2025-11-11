import streamlit as st # type: ignore

# sidebar
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New Userr", ["yes", "No"])
st.sidebar.slider("Select a Number", 0,10)