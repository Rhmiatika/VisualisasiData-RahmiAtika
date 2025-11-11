import streamlit as st # type: ignore
import numpy as np # type: ignore

st.title("Container")
with st.container():
    st.write('Element Inside Container')

    # Defining Chart Element
    st.line_chart(np.random.randn(40, 4))
    st.write("Element Outside Container")