import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import date, datetime, timedelta

# CSS styling
st.markdown("""
    <style>
        .main {background-color: #f0f2f6;} /* Light gray background for main content */
        .sidebar .sidebar-content {background-color: #e3f2fd;} /* Light blue background for sidebar */
        .icon {
            font-size: 2em; /* Icon size */
            color: #2196F3; /* Icon color */
            margin-right: 10px;
        }
        .tile {
            background-color: #90caf9; /* Light blue background for tiles */
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
            color: #fff;
            text-align: center;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Set up the app title and description
st.title("🌱 Digital Mobile Health App")
st.write("Welcome to your personal health and wellness management app. Track your health metrics, set goals, and monitor your progress.")

# Sidebar for navigation with icons
st.sidebar.title("🌐 Navigation")
app_mode = st.sidebar.selectbox("Choose a section", [
    "Home", "Log Health Metrics", "Log Menstrual Cycle", "Log Diet & Exercise", "View Dashboard",
    "Set Goals", "Health Records", "Terms of Service and Privacy Policy"
])

# Date in Sidebar
st.sidebar.write("### 📅 Current Date")
st.sidebar.write(date.today())

# Home Page with tiles
if app_mode == "Home":
    st.subheader("Welcome to your Health Dashboard")
    st.write("Use this app to log daily health metrics and track your progress over time.")
    
    # Create a row of tiles for key metrics
    st.markdown(f"""
    <div class="tile">🚶 Steps Today: {0}</div>
    <div class="tile">💧 Water Intake: {0} oz</div>
    <div class="tile">💤 Sleep: {0} hrs</div>
    """, unsafe_allow_html=True)

# Log Health Metrics Page with icons and styles
elif app_mode == "Log Health Metrics":
    st.subheader("Log Daily Health Metrics 🩺")
    
    steps = st.number_input("Steps Walked Today", min_value=0, max_value=50000, step=100)
    sleep = st.number_input("Hours of Sleep", min_value=0.0, max_value=24.0, step=0.5)
    water_intake = st.number_input("Water Intake (oz)", min_value=0, max_value=300, step=1)
    
    if st.button("Save Entry"):
        # Append to the data
        st.success("Health metrics logged successfully!")

# Log Menstrual Cycle Page
elif app_mode == "Log Menstrual Cycle":
    st.subheader("Log Menstrual Cycle 🌸")
    cycle_start = st.date_input("Start Date")
    cycle_end = st.date_input("End Date", min_value=cycle_start)
    cycle_length = (cycle_end - cycle_start).days
    st.write("Cycle Length:", cycle_length, "days")
    if st.button("Save Cycle Data"):
        st.success("Menstrual cycle data logged successfully!")

# Log Diet & Exercise Page
elif app_mode == "Log Diet & Exercise":
    st.subheader("Log Diet & Exercise 🍎")
    meals = st.text_area("Enter Meals & Calories (e.g., Breakfast: 300, Lunch: 500)")
    total_calories = sum([int(line.split(": ")[1]) for line in meals.splitlines() if ": " in line])
    st.write("Total Calories Consumed:", total_calories, "kcal")
    
    exercise_type = st.selectbox("Exercise Type", ["Running", "Cycling", "Yoga", "Weight Lifting", "Other"])
    duration = st.slider("Duration (minutes)", 0, 180)
    heart_rate = st.slider("Heart Rate (bpm)", 60, 200)
    calories_burned = duration * (heart_rate / 10)
    st.write("Calories Burned:", calories_burned, "kcal (estimated)")
    
    if st.button("Save Diet & Exercise Data"):
        st.success("Diet and exercise data logged successfully!")

# View Dashboard Page with chart
elif app_mode == "View Dashboard":
    st.subheader("Health Dashboard 📊")
    st.write("View your health metrics over time.")
    df = pd.DataFrame({
        "Date": [date.today()],
        "Steps": [0],
        "Sleep (hrs)": [0],
        "Water Intake (oz)": [0],
        "Calories Consumed": [0],
        "Calories Burned": [0],
        "Heart Rate (bpm)": [0]
    })
    st.line_chart(df.set_index("Date"))

# Set Goals Page
elif app_mode == "Set Goals":
    st.subheader("Set Health Goals 🎯")
    goal_steps = st.number_input("Daily Steps Goal", min_value=0, max_value=50000, step=100, value=10000)
    goal_sleep = st.number_input("Daily Sleep Goal (hours)", min_value=0.0, max_value=24.0, step=0.5, value=8.0)
    goal_water = st.number_input("Daily Water Intake Goal (oz)", min_value=0, max_value=300, step=1, value=64)
    
    if st.button("Save Goals"):
        st.success("Goals saved successfully!")
        st.write(f"Your daily goals: {goal_steps} steps, {goal_sleep} hours of sleep, {goal_water} oz of water.")

# Health Records Page
elif app_mode == "Health Records":
    st.subheader("Log Health Records 📋")
    conditions = st.text_area("Existing Health Conditions")
    allergies = st.text_area("Known Allergies")
    if st.button("Save Health Records"):
        st.success("Health records saved successfully!")

# Terms of Service and Privacy Policy
elif app_mode == "Terms of Service and Privacy Policy":
    st.subheader("Terms of Service 📜")
    st.write("By using this app, you agree to the following terms...")
    st.subheader("Privacy Policy 🔒")
    st.write("Your privacy is important to us. We are committed to safeguarding any information you share.")

# Terms of Service and Privacy Policy
elif app_mode == "Terms of Service and Privacy Policy":
    st.subheader("Terms of Service 📜")
    st.write("""
    By using this app, you agree to abide by the terms and conditions outlined below. These terms govern your use of the application and the services provided.
    """)

    st.subheader("Privacy Policy 🔒")
    st.write("""
    **Your privacy matters to us.**
    
    We are committed to protecting your personal information and ensuring that it is handled securely. Here’s how we safeguard your data:
    - **Data Transparency:** You own your data, and we provide clear explanations about how it is used.
    - **Security Measures:** Your information is stored securely and encrypted to prevent unauthorized access.
    - **No Unauthorized Sharing:** We do not sell or share your data with third parties without your consent.
    
    For more details, please review our comprehensive [Privacy Policy](#).
    """)


