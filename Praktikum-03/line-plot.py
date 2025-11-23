import streamlit as st # type: ignore
import matplotlib.pyplot as plt # type: ignore

st.title('Praktikum 3: Matplotlib - Line Chart')
st.write("Kelompok 28 - Visualisasi Data")
st.markdown("""
1. Rahmi Atiika - 0110222279
2. Saskia Putri Ananda - 0110222159
3. Noer Muhammad Ayub - 0110222142
""")

# Buat Data Sampel
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70]
product_B_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

# Layout Streamlit
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", ("Single Line Plot",
                                                         "Multiple & Customizations",
                                                         "Jenis Garis untuk Menunjukkan Tren",
                                                         "Subplot"))

# Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(month, product_A_sales, label="Product A")
    ax.set_title('Penjualan Produk A per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    st.pyplot(fig)

# Multiple Line Plot & Customizations
def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(month, product_A_sales, label="Product A", color='blue', linestyle='--', marker='o')
    ax.plot(month, product_B_sales, label="Product B", color='red', linestyle='-', marker='x')

    ax.set_title('Penjualan Produk per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Jenis Garis untuk Tren
product_C_sales = [18,22,25,28,32,38,42,45,48,52,56,60]
product_D_sales = [7,9,11,13,16,18,20,23,25,28,30,33]
def tren_line_plot():
    fig, axs = plt.subplots()
    axs.plot(month, product_A_sales, label="Product A", color='blue', linestyle='--')
    axs.plot(month, product_B_sales, label="Product B", color='red', linestyle='-')
    axs.plot(month, product_C_sales, label="Product C", color='green', linestyle='-.')
    axs.plot(month, product_D_sales, label="Product D", color='purple', linestyle=':')
    axs.set_title('Penjualan Produk per Bulan')
    axs.set_xlabel('Bulan')
    axs.set_ylabel('Penjualan')
    axs.legend()
    axs.grid(True)
    st.pyplot(fig)

# Subplot
def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10,8))

    # plot pertama untuk product C
    axs[0].plot(month, product_C_sales, label='Product C', color='green', marker='d')
    axs[0].set_title('Penjualan Product C per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid('True')

    # plot pertama untuk product D
    axs[1].plot(month, product_D_sales, label='Product D', color='purple', marker='s')
    axs[1].set_title('Penjualan Product D per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid('True')

    plt.tight_layout()
    st.pyplot(fig)

# Logika untuk menampilkan visualisasi sesuai menu
if option == "Single Line Plot":
    line_plot()
elif option == "Multiple & Customizations":
    customize_line_plot()
elif option == "Jenis Garis untuk Menunjukkan Tren":
    tren_line_plot()
elif option == "Subplot":
    subplots()