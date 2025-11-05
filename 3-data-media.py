import streamlit as st  # type: ignore
import base64
from PIL import Image # type: ignore

st.title("Kelompok 28")
st.markdown("""
- Noer Muhammad Ayub - 0110222142
- Rahmi Atika - 0110222279    
- Saskia Putri Ananda - 0110222159 
""")
st.write("Displaying an Images")
# Displaying image by spesifying path
# Image Courtesy by unplash
st.write("Image Courtesy: unplash.com")

# image courtesy
st.write("Displaying Multiple Images")
# Listing out animal images
animal_images = [
    'assets/desix.jpg',
    'assets/ujeans.jpg',
    'assets/brian.jpg',
    'assets/piri.jpg',
    'assets/doun.jpg',

]
# Displaying Multiple images with width 150
st.image(animal_images, width=150)
# Image COurtesy
st.write("Image courtesy: unplash")

#Background Image
import streamlit as st # type: ignore
import base64

# Function to set Image as Background
def add_local_background_image(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    
    # Menampilkan Atribusi Gambar
    st.write("sumber: pinterest.com") 

    # Menerapkan CSS untuk Background
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
        background-size: 50%;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

st.write("Background Image")

# Calling Image in function
add_local_background_image('assets/desix.jpg')

original_image = Image.open("assets/desix-bg.jpg")
# Display Original Image
st.title("Original image")
st.image(original_image)
# Resizing image to 600*400
resized_image = original_image.resize((600, 400))
# Displaying resized image
st.title("Resized Image")
st.image(resized_image)
