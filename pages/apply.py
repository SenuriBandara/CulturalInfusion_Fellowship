import streamlit as st

st.set_page_config(page_title="Apply Now", layout="wide")

st.title("Apply Now")
st.write("Complete your application for Cultural Infusion Fellowship")

st.subheader("Personal Information")

col1, col2 = st.columns(2)
with col1:
    st.text_input("First Name *")
with col2:
    st.text_input("Last Name *")

st.text_input("Email *")
st.text_input("Phone Number *")

st.selectbox("Nationality *", ["Select", "Sri Lanka", "India", "Australia", "Other"])

st.subheader("Program Details")

st.selectbox(
    "Internship Type",
    ["Global Internship", "Internship + Cultural Program", "Short-Term Internship", "Not Sure"]
)

st.text_area("Tell us about your interest")

st.subheader("Upload CV")
st.file_uploader("Upload your CV / Resume")

st.info("Our admissions team will contact you for interview scheduling.")

if st.button("Submit Application"):
    st.success("Application submitted successfully!")
