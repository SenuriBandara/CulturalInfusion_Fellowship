import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# CSS
# =========================
st.markdown("""
<style>

.block-container {
    padding: 2rem 5rem;
    max-width: 100%;
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

/* CARDS */
.card {
    background: linear-gradient(120deg, #0b1220, #1e3a8a);
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 18px;
    color: white;
}

.small-card {
    background: linear-gradient(120deg, #0b1220, #1e3a8a);
    padding: 16px;
    border-radius: 14px;
    margin-bottom: 12px;
    color: white;
    border-left: 4px solid #60a5fa;
}

/* PRICE BOX */
.price-box {
    background: linear-gradient(120deg, #0b1220, #1e3a8a);
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    color: white;
}

/* CTA */
.cta {
    background: linear-gradient(120deg, #0b1220, #1e3a8a);
    color: white;
    padding: 80px 50px;
    border-radius: 22px;
    text-align: center;
    margin-top: 50px;
}

/* BUTTON */
.apply-btn {
    display: flex;
    justify-content: center;
    margin-top: 30px;
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
# OVERVIEW
# =========================
st.markdown("""
<div class="overview-box">

<h2>Program Overview</h2>

<h4>Building Future Global Leaders</h4>

<p>
The Cultural Infusion Fellowship is a globally connected development experience designed to shape future-ready talent.<br><br>

It blends international exposure, professional development, and cultural immersion into one structured journey.<br><br>

Participants gain real-world experience, build globally relevant skills, and engage with diverse cultures and industries.
</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# EXPERIENCE
# =========================
st.markdown("## Learning & Experience Pathway")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <b>Professional Development</b><br><br>
        Structured international internship experience<br>
        Industry-relevant skill building<br>
        Career readiness development<br>
        Leadership capability enhancement
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <b>Global Exposure</b><br><br>
        Immersive cultural integration<br>
        International collaboration opportunities<br>
        Global peer networking<br>
        Cross-cultural real-world experience
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# INCLUSIONS
# =========================
st.markdown("## Program Inclusions")

included = [
("International Internship Placement", "Structured global internship aligned to your career path."),
("Learning & Development Workshops", "Expert-led sessions for professional growth."),
("Career Acceleration Support", "Tools to strengthen employability."),
("Global Talent Network Access", "Connect with international peers and mentors."),
("1:1 Mentorship & Advisory", "Guidance from experienced professionals."),
("Professional Branding & CV Development", "Build a strong global-ready profile."),
("Visa & Documentation Support", "Assistance throughout visa process."),
("Accommodation Guidance", "Support in finding safe housing."),
("Arrival & Transition Support", "Smooth onboarding support."),
("Cultural Immersion Experiences", "Activities for real cultural engagement.")
]

cols = st.columns(2)

for i, (title, desc) in enumerate(included):
    with cols[i % 2]:
        st.markdown(f"""
<div class="small-card">
<b>{title}</b><br>
{desc}
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# PROGRAM INVESTMENT
# =========================
st.markdown("## Program Investment")

pricing = [
("4 Weeks", "9,340 AUD", "5,600 AUD"),
("6 Weeks", "9,585 AUD", "5,600 AUD"),
("8 Weeks", "11,440 AUD", "5,600 AUD"),
("10 Weeks", "13,295 AUD", "5,600 AUD"),
("12 Weeks", "15,290 AUD", "6,600 AUD"),
("16 Weeks", "18,730 AUD", "6,600 AUD"),
("20 Weeks", "21,460 AUD", "6,600 AUD"),
("24 Weeks", "24,150 AUD", "6,600 AUD"),
]

cols = st.columns(4)

for i, (duration, full, without) in enumerate(pricing):
    with cols[i % 4]:
        st.markdown(f"""
<div class="price-box">

<b>{duration}</b><br><br>

Full Program<br>
{full}<br><br>

Without Accommodation<br>
{without}

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

# =========================
# APPLY BUTTON (FIXED)
# =========================
st.markdown("""
<div class="apply-btn">
    <a href="pages/apply.py" style="
        background:white;
        padding:12px 25px;
        border-radius:10px;
        text-decoration:none;
        font-weight:600;
        color:#1e3a8a;
    ">Apply Now 🚀</a>
</div>
""", unsafe_allow_html=True)
