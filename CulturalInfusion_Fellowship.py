import streamlit as st
import pandas as pd
import plotly.express as px


# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="Cultural Infusion Internships Dashboard",
    layout="wide"
)


# ---------------------------------
# Title
# ---------------------------------

st.title("Cultural Infusion Internships Dashboard")


# ---------------------------------
# Load SharePoint Excel Dashboard
# ---------------------------------

url = "YOUR_SHAREPOINT_EXCEL_LINK"


dashboard = pd.read_excel(
    url,
    sheet_name="Dashboard",
    header=None
)


# ---------------------------------
# Extract KPI Data
# ---------------------------------

total_leadgen = dashboard.iloc[2,0]
total_applied = dashboard.iloc[2,1]
total_interview = dashboard.iloc[2,2]
total_accepted = dashboard.iloc[2,3]
total_payment = dashboard.iloc[2,4]


# ---------------------------------
# KPI Cards
# ---------------------------------

st.subheader("Pipeline Overview")


col1, col2, col3, col4, col5 = st.columns(5)


col1.metric(
    "Total Leadgen",
    total_leadgen
)

col2.metric(
    "Total Applied",
    total_applied
)

col3.metric(
    "Interview Done",
    total_interview
)

col4.metric(
    "Total Accepted",
    total_accepted
)

col5.metric(
    "Payment Done",
    total_payment
)



# ---------------------------------
# Funnel Chart
# ---------------------------------

st.subheader("Internship Pipeline Funnel")


funnel_data = pd.DataFrame(
    {
        "Stage":[
            "Leadgen",
            "Applied",
            "Interview Done",
            "Accepted",
            "Payment Done"
        ],

        "Count":[
            total_leadgen,
            total_applied,
            total_interview,
            total_accepted,
            total_payment
        ]
    }
)


fig = px.funnel(
    funnel_data,
    x="Count",
    y="Stage"
)


st.plotly_chart(
    fig,
    use_container_width=True
)



# ---------------------------------
# Conversion Rates
# ---------------------------------

st.subheader("Conversion Performance")


leadgen_applied = dashboard.iloc[18,0]
applied_interview = dashboard.iloc[18,1]
interview_accepted = dashboard.iloc[18,2]
accepted_paid = dashboard.iloc[18,3]
leadgen_paid = dashboard.iloc[18,4]
applied_paid = dashboard.iloc[18,5]



c1,c2,c3,c4,c5,c6 = st.columns(6)


c1.metric(
    "Leadgen → Applied",
    leadgen_applied
)

c2.metric(
    "Applied → Interview",
    applied_interview
)

c3.metric(
    "Interview → Accepted",
    interview_accepted
)

c4.metric(
    "Accepted → Paid",
    accepted_paid
)

c5.metric(
    "Leadgen → Paid",
    leadgen_paid
)

c6.metric(
    "Applied → Paid",
    applied_paid
)



# ---------------------------------
# Data Preview (Optional)
# ---------------------------------

with st.expander("View Dashboard Data"):
    st.dataframe(
        dashboard
    )
