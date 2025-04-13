import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd
import random


# Function to load Lottie animations
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        return None


# Lottie animations
lottie_events = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_u4yrau.json")
lottie_progress = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_2szqu88a.json")
lottie_community = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_i8xxlqfs.json")

# Page setup
st.set_page_config(page_title="Community Engagement", page_icon="🌟", layout="wide")

# Header Section
with st.container():
    st.markdown(
        """
        <div style="background-color:#2F4F4F;padding:10px;border-radius:10px;">
        <h1 style="color:white;text-align:center;">Community Engagement</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        """
        Join the fitness revolution with your friends and compete in exciting challenges! 
        Track your progress, climb the leaderboard, and earn rewards in our vibrant fitness community.
        """
    )

# ---- EVENTS SECTION ----
with st.container():
    st.write("---")
    st.header("🎉 Events and Challenges")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Current Highlight: Step Count Hierarchy")
        st.write(
            """
            Compete with your friends to see who takes the most steps in a week!  
            The top 3 participants receive exciting rewards, including gift cards, fitness equipment, or a free subscription to our AI Fitness Coach.
            
            🌟 **Start Date:** Monday  
            🏆 **End Date:** Sunday  
            🎁 **Rewards:**  
            - 🥇 1st Place: $50 Gift Card  
            - 🥈 2nd Place: Resistance Band Set  
            - 🥉 3rd Place: Fitness Water Bottle  
            """
        )
        st.markdown("**Join Now and Climb the Leaderboard!**")
    with col2:
        if lottie_events:
            st_lottie(lottie_events, height=300, key="events")

# ---- LEADERBOARD SECTION ----
with st.container():
    st.write("---")
    st.header("🏅 Leaderboard")

    # Sample leaderboard data
    leaderboard_data = {
        "Name": ["Aarush", "Neha", "Raj", "Simran", "Aditya"],
        "Steps This Week": [random.randint(7000, 15000) for _ in range(5)],
        "Rank": [1, 2, 3, 4, 5],
    }
    leaderboard_df = pd.DataFrame(leaderboard_data).sort_values(by="Steps This Week", ascending=False)

    # Display leaderboard
    st.dataframe(leaderboard_df, use_container_width=True)

# ---- PERSONAL PROGRESS SECTION ----
with st.container():
    st.write("---")
    st.header("📊 Your Progress")
    st.write(
        """
        Track your performance and compare it with your friends!
        """
    )

    col1, col2 = st.columns([2, 1])
    with col1:
        user_steps = st.slider("Your Steps This Week:", 0, 20000, 12000)
        friend_steps = random.randint(5000, 15000)
    
        st.progress(user_steps / 20000)  # Display progress bar
    
        st.write(
            f"**Your Progress:** {user_steps} steps  \n"
            f"**Your Friend's Progress:** {friend_steps} steps"
        )

    with col2:
        if lottie_progress:
            st_lottie(lottie_progress, height=300, key="progress")

# ---- COMMUNITY STATS SECTION ----
with st.container():
    st.write("---")
    st.header("🌍 Community Motivation")
    st.write(
        """
        Together, we’re stronger! Check out how our community is making strides towards fitness goals.
        """
    )
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Steps Taken This Week", value="5,678,432", delta="12% Increase")
        st.metric(label="Active Participants", value="3,245", delta="20% Increase")
    with col2:
        if lottie_community:
            st_lottie(lottie_community, height=300, key="community")
