import pyrebase
import streamlit as st
from datetime import datetime
import os
import sys
from PIL import Image


# Firebase configuration
firebaseConfig = {
    'apiKey': "AIzaSyBzCk6aPK_YZf2J2HsA-o4VDCMTum7k8hU",
    'authDomain': "dadhichi-bcd1c.firebaseapp.com",
    'projectId': "dadhichi-bcd1c",
    'storageBucket': "dadhichi-bcd1c.firebasestorage.app",
    'messagingSenderId': "910382895233",
    'appId': "1:910382895233:web:c945002be32152b996bd80",
    'databaseURL': ""
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Streamlit page configuration
st.set_page_config(page_title="Login / Sign Up", page_icon="🔑")

# Sidebar selection for login or sign up
choice = st.sidebar.selectbox('Login / Sign Up', ['Login', 'Sign Up'])

# Input fields for email and password
email = st.sidebar.text_input('Email')
password = st.sidebar.text_input('Password', type='password')

# Function for handling login
def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        st.success("Login successful! Redirecting to DADHICHI...")
        os.system("streamlit run Home.py")
        st.experimental_rerun()
        return user
    except Exception as e:
        st.error(f"Login failed: {e}")
        return None

# Function for handling sign-up
def sign_up_user(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        st.success("Sign up successful! Please check your email for verification.")
        auth.send_email_verification(user['idToken'])
        return user
    except Exception as e:
        st.error(f"Sign up failed: {e}")
        return None

# Handling logic for login or sign up
if choice == 'Login':
    if st.sidebar.button('Login'):
        if email and password:
            login_user(email, password)
        else:
            st.warning("Please enter both email and password to log in.")

elif choice == 'Sign Up':
    if st.sidebar.button('Sign Up'):
        if email and password:
            sign_up_user(email, password)
        else:
            st.warning("Please enter both email and password to sign up.")

# Displaying large image on the main page
st.write("# Welcome to Dadhichi")
st.markdown("<h5>Your one-stop fitness solution</h5>", unsafe_allow_html=True)

logo = Image.open("./images/dadhichi.png")
st.image(logo, width=1200)

# Additional UI for logged-in users
if st.session_state.get('user', None):
    st.write("You are logged in.")
