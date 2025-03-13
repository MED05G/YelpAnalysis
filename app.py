import streamlit as st

# Custom CSS for styling
st.markdown("""
<style>
    .header {
        font-size: 32px;
        font-weight: bold;
        color: #4CAF50; /* Green color */
        margin-bottom: 10px;
    }
    .welcome-back {
        font-size: 24px;
        font-weight: bold;
        color: #333333; /* Dark gray color */
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="header">ShipStat</div>', unsafe_allow_html=True)
st.markdown('<div class="welcome-back">Welcome back, Angela</div>', unsafe_allow_html=True)