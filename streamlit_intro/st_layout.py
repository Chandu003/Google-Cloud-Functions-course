import streamlit as st
import pandas as pd

my_select_box = st.sidebar.selectbox('Select',['US','UK','DE','FR'],index=2)

st.write(my_select_box)

my_slider = st.sidebar.slider('Temperature')

left_column, right_column = st.columns(2)

import random
data = [random.random() for i in range(100)]

with left_column:
    st.subheader('A line chart')
    st.line_chart(data)

right_column.subheader('Data')
right_column.write(data[:10])

col1, col2, col3 = st.columns([0.2,0.3,0.5])

col1.markdown('Hello Streamlit World!!!')
col2.write(data[:5])

with col3:
    st.header('A cat')
    st.image('https://static.streamlit.io/examples/cat.jpg')



# Expander
with st.expander('Click to expand'):
    st.bar_chart({'data':[random.randint(2,10) for i in range(25)]})
    st.write('This is an image of a dog')
    st.image('https://static.streamlit.io/examples/dog.jpg')





