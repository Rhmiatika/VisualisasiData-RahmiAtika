import streamlit as st # type: ignore
import graphviz as graphviz # type: ignore

st.title("Graphviz Chart")
st.write("Kelompok: 28")
st.markdown("""
- Noer Muhammad Ayub - 0110222142
- Rahmi Atika - 0110222279    
- Saskia Putri Ananda - 0110222159 
""")            

st.graphviz_chart("""
    digraph {
            "Training Data" -> "ML Algorithm" 
            "ML Algorithm" -> "Model"
            "Model" -> "Results Forecasting"
            "New Data" -> "Model"
            }     
""")