import streamlit as st

st.set_page_config(page_title="Apply Now", layout="wide")

st.title("Apply Now")
st.write("Please complete your application for the Cultural Infusion Fellowship.")

# ================= PERSONAL INFO =================
st.subheader("1. Personal Information")

col1, col2 = st.columns(2)
with col1:
    first_name = st.text_input("First Name *")
with col2:
    last_name = st.text_input("Last Name *")

email = st.text_input("Email *")
phone = st.text_input("Phone Number *")
nationality = st.selectbox("Nationality *", ["Select", "Sri Lanka", "India", "Australia", "Other"])

# ================= PROGRAM DETAILS =================
st.subheader("2. Program Details")

internship_type = st.selectbox(
    "What type of internship are you looking for?",
    ["Global Internship", "Internship + Cultural Program", "Short-Term Internship", "Not Sure"]
)

st.text_area("Tell us more about your preference")

# ================= CV =================
st.subheader("3. Upload CV")
cv = st.file_uploader("Upload your CV / Resume", type=["pdf", "docx"])

st.info("After submission, our team will contact you to schedule your interview.")

# ================= SUBMIT =================
if st.button("Submit Application"):
    st.success("Application submitted successfully. We will contact you soon.")
