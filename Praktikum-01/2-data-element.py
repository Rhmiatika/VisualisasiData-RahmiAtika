# import library yang dibutuhkan
import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd # type: ignore
import numpy as np # type: ignore
import altair as alt # type: ignore
import matplotlib as plt  # type: ignore

#menampilan judul dan deskripsi
st.title("Praktikum 1 - Visualisasi Data") #Menampilkan judul utama di halaman
st.caption("Bagian 2: Data Elements") #Menampilkan keterangan Bagian

st.title("Kelompok 28")
st.markdown("""
- Noer Muhammad Ayub - 0110222142
- Rahmi Atika - 0110222279    
- Saskia Putri Ananda - 0110222159 
""")
#Data Frame: struktur data berbntuk tabel (baris dan kolom) yang disediakan oleh libarary pandas
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

#menampilkan dataframe
st.dataframe(df)

#highlight Nilai Minimum
st.subheader("Highlight Minimum Value di Daraframe")

#highlight nilai terkecil disetiap kolom dataframe
#axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))


#Tabel Statis
st.subheader("Data Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

#menampilkan tabel statis
st.table(df)

#Matrics: komponen tampilan angka penting
st.subheader("Metrics")
st.metric(label="Temperatur", value="31 C", delta="1.2 C") #kenaikan 1.2 C

#Metrics
col1, col2, col3 = st.columns(3)

# Menampilkan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") # naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") #naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off") #netral (tidal baik, tidak buruk)

# menampilkan indikator data
st.metric(label="Speed", value=None, delta=0) #kosong #naik baik karena di setting default
st.metric("Trees", "91456", "1132649") #penurunan

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))
# defining nultiple argument in write funtion
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nwrite is super funtion")

# Defining random values for chart
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b'])

import matplotlib.pyplot as plt # type: ignore
# Defining chart
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b'])
# Defining chart in write() function
st.write(chart)

# Math calculations with no funtions defined
"Adding 5 & 4 =", 5+4
# Displaying Variable 'a' and its value 
a = 5
'a', a

# Markdown with Magic
"""
# Magic Feature
Markdown working witout defining its funstion explicitly
"""
# dataFrame using magic
df = pd.DataFrame({'col': [1,2]})
'dataframe', df

# Magic working on charts
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots() # type: ignore
ax.hist(s, bins=15)

#Magic chart
"chart", chart

