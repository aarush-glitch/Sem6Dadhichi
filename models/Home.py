import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import time  # For delay before redirecting
import subprocess  # For running the streamlit command

# Configure page
st.set_page_config(page_title="DADHICHI", page_icon=":tada:", layout="wide")

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./styles/styles.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_FYx0Ph.json")
music = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ikk4jhps.json")
podcast = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_JjpNLdaKYX.json")

img_contact_form = Image.open("./images/home.jpg")
img_lottie_animation = Image.open("./images/home.jpg")

# Load logo
logo = Image.open("./images/dadhichi.png")  # Replace with the correct path to your logo file

# Display logo in the header
with st.container():
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(logo, width=1000)

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hello, welcome to our website :wave:")
    st.write("Step into a fitter future: Welcome to your fitness revolution!")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    st.write("## About us :point_down:")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("")
        st.write(
            """
            - We are thrilled to have you here on our platform dedicated to empowering and inspiring individuals on their journey towards a healthier and fitter lifestyle. Whether you're a seasoned fitness enthusiast or just starting your fitness journey, we have everything you need to reach your goals and achieve the best version of yourself.
            
            - What sets us apart is the fact that we provide personalized assistance at the comfort of your home or any place of your choice at a price that is both convenient and much cheaper than traditional gyms.

            Let your fitness journey start here!
            Join us today and embark on a transformative experience that will enhance your physical and mental well-being. Let's build strength, resilience, and a healthier future together!
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Get fit, Jam on, Repeat :headphones:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.lottie(music, height=300, key="music")
    with text_column:
        st.write("##")
        st.subheader("Workout music")
        st.write(
            """
            Power up your workout with the ultimate music fuel!
            """
        )
        st.markdown("[Have a Listen...](https://open.spotify.com/playlist/6N0Vl77EzPm13GIOlEkoJn?si=9207b7744d094bd3)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.lottie(podcast, height=300, key="podcast")
    with text_column:
        st.write("##")
        st.subheader("Podcast")
        st.write(
            """
            Take your workouts to the next level with our immersive podcast that pumps you up from start to finish!
            """
        )
        st.markdown("[Have a listen...](https://open.spotify.com/playlist/09Ig7KfohF5WmU9RhbDBjs?si=jyZ79y3wQgezrEDHim0NvQ)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    # Documention: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/aarush9604@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

# ---- LOGOUT FUNCTIONALITY ----
# Session State for Authentication
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True  # Default to logged in for demonstration

# Sidebar Logout Button
st.sidebar.header("Navigation")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.sidebar.success("You have been logged out! Redirecting...")

    # Delay before redirecting to simulate smooth transition
    time.sleep(2)

    # Run the `streamlit run Account.py` command to open Account.py
    subprocess.run(["streamlit", "run", "Account.py"])  # This will run Account.py after logout

    # Stop the execution of Home.py
    st.stop()  # Prevent further execution after logout
