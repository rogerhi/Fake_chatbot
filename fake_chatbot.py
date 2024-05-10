import streamlit as st
import time

st.title("Chatbot App")

input_text = st.text_input("Type a message:")

if st.button("Send"):
    user_input = input_text
    st.write(f"**You:** {user_input}")
    time.sleep(1)  # simulate a delay to mimic a chatbot's response time
    st.write(f"**Chatbot:** {user_input}")  # mirror the user's input