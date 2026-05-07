import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# STATE CONTROL
# =========================
if "show_form" not in st.session_state:
    st.session_state.show_form = False

def open_form():
    st.session_state.show_form = True

def close_form():
    st.session_state.show_form = False

# =========================
# CSS
# =========================
st.markdown("""
<style>

.block-container {
    padding: 2rem 5rem;
}

/* HERO */
.hero {
    padding: 90px 40px;
    background: linear-gradient(120deg, #0b1220, #1e3a8a);
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

.hero h1 {
    font-size: 56px;
    font-weight: 800;
}

.hero p {
    font-size: 20px;
    color: #e2e8f0;
}

/* OVERVIEW */
.overview-box {
    background: linear-gradient(120deg, #0b1220, #1e3a8a);
    padding: 60px 50px;
    border-radius: 22px;
    color: white;
    margin-bottom: 30px;
}

/* CTA */
.cta {
    background: linear-gradient(120deg, #0b1220, #1e3a8a);
    color: white;
    padding: 70px;
    border-radius: 22px;
    text-align: center;
    margin-top: 40px;
}

.stButton > button {
    background: white;
    color: #1e3a8a;
    font-weight: 600;
    padding: 0.7rem 2rem;
    border-radius: 10px;
}

/* FORM */
.form-box {
    background: white;
    padding: 40px;
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.form-title {
    font-size: 28px;
    font-weight: 800;
    margin-bottom: 10px;
}

.section {
    font-weight: 700;
    margin-top: 20px;
    color: #1e3a8a;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown("""
<div class="hero">
    <h1>Cultural Infusion Fellowship</h1>
    <p>Where Talent, Opportunity, and Culture Converge</p>
</div>
""", unsafe_allow_html=True)

# =========================
# OVERVIEW (SIMPLE)
# =========================
st.markdown("""
<div class="overview-box">
<h2>Program Overview</h2>
<p>
The Cultural Infusion Fellowship is a globally connected development experience designed to shape future-ready talent.
It blends international exposure, professional development, and cultural immersion into one structured journey.
Participants gain real-world experience, build globally relevant skills, and engage with diverse cultures and industries.
</p>
</div>
""", unsafe_allow_html=True)

# =========================
# CTA
# =========================
st.markdown("""
<div class="cta">
    <h2>Begin Your Global Journey</h2>
    <p>Join Cultural Infusion Fellowship and unlock global opportunities.</p>
</div>
""", unsafe_allow_html=True)

st.button("Apply Now", on_click=open_form)

# =========================
# APPLICATION FORM
# =========================
if st.session_state.show_form:

    st.markdown("---")

    st.markdown('<div class="form-box">', unsafe_allow_html=True)

    st.markdown('<div class="form-title">Apply Now</div>', unsafe_allow_html=True)

    st.write("""
Please complete the form below and schedule your interview to apply for our internship program.
If you’re accepted, confirm your spot with a deposit.
""")

    # CLOSE BUTTON
    st.button("Close Form", on_click=close_form)

    st.markdown('<div class="section">1. Personal Information</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name *")
    with col2:
        last_name = st.text_input("Last Name *")

    email = st.text_input("Email *")
    phone = st.text_input("Phone Number *")
    nationality = st.selectbox("Nationality *", ["Select", "Sri Lanka", "India", "Australia", "Other"])

    st.markdown('<div class="section">2. Program Details</div>', unsafe_allow_html=True)

    internship_type = st.selectbox(
        "What type of internship are you looking for?",
        ["Global Internship", "Internship + Cultural Program", "Short-Term Internship", "Not Sure"]
    )

    st.text_area("Tell us your preference (optional)")

    cv = st.file_uploader("Upload your CV/Resume (optional)")

    st.markdown('<div class="section">Next Step</div>', unsafe_allow_html=True)

    st.info("On clicking submit, you will be contacted by our admissions team for interview scheduling.")

    submitted = st.button("Submit Application")

    if submitted:
        st.success("Application submitted successfully. Our team will contact you soon.")

    st.markdown('</div>', unsafe_allow_html=True)
