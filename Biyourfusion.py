# Import necessary libraries
import streamlit as st
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
st.title("🌱 BiYourFusion Mobile Health App")
st.write("Welcome to your personal health and wellness management app. Track your daily health insights, set goals, monitor your progress, and store your health records.")

# Function to display the introduction
def show_intro():
    st.title("WhyBiyourFusion 🌟")
    st.markdown("""
        **BiyouFusion** is an all-in-one health and wellness app designed for maximum convenience and efficiency. 
        Unlike competitors like **MyFitnessPal**, **OurApp**, and **Apple Health**, BiyouFusion consolidates multiple essential features 
        into one platform, helping you track your health goals, fitness, menstrual cycles, and medical records effortlessly.

        ### Key Features:
        - **Health Goals**: Track weight, calorie intake, and nutrition.
        - **Menstrual Cycle**: Log phases, ovulation, contraceptives, and receive tailored tips.
        - **Fitness & Exercise**: Log workouts, monitor activity trends, access workout videos, and create personalized plans.
        - **Health Records**: Upload, update, and share health and immunization records with healthcare providers anytime.

        BiyouFusion makes it easier to manage your health and fitness in one place, offering **convenience, efficiency**, and **easy access** to important health information.
    """)

# Sidebar for navigation with icons
st.sidebar.title("🌐 Navigation")
app_mode = st.sidebar.selectbox("Choose a section", [
    "Home", "Why Biyoufusion", "Log Health Metrics", "Log Menstrual Cycle", 
    "Fitness & Exercise", "View Dashboard", "Set Goals", "Health Records", "Immunization Records", 
    "Terms of Service and Privacy Policy"
])

# Date in Sidebar
st.sidebar.write("### 📅 Current Date")
st.sidebar.write(date.today())

# Home Page with tiles
if app_mode == "Home":
    st.subheader("Welcome to your Health Dashboard")
    st.write("Use this app to log daily health metrics and track your progress over time.")
    
    # Placeholder for health metrics
    steps_today = 0  # Fetch from data storage or user input
    water_intake = 0  # Fetch from data storage or user input
    sleep_hours = 0  # Fetch from data storage or user input
    
    # Create a row of tiles for key metrics
    st.markdown(f"""
    <div class="tile">🚶 Steps Today: {steps_today}</div>
    <div class="tile">💧 Water Intake: {water_intake} oz</div>
    <div class="tile">💤 Sleep: {sleep_hours} hrs</div>
    """, unsafe_allow_html=True)

# Log Health Metrics Page with icons and styles
elif app_mode == "Log Health Metrics":
    st.subheader("Log Daily Health Metrics 🩺")
    
    # Log health metrics
    steps = st.number_input("Steps Walked Today", min_value=0, max_value=50000, step=100)
    sleep = st.number_input("Hours of Sleep", min_value=0.0, max_value=24.0, step=0.5)
    water_intake = st.number_input("Water Intake (oz)", min_value=0, max_value=300, step=1)
    
    if st.button("Save Entry"):
        st.success("Health metrics logged successfully!")
        # Here, you can save the data to a local file or database for future use
        st.write(f"**Steps:** {steps} steps")
        st.write(f"**Sleep:** {sleep} hrs")
        st.write(f"**Water Intake:** {water_intake} oz")

# Log Menstrual Cycle Page with enhanced features and tips
elif app_mode == "Log Menstrual Cycle":
    st.subheader("Log Menstrual Cycle 🌸")

    # Cycle tracking inputs
    cycle_start = st.date_input("Start Date")
    cycle_end = st.date_input("End Date", min_value=cycle_start)
    cycle_length = (cycle_end - cycle_start).days
    st.write(f"Cycle Length: {cycle_length} days")

    # Ovulation tracking
    ovulation_date = st.date_input("Ovulation Date (estimated)", min_value=cycle_start, max_value=cycle_end)
    st.write(f"Estimated Ovulation Date: {ovulation_date}")

    # Contraceptive use tracking
    contraceptive_type = st.selectbox("Select Contraceptive Method", [
        "None", "Birth Control Pill", "IUD", "Condom", "Natural Rhythm Method", "Other"
    ])
    contraceptive_notes = st.text_area("Additional Notes on Contraceptive Use (if any)")

    # Conception and sexual activity tracking
    trying_to_conceive = st.radio("Are you trying to conceive?", ["Yes", "No"])
    had_unprotected_sex = st.radio("Did you have unprotected sex this cycle?", ["Yes", "No"])
    unprotected_sex_dates = st.text_area("Dates of Unprotected Sex (if applicable, format: YYYY-MM-DD)")

    # Save button
    if st.button("Save Cycle Data"):
        st.success("Menstrual cycle data logged successfully!")
        st.write("### Summary of Recorded Data")
        st.write(f"- Cycle Start Date: {cycle_start}")
        st.write(f"- Cycle End Date: {cycle_end}")
        st.write(f"- Cycle Length: {cycle_length} days")
        st.write(f"- Estimated Ovulation Date: {ovulation_date}")
        st.write(f"- Contraceptive Method: {contraceptive_type}")
        st.write(f"- Contraceptive Notes: {contraceptive_notes}")
        st.write(f"- Trying to Conceive: {trying_to_conceive}")
        st.write(f"- Unprotected Sex: {had_unprotected_sex}")
        if had_unprotected_sex == "Yes" and unprotected_sex_dates:
            st.write(f"- Dates of Unprotected Sex: {unprotected_sex_dates}")

    # Menstrual phase tips
    st.write("### Tips for Each Phase of the Menstrual Cycle")
    phase = st.radio("Select a Cycle Phase to Learn More", [
        "Menstrual Phase", "Follicular Phase", "Ovulation Phase", "Luteal Phase"
  
