import streamlit as st # type: ignore
import time

st.title("Kelompok 28")
st.markdown("""
- Noer Muhammad Ayub - 0110222142
- Rahmi Atika - 0110222279    
- Saskia Putri Ananda - 0110222159 
""")
st.title('Creating a Button')
# Defining a button
button = st.button('Click Here')
if button:
    st.write('You have clicked the Button')
else:
    st.write('You have net clicked the Button')

st.title('Creating a Button')  
# Defining Radio button  
gender = st.radio(
    "Select your gender",
    ('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")

st.write("Creating Checkboxes")
st.write("Select yoyr Hobies:")
# Deifning CHeckboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

st.write("Creating Dropdown")
# Creating Dropdown
hobby = st.selectbox('Choose your hobby: ',
('Books', 'Movies', 'Sports'))

st.title("Multi_Select")
# Defining Multi_Select with Pre_Selection
hobbies = st.multiselect('What are your hobbies: ',
['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Browing', 'Hiking'],
['Reading', 'Playing'])

st.title("Download Button")
# Creating Download BUtton
down_btn = st.download_button(
    label="Download Image",
    data=open("assets/desix.jpg", "rb"),
    file_name="tiger.jpg",
    mime="image/jpg"
)

import streamlit as st # type: ignore
st.title("Download Button")
# Creating Download Button
down_btn = st.download_button(
    label="Download Image",
    data=open("assets/desix.jpg", "rb"),
    file_name="grup desix.jpg",
    mime="image/jpg"
)
