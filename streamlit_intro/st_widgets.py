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




