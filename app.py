import streamlit as st

st.title("Student Stress Checker")

study = st.slider("Study Hours", 0, 12)
sleep = st.slider("Sleep Hours", 0, 12)
screen = st.slider("Screen Time", 0, 12)

if st.button("Check Stress"):
    if sleep < 5 or study > 7 or screen > 7:
        st.write("Stress Level: High")
    elif sleep >= 6 and study <= 5:
        st.write("Stress Level: Low")
    else:
        st.write("Stress Level: Medium")