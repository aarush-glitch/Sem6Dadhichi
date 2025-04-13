import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2:3b", temperature=0)

#Streamlit UI
st.set_page_config(page_title="Dadhichi | AI Workout Planner", layout="centered")
st.title("🏋️ Dadhichi - Personalized Workout Plan Generator")

#Collect User Inputs
goal = st.selectbox("Choose your fitness goal:", ["Lose weight", "Build muscle", "Improve Endurance", "General fitness"]).lower()
duration = st.slider("How much time do you have for your workout?", 15, 120, 30)
intensity = st.selectbox("Select workout intensity:", ["Low", "Medium", "High"]).lower()
location = st.selectbox("Where will you work out?", ["Gym", "Home", "Outdoor"]).lower()
type = st.selectbox("What do you prefer, yoga or training?", ["Yoga", "Training"]).lower()

#Optional user notes
user_notes = st.text_area("Any injuries, preferences, or goals you'd like to consider?", "")

#Generate button
if st.button("Generate Plan"):
    context = f"""
    You are a certified personal trainer AI.
    Based on the user's input below, generate a personalized workout plan which includes exercises, sets, reps, and duration in case if the user chooses to train and different yoga poses in case if the user chooses to do yoga.
    Do not keep the prompt too long, make it to the point suggest exercises strictly based on user requirements, you do not need to mention an alternative to the exercise you mentioned.
    
    User goal: {goal}
    Workout duration: {duration} minutes
    Workout intensity: {intensity}
    Workout location: {location}
    Workout type: {type}
    In workout type, if yoga is selected, suggest different yoga poses based on user requirements and if training is selected, suggest different exercises based on user requirements.
    Important: If the user chooses do yoga you must not suggest them any training exercises.
    Important: If the user chooses to train you must not suggest them any yoga poses.
    Additional notes: {user_notes}
    
    Your response should include:
    1. A workout plan (Step-by-step) suited for the user input.
    2. A short motivational message to the user.
    
    """
    
    prompt = ChatPromptTemplate.from_template(context)
    chain = prompt | model
    result = chain.invoke({
        "context":context,
        "question": "Can you create a workout plan for me?"
    })
    
    st.subheader("🏋🏻‍♂️ Your Personalized Workout Plan:")
    st.markdown(result.strip())
