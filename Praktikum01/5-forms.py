import streamlit as st # type: ignore
import datetime
import pandas as pd # type: ignore

st.title("Kelompok 28")
st.markdown("""
- Noer Muhammad Ayub - 0110222142
- Rahmi Atika - 0110222279    
- Saskia Putri Ananda - 0110222159 
""")
st.title("Text Box")
# Creating Text Box
name = st.text_input("Enter Your Name")
st.write("Your Name is ", name)

# Creating Text Box
input_text = st.text_area("Enter Your Review")
# Printing entered text
st.write(""" You entered: \n""",input_text)

# Create Number Input
st.number_input("Enter Your Number")

# Create Number Input
num = st.number_input("Enter Your Number", 0, 10, 5, 2)
# Create Number Input
st.write("Min, Value is 0, \n Max. Value is 10")
st.write("Default, Value is 5, \n Step Size Value is 2")
st.write("Total value after adding number entered with step value is:", num)

st.title("Time")
# Deifining Time Function
st.time_input("Select Your Time")

st.title("Date")
# Deifining Date Function
st.date_input("Select Date")

st.title("Date")
# Deifining Date Function
st.date_input("Select Your date", value=datetime.date(1989, 12, 25),
              min_value=datetime.date(1987, 1, 1),
              max_value=datetime.date(2005, 12, 1))

st.title("Select Color")
# Deifining color picker
color_code = st.color_picker("Select Your Color")
st.header(color_code)

st.title("CSV Data")
data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")
if details:
    if data_file is not None:
        file_details = {"file_name": data_file.name, "file_type": data_file.type, "file_size": data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")

my_form = st.form(key='form')
a = my_form.text_input(label="Enter any text")
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')

st.write(a)