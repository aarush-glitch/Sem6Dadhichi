import streamlit as st

# Function to generate a workout plan based on user inputs
def generate_workout_plan(goal, duration, intensity, location, track=None):
    # Define workout routines
    workout_plans = {
        'lose weight': {
            'gym': ["Left Dumbbell", "Right Dumbbell", "Squats", "Pushups", "Shoulder Press"],
            'yoga': {
                'track 1': ["Pranamasana", "Eka Pada Pranamasana", "Ashwa Sanchalanasana"],
                'track 2': ["Ardha Chakrasana", "Utkatasana (Chair Pose)", "Veerabhadrasana 2 (Warrior 2 Pose)"]
            }
        },
        'build muscle': {
            'gym': ["Squats", "Pushups", "Shoulder Press", "Left Dumbbell", "Right Dumbbell"],
        },
        'improve endurance': {
            'gym': ["Squats", "Pushups", "Shoulder Press"],
            'yoga': {
                'track 1': ["Pranamasana", "Eka Pada Pranamasana", "Ashwa Sanchalanasana"],
                'track 2': ["Ardha Chakrasana", "Utkatasana (Chair Pose)", "Veerabhadrasana 2 (Warrior 2 Pose)"]
            }
        },
        'general fitness': {
            'gym': ["Left Dumbbell", "Right Dumbbell", "Pushups", "Squats", "Shoulder Press"],
            'yoga': {
                'track 1': ["Pranamasana", "Eka Pada Pranamasana", "Ashwa Sanchalanasana"],
                'track 2': ["Ardha Chakrasana", "Utkatasana (Chair Pose)", "Veerabhadrasana 2 (Warrior 2 Pose)"]
            }
        }
    }

    # Select exercises based on the inputs
    if location == "Gym":
        exercises = workout_plans[goal]['gym']
    elif location == "Yoga" and track:
        exercises = workout_plans[goal]['yoga'][track.lower()]
    else:
        return "Please select a valid option!"

    # Create a detailed workout plan
    plan = f"Your {goal} workout plan for {duration} minutes at {location}:\n\n"
    for i, exercise in enumerate(exercises, 1):
        plan += f"{i}. {exercise} - {intensity.capitalize()} intensity - 3 sets of 10-12 reps\n"

    return plan

# Streamlit UI
st.title("Personalized Workout Plan Generator")

# Collect user inputs
goal = st.selectbox("Choose your fitness goal:", ["Lose weight", "Build muscle", "Improve Endurance", "General fitness"]).lower()
duration = st.slider("How much time do you have for your workout?", 15, 120, 30)
intensity = st.selectbox("Select workout intensity:", ["low", "medium", "high"]).lower()
location = st.selectbox("Where will you work out?", ["Gym", "Yoga"])

# Show track options if Yoga is selected
track = None
if location == "Yoga":
    track = st.selectbox("Choose your yoga track:", ["Track 1", "Track 2"])

# Generate and display workout plan
if st.button("Generate Workout Plan"):
    workout_plan = generate_workout_plan(goal, duration, intensity, location, track)
    st.text(workout_plan)
