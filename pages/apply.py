import streamlit as st

st.title("Apply Now")

st.text_input("First Name")
st.text_input("Last Name")
st.text_input("Email")
st.text_input("Phone Number")

st.selectbox("Nationality", ["Sri Lanka", "India", "Australia", "Other"])

st.text_area("Why do you want to join?")

st.file_uploader("Upload CV")

if st.button("Submit"):
    st.success("Application submitted successfully!")
