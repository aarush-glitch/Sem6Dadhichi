import streamlit as st
import streamlit_option_menu as option_menu
import firebase_admin
import datetime
from firebase_admin import credentials, auth, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("dadhichi-login-e531cfc68a8a.json")  # Replace with your key
    firebase_admin.initialize_app(cred)
    # db = firestore.client()


if 'username' not in st.session_state:
    st.session_state.username = ''
if 'useremail' not in st.session_state:
    st.session_state.useremail = ''

def signup_user(name, email, password, username):
    try:
        user = auth.create_user(email=email, password=password, uid=username)
        st.success("User created successfully")
        st.balloons()
        # db.collection("users").document(user.uid).set({
        #     "name": name,
        #     "email": email,
        #     "username": username,
        #     "created_at": datetime.datetime.now()
        # })
    except Exception as e:
        st.error(f"Error creating user: {e}")


def login_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        
        # maintain email user id for sesion state
        st.session_state.username = user.uid
        st.session_state.useremail = user.email
        st.session_state.signedout = True
        st.session_state.signout = True
        st.success(f"Logged in as {user.uid}")
        
    except Exception as e:
        st.error(f"Error loggin in: {e}")
        # api_key = ""
        # payload = {
        #     "email": email,
        #     "password": password,
        #     "returnSecureToken": True
        # }
        # r = requests.post(f"")

def signout_user():
    st.session_state.signedout = False
    st.session_state.signout = False
    st.session_state.username = ''
    st.session_state.useremail = ''


st.title("🔐 Account")

if 'signedout' not in st.session_state:
    st.session_state.signedout = False
if 'signout' not in st.session_state:
    st.session_state.signout = False

if not st.session_state['signedout']:
    option = st.selectbox("Choose an option", ["Login", "Create Account"])    

    if option == "Create Account":
        st.subheader("Create New Account")
        name = st.text_input("Name")
        email = st.text_input("Email")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Sign Up"):
            if name and email and username and password:
                signup_user(name, email, password, username)
            else:
                st.warning("Please fill in all fields")

    elif option == "Login":
        st.subheader("Login to Your Account")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            login_user(email, password)

if st.session_state['signout']:
    st.text(f"Welcome {st.session_state.username}")
    st.text(f"Email: {st.session_state.useremail}")
    st.button("Sign Out", on_click=signout_user)
