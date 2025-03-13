import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit Setup
st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        width: 100%;
        margin: 5px 0;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        color: white;
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .card-blue {
        background-color: #e7f3ff;
        border-left: 5px solid #007bff;
    }
    .card-green {
        background-color: #e7ffe7;
        border-left: 5px solid #28a745;
    }
    .card-header {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .card-content {
        font-size: 14px;
        margin-bottom: 10px;
    }
    .card-button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
    }
    .card-button:hover {
        background-color: #0056b3;
    }
    .top-nav {
        display: flex;
        justify-content: space-around;
        background-color: #007bff;
        padding: 10px;
    }
    .top-nav a {
        color: white;
        text-decoration: none;
        font-size: 18px;
    }
    .top-nav a:hover {
        color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown("<h1 style='text-align: center;'>Welcome back, Angela</h1>", unsafe_allow_html=True)

# Quick Actions Row
st.markdown("<h2>Quick Actions</h2>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("Request Money")
with col2:
    st.button("Record Expense")
with col3:
    st.button("Add Property")
with col4:
    st.button("Add Tenant")

# Main Content Area
col1, col2 = st.columns([3, 1])

with col1:
    # Items to Complete Section
    st.markdown("<h2>Items To Complete</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="card card-blue">
            <div class="card-header">Verify Your Identity Securely</div>
            <div class="card-content">Provide your address for verification. This information is secure and won't be shared with tenants.</div>
            <button class="card-button">Complete Verification</button>
        </div>
        """, unsafe_allow_html=True)

    # Marketing & Leasing Section
    st.markdown("<h2>Marketing & Leasing</h2>", unsafe_allow_html=True)
    col1_1, col1_2 = st.columns(2)
    with col1_1:
        st.markdown("""
            <div class="card">
                <div class="card-header">Prospective Tenants</div>
                <div class="card-content">Details about prospective tenants...</div>
            </div>
            <div class="card">
                <div class="card-header">Expiring Leases</div>
                <div class="card-content">Details about expiring leases...</div>
            </div>
            """, unsafe_allow_html=True)
    with col1_2:
        st.markdown("""
            <div class="card">
                <div class="card-header">Lease Assist</div>
                <div class="card-content">Details about lease assist...</div>
            </div>
            <div class="card">
                <div class="card-header">Lease Assist</div>
                <div class="card-content">Details about lease assist...</div>
            </div>
            """, unsafe_allow_html=True)

    # Report Dates Section
    st.markdown("<h2>Report Dates</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="card">
            <div class="card-content">28 Nov 2024</div>
            <div class="card-content">01 Jan 2025</div>
        </div>
        """, unsafe_allow_html=True)

    # Referral Section
    st.markdown("""
        <div class="card card-green">
            <div class="card-header">Refer & Earn $250!</div>
            <div class="card-content">Invite your friends and get $250 for each successful referral. Start sharing today!</div>
            <button class="card-button">Share Now</button>
        </div>
        """, unsafe_allow_html=True)

    # Messages Section
    st.markdown("<h2>Unread Messages (01)</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="card">
            <div class="card-header">Emergency Oasis <span style="color: red;">●</span></div>
            <div class="card-content">5 mins ago</div>
            <div class="card-content">Hello, I hope you're doing well! I've come across...</div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    # Financial Sidebar
    st.markdown("<h2>Financial Overview</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="card">
            <div class="card-header">$288 (This month)</div>
            <div class="card-content">$300</div>
            <div class="card-content">$250</div>
            <div class="card-content">$150</div>
            <div class="card-content">$100</div>
            <div class="card-content">$50</div>
            <div class="card-content">$0</div>
        </div>
        """, unsafe_allow_html=True)

    # Chart
    st.markdown("<h2>Monthly Revenue</h2>", unsafe_allow_html=True)
    chart_data = pd.DataFrame({
        'Month': ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        'Revenue': [200, 300, 400, 500, 600, 700]
    })
    fig = px.line(chart_data, x='Month', y='Revenue', title='Monthly Revenue')
    st.plotly_chart(fig, use_container_width=True)