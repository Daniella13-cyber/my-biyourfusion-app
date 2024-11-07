Certainly! Adding icons to the navigation menu can enhance the user experience by providing visual cues. Streamlit allows the use of emojis, which work well as quick and lightweight icons. Here’s how you can add icons to each menu item using emoji codes.

### Updated Code with Icons in Navigation Menu

```python
import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta

# Set up the app title and description
st.title("Digital Mobile Health App")
st.write("Welcome to your personal health and wellness management app. Track your health metrics, set goals, and monitor your progress.")

# Sidebar for navigation with icons
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox(
    "Choose a section", 
    [
        "🏠 Home", 
        "📊 Log Health Metrics", 
        "📅 Log Menstrual Cycle", 
        "🍎 Log Diet & Exercise", 
        "📈 View Dashboard", 
        "🎯 Set Goals", 
        "📝 Health Records", 
        "⚖️ Terms of Service and Privacy Policy"
    ]
)

# Dummy data for demonstration
data = {
    "Date": [date.today()],
    "Steps": [0],
    "Sleep (hrs)": [0],
    "Water Intake (oz)": [0],
    "Calories Consumed": [0],
    "Calories Burned": [0],
    "Heart Rate (bpm)": [0]
}

# Home Page
if app_mode == "🏠 Home":
    st.subheader("Welcome to your Health Dashboard")
    st.write("Use this app to log daily health metrics and track your progress over time.")

# Log Health Metrics Page
elif app_mode == "📊 Log Health Metrics":
    st.subheader("Log Daily Health Metrics")
    
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

# Log Menstrual Cycle Page
elif app_mode == "📅 Log Menstrual Cycle":
    st.subheader("Log Menstrual Cycle")
    cycle_start = st.date_input("Start Date")
    cycle_end = st.date_input("End Date", min_value=cycle_start)
    cycle_length = (cycle_end - cycle_start).days
    st.write("Cycle Length:", cycle_length, "days")
    if st.button("Save Cycle Data"):
        st.success("Menstrual cycle data logged successfully!")

# Log Diet & Exercise Page
elif app_mode == "🍎 Log Diet & Exercise":
    st.subheader("Log Diet & Exercise")
    
    # Diet & Calorie Counting
    st.write("### Diet & Calorie Counting")
    meals = st.text_area("Enter Meals & Calories (e.g., Breakfast: 300, Lunch: 500)")
    total_calories = sum([int(line.split(": ")[1]) for line in meals.splitlines() if ": " in line])
    st.write("Total Calories Consumed:", total_calories, "kcal")
    
    # Exercise & Heart Rate
    st.write("### Exercise & Heart Rate")
    exercise_type = st.selectbox("Exercise Type", ["Running", "Cycling", "Yoga", "Weight Lifting", "Other"])
    duration = st.slider("Duration (minutes)", 0, 180)
    heart_rate = st.slider("Heart Rate (bpm)", 60, 200)
    calories_burned = duration * (heart_rate / 10)  # Basic estimation
    st.write("Calories Burned:", calories_burned, "kcal (estimated)")
    
    if st.button("Save Diet & Exercise Data"):
        data["Calories Consumed"].append(total_calories)
        data["Calories Burned"].append(calories_burned)
        data["Heart Rate (bpm)"].append(heart_rate)
        st.success("Diet and exercise data logged successfully!")

# View Dashboard Page
elif app_mode == "📈 View Dashboard":
    st.subheader("Health Dashboard")
    st.write("View your health metrics over time.")
    
    df = pd.DataFrame(data)
    st.line_chart(df.set_index("Date"))
    st.write(df)

# Set Goals Page
elif app_mode == "🎯 Set Goals":
    st.subheader("Set Health Goals")
    
    st.write("Define your personal health goals.")
    goal_steps = st.number_input("Daily Steps Goal", min_value=0, max_value=50000, step=100, value=10000)
    goal_sleep = st.number_input("Daily Sleep Goal (hours)", min_value=0.0, max_value=24.0, step=0.5, value=8.0)
    goal_water = st.number_input("Daily Water Intake Goal (oz)", min_value=0, max_value=300, step=1, value=64)
    
    if st.button("Save Goals"):
        st.write("Goals saved successfully!")
        st.write(f"Your daily goals: {goal_steps} steps, {goal_sleep} hours of sleep, {goal_water} oz of water.")

# Health Records Page
elif app_mode == "📝 Health Records":
    st.subheader("Log Health Records")
    
    # Health Conditions and Allergies
    conditions = st.text_area("Existing Health Conditions")
    allergies = st.text_area("Known Allergies")
    if st.button("Save Health Records"):
        st.success("Health records saved successfully!")
        st.write("Conditions:", conditions)
        st.write("Allergies:", allergies)

# Terms of Service and Privacy Policy
elif app_mode == "⚖️ Terms of Service and Privacy Policy":
    st.subheader("Terms of Service")
    st.write("By using this app, you agree to the following terms... [Add your terms of service text here].")
    st.subheader("Privacy Policy")
    st.write("Your privacy is important to us. We are committed to safeguarding any information you share. [Add privacy policy details here].")

# Sidebar Date
st.sidebar.write("### Current Date")
st.sidebar.write(date.today())
```

### Explanation of Icons
- **🏠 Home**: Home page icon
- **📊 Log Health Metrics**: Metrics logging icon
- **📅 Log Menstrual Cycle**: Calendar icon for cycle tracking
- **🍎 Log Diet & Exercise**: Food and exercise icon
- **📈 View Dashboard**: Dashboard view icon
- **🎯 Set Goals**: Target icon for goal setting
- **📝 Health Records**: Notes icon for health records
- **⚖️ Terms of Service and Privacy Policy**: Scales icon for legal information

This will add a more visually appealing and organized look to the navigation. Each item is paired with a relevant icon for easy recognition.
