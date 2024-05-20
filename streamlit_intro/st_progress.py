import streamlit as st
import time

st.write('Starting an exptensive computation')
latest = st.empty()

progress_text = 'Operations in progress. Please wait'
my_bar = st.progress(50,text=progress_text)
time.sleep(2)

for i in range(100):
    my_bar.progress(i+1)

    latest.text(f"Iteration {i + 1}")
    time.sleep(0.1)

st.write('We are done!!:+1:')