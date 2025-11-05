# import library yang dibutuhkan
import streamlit as st # pyright: ignore[reportMissingImports]

# text elemen
# header - untuk membuat tulisan header
st.title("Kelompok 28")
st.markdown("""
- Noer Muhammad Ayub - 0110222142
- Rahmi Atika - 0110222279    
- Saskia Putri Ananda - 0110222159 
""")
st.write("Hello")
st.header("ALOO INI HEADER YA")     #membuat header
st.subheader("Ini sub header nya")  #membuat sub header
st.text("ini teks biasa tanpa format")  #membuat subjuduk yang kecil
st.markdown("*Teks blod* teks italic") #membuat teks bold dan italic
st.markdown("""
- Ini  baris satu 
- ini menggunakan markdown multibaris      
1. Ini baris dua    
2. ini menggunakan markdown multibaris    
* Ini baris tiga
* ini menggunakan markdown multibaris
""")
st.caption("CAPTION") 
st.title("ini judul")

# Praktikum Mandiri

st.title("PRAKTIMUM01 VISUALISASI DATA")
st.subheader("Text Elemen")

# Bagian 2: Memanpilkan Rumus (LaTeX)
st.header("Displaying LaTeX")
st.latex(r'''\cos^2\thate = 1-2\sin^2\theta''') # rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') # rumus kuadrat binominimal

# Bagian 3: Menampilkan kode program
st.header("Display Code")
st.subheader("Python Code")

# simpan ke variable
code = '''
def hello()
    print("Hello, Streamlit!")
'''

# st.code() untuk menampilkan potongan code dengan format rapi dan syntax highlighting
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
        public class GFG {
            public static void main (String arg[]){
                system.out.printIn("Hello World!);
        }
    }
""", language='java')
#fungsi st.code() bisa digunakan untuk bahasa pemrograman lain seperti 
# Java, Javascript, C++. HTML, dll

st.subheader("JavaScripts code")
st.code(""" 
<p id="demo"></p>
<script>
try {
    addalert("Welcome guest!); //kesalahan ketik (addalert)
    sengaja dibuat untuk menimbulkan error
}
catch(err) {
    document.getElementById("demo).innerHTML = err.message; //
    menampilkan pesan error di elemen HTML dengan id 'demo'
}
</script>
""", language='javascript')
#kode ini menunjukkan contoh bagaimana menangani error (exception) di Javascript
#hasilnya tidak dijalankan di streamlit, tapi ditampilkan sebagai contoh kode
