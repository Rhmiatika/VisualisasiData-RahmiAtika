import streamlit as st # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

st.title('Praktikum 3: Matplotlib - Line Chart')
st.write("Kelompok 28 - Visualisasi Data")
st.markdown("""
1. Rahmi Atiika - 0110222279
2. Saskia Putri Ananda - 0110222159
3. Noer Muhammad Ayub - 0110222142
""")

data = {
    'Jurusan': ['Ilmu Komputer', 'Teknik Informatika', 'Sistem Informasi', 'Data Science'],
    'Jumlah Mahasiswa' : [120, 150, 100, 80]
}
df = pd.DataFrame(data)

# streamlit App
st.title("Basic Bar Chart - Jumlah Mahasiswa per Jurusan")
st.bar_chart(df.set_index('Jurusan'))

# Streamlit App
st.title("Basic Bar Chart Menggunakan Matplotlib")

fig, ax = plt.subplots()
ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color='lightblue')
ax.set_title('Jumlah Mahasiswa Per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

st.pyplot(fig)

st.title("Kustomisasi Basic Bar Chart")

fig, ax = plt.subplots()
colors = ['blue', 'skyblue', 'pink', 'red']
bars = ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color=colors)
ax.set_title('Jumlah Mahasiswa Per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

# Menampilkan nilai pada batang
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, 
            str(bar.get_height()), ha='center')

st.pyplot(fig)

st.title("Multiple Basic Bar Chart")

# Data Tambahan
data_2023 = [120, 150, 100, 80]
data_2024 = [140, 160, 110, 90]

x = range(len(data['Jurusan']))
width = 0.4

fig, ax = plt.subplots()
ax.bar(x, data_2023, width=width, label='2023', color='pink')
ax.bar([p + width for p in x], data_2024, width=width, 
       label='2024', color='lightblue')

ax.set_title('Jumlah Mahasiswa Per Jurusan (2023 vs 2024)')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xticks([p + width / 2 for p in x])
ax.set_xticklabels(data['Jurusan']) # mengatur kabel x-axis di tengah
ax.legend()

st.pyplot(fig)