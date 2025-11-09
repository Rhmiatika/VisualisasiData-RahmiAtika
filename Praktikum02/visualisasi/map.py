import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore

st.title("Map")
st.write("Kelompok: 28")
st.markdown("""
- Noer Muhammad Ayub - 0110222142
- Rahmi Atika - 0110222279    
- Saskia Putri Ananda - 0110222159 
""")            

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)