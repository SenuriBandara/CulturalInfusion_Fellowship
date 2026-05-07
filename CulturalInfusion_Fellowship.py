import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

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

/* BOXES */
.card, .small-card, .price-box, .cta {
    background: linear-gradient(120deg, #0b1220, #1e3a8a);
    color: white;
    border-radius: 16px;
    padding: 20px;
}

/* CTA */
.cta {
    text-align: center;
    padding: 80px 50px;
    margin-top: 50px;
}

/* APPLY BUTTON */
.apply-container {
    text-align: center;
    margin-top: 40px;
}

.apply-btn {
    display: inline-block;
    background: white;
    color: #1e3a8a;
    padding: 12px 28px;
    border-radius: 10px;
    font-weight: 600;
    text-decoration: none;
}

.apply-btn:hover {
    background: #e2e8f0;
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
<div class="card">
<h2>Program Overview</h2>
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
st.markdown("## Learning & Experience")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <b>Professional Development</b><br><br>
    Internship experience<br>
    Skill building<br>
    Career readiness<br>
    Leadership growth
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <b>Global Exposure</b><br><br>
    Cultural immersion<br>
    Networking<br>
    Collaboration<br>
    Real-world experience
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# CTA
# =========================
st.markdown("""
<div class="cta">
    <h2>Begin Your Global Journey</h2>
    <p>Join Cultural Infusion Fellowship and unlock global opportunities.</p>
</div>
""", unsafe_allow_html=True)

# ✅ SAFE NAVIGATION (NO ERRORS EVER)
st.markdown("""
<div class="apply-container">
    <a class="apply-btn" href="/apply">Apply Now 🚀</a>
</div>
""", unsafe_allow_html=True)
