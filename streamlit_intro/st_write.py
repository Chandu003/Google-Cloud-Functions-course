import streamlit as st
import pandas as pd

# Display data on the screen:
# 1. st.write
# 2. Magic

st.title('Hello Streamlit World! :100:')
st.write('We Learn Streamlit!!!!')

l1 = [1,2,3,4,5]
st.write(l1)

l2 = {1:1,2:2,3:3}

st.write(l2)

# USING MAGIC

'Displaying using magic :smile:'

df = pd.DataFrame({
    'first':[1,2,3,4,5],
    'second':[45,32,12,45,45]
})

df