import streamlit as st

st.set_page_config(page_title="Apply Now", layout="wide")

st.title("Apply Now")

st.subheader("Personal Information")
col1, col2 = st.columns(2)

with col1:
    st.text_input("First Name")
with col2:
    st.text_input("Last Name")

st.text_input("Email")
st.text_input("Phone Number")
st.selectbox("Nationality", ["Sri Lanka", "India", "Australia", "Other"])

st.subheader("Program Details")
st.selectbox("Internship Type", ["Global Internship", "Short Term", "Not Sure"])
st.text_area("Why do you want to join?")

st.subheader("Upload CV")
st.file_uploader("Upload your CV")

if st.button("Submit Application"):
    st.success("Application submitted successfully! We will contact you soon.")
