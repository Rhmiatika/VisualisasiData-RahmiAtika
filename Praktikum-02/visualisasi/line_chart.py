import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore

st.title("Line Chart")
st.write("Kelompok: 28")
st.markdown("""
- Noer Muhammad Ayub - 0110222142
- Rahmi Atika - 0110222279    
- Saskia Putri Ananda - 0110222159 
""")            

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.line_chart(df)