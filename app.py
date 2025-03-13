import streamlit as st

# Page Config
st.set_page_config(page_title="Login | Yelp", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
        /* Center everything */
        .block-container { 
            max-width: 400px;
            margin-top: 2rem;
        }
        /* Logo */
        .logo {
            font-size: 28px;
            font-weight: bold;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #D32323;
            padding: 10px;
            border-radius: 10px;
        }
        .logo span {
            color: white;
        }
        /* Input fields */
        .stTextInput > div > div > input {
            border: 2px solid #ddd;
            border-radius: 8px;
            padding: 10px;
        }
        /* Buttons */
        .stButton > button {
            width: 100%;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
            background-color: #D32323;
            color: white;
            border: none;
        }
        .stButton > button:hover {
            background-color: #B71C1C;
        }
        .google-btn {
            background: #fff;
            color: black;
            border: 1px solid #ddd;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 10px;
            width: 100%;
            border-radius: 8px;
            font-size: 16px;
            margin-top: 10px;
            cursor: pointer;
        }
        .google-btn img {
            width: 20px;
            margin-right: 10px;
        }
        /* Footer */
        .footer {
            text-align: center;
            margin-top: 20px;
            font-size: 14px;
        }
        .footer a {
            color: #D32323;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)


# Logo
st.markdown('<div class="logo">YELP</div>', unsafe_allow_html=True)

# Title
st.markdown("## Welcome back")
st.markdown("Please enter your details")

# Login Form
email = st.text_input("Email address")
password = st.text_input("Password", type="password")
remember_me = st.checkbox("Remember for 30 days")

col1, col2 = st.columns([1, 1])
with col1:
    pass
with col2:
    st.markdown('<a href="#" style="text-decoration: none; color: yellow;">Forgot password</a>', unsafe_allow_html=True)


# Sign In Button
if st.button("Sign in", key="signin"):
    if email and password:
        st.success("Logged in successfully!")
    else:
        st.error("Please enter valid credentials.")

# Google Sign In Button
st.markdown(
    '<div class="google-btn"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/512px-Google_%22G%22_Logo.svg.png"> Sign in with Google</div>',
    unsafe_allow_html=True,
)

# Footer (Sign up option)
st.markdown('<div class="footer">Don’t have an account? <a href="#">Sign up</a></div>', unsafe_allow_html=True)





