import streamlit as st
import pandas as pd

# Text input 
name = st.text_input('Your Name ')

if name:
    st.write(f'Hello {name}!!')

# Number input
x = st.number_input('Enter a number', min_value=1,max_value=99,step=1)

st.write(f'The current number is {x}')

# Use for better readibilty - horizontal line
st.divider()

# BUTTON

click = st.button('Click Me')

if click:
    st.write(':ghost:'*3)

st.divider()

#checkbox
agree = st.checkbox('I agree')

if agree:
    'Great, You Agreed!'

checked = st.checkbox('Contunue',value=True)

if checked:
    ':+1:'*5

df = pd.DataFrame({'Name':['chan','ram'],
                   'age':[34,22]})
if st.checkbox('Show data'):
    df
st.divider()
# Radio pattern
pets = ['cat','dog','fish']
pet = st.radio('Fav pet',pets,index=2,key='your_pet') # to add a pre-select radio 
st.write('Your fav pet:',pet)

st.session_state.your_pet *3
st.divider()
# select
cities = ['London','berlin','madrid']
city = st.selectbox('Your city',cities,index=1)

'You live in ', city

# Slider

x = st.slider('x',value=10)

st.write(f'x is {x}')

x = st.slider('x',value=10, min_value=12, max_value=55,step=3)

st.write(f'x is {x}')

st.divider()
# file upload

file = st.file_uploader('Upload the file:',type=['txt','cpp','xlsx'])

if file:
    st.write(file)
    if file.type == 'application/octet-stream':
        from io import StringIO
        stringio = StringIO(file.getvalue().decode('utf-8'))
        string_data = stringio.read()
        st.write(string_data)
    elif file.type == 'text/plain':
        stringio = StringIO(file.getvalue().decode('utf-8'))
        string_data = stringio.read()
        st.write(string_data)
    elif file.type =='text/csv':
        import pandas as pd
        df = pd.read_csv(file)
        st.write(df)



# Camera input
camera_photo = st.camera_input('Take a photo')
if camera_photo:
    st.image(camera_photo)