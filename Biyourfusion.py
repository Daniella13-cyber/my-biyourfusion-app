import streamlit as st
import pandas as pd
from datetime import date

# Set up the app title and description
st.title("Digital Mobile Health App")
st.write("Welcome to your personal health and wellness management app. Track your health metrics, set goals, and monitor your progress.")

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose a section", ["Home", "Log Health Metrics", "View Dashboard", "Set Goals"])

# Dummy data for demonstration
data = {
    "Date": [date.today()],
    "Steps": [0],
    "Sleep (hrs)": [0],
    "Water Intake (oz)": [0]
}

# Home Page
if app_mode == "Home":
    st.subheader("Welcome to your Health Dashboard")
    st.write("Use this app to log daily health metrics and track your progress over time.")

# Log Health Metrics Page
elif app_mode == "Log Health Metrics":
    st.subheader("Log Health Metrics")
    
    steps = st.number_input("Steps Walked Today", min_value=0, max_value=50000, step=100)
    sleep = st.number_input("Hours of Sleep", min_value=0.0, max_value=24.0, step=0.5)
    water_intake = st.number_input("Water Intake (oz)", min_value=0, max_value=300, step=1)
    
    if st.button("Save Entry"):
        # Append to the data
        data["Date"].append(date.today())
        data["Steps"].append(steps)
        data["Sleep (hrs)"].append(sleep)
        data["Water Intake (oz)"].append(water_intake)
        st.success("Health metrics logged successfully!")

# View Dashboard Page
elif app_mode == "View Dashboard":
    st.subheader("Health Dashboard")
    st.write("View your health metrics over time.")
    
    df = pd.DataFrame(data)
    st.line_chart(df.set_index("Date"))
    st.write(df)

# Set Goals Page
elif app_mode == "Set Goals":
    st.subheader("Set Health Goals")
    
    st.write("Define your personal health goals.")
    goal_steps = st.number_input("Daily Steps Goal", min_value=0, max_value=50000, step=100, value=10000)
    goal_sleep = st.number_input("Daily Sleep Goal (hours)", min_value=0.0, max_value=24.0, step=0.5, value=8.0)
    goal_water = st.number_input("Daily Water Intake Goal (oz)", min_value=0, max_value=300, step=1, value=64)
    
    if st.button("Save Goals"):
        st.write("Goals saved successfully!")
        st.write(f"Your daily goals: {goal_steps} steps, {goal_sleep} hours of sleep, {goal_water} oz of water.")

st.sidebar.write("### Current Date")
st.sidebar.write(date.today())
