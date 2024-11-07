import streamlit as st
import pandas as pd
from datetime import date

# Apply custom CSS for colors, gradients, and layout styling
st.markdown("""
    <style>
        /* Colors */
        :root {
            --white: #ffffffff;
            --madder: #a41623ff;
            --orange-pantone: #f85e00ff;
            --olive: #918450ff;
            --keppel: #60ab9aff;
        }

        /* Gradient Background */
        .app-container {
            background: linear-gradient(135deg, var(--madder), var(--orange-pantone), var(--olive), var(--keppel));
            padding: 20px;
            border-radius: 10px;
            color: var(--white);
        }

        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: var(--madder);
            color: var(--white);
        }

        /* Tile/Card styling */
        .metric-tile {
            background: var(--orange-pantone);
            padding: 20px;
            border-radius: 10px;
            color: var(--white);
            text-align: center;
            font-size: 20px;
            margin: 10px 0;
        }

        /* Icon style */
        .icon {
            color: var(--keppel);
            font-size: 40px;
        }

        /* Other styling for buttons, headers */
        .stButton>button {
            background-color: var(--olive);
            color: var(--white);
            font-weight: bold;
            border-radius: 8px;
        }

        .stButton>button:hover {
            background-color: var(--keppel);
        }
    </style>
""", unsafe_allow_html=True)

# Set up the app title and description
st.markdown("<div class='app-container'><h1>Digital Mobile Health App</h1><p>Welcome to your personal health and wellness management app. Track your health metrics, set goals, and monitor your progress.</p></div>", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose a section", ["Home", "Log Health Metrics", "Log Menstrual Cycle", "Log Diet & Exercise", "View Dashboard", "Set Goals", "Health Records", "Terms of Service and Privacy Policy"])

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
if app_mode == "Home":
    st.markdown("<div class='app-container'><h2>Welcome to your Health Dashboard</h2><p>Use this app to log daily health metrics and track your progress over time.</p></div>", unsafe_allow_html=True)

# Log Health Metrics Page
elif app_mode == "Log Health Metrics":
    st.markdown("<div class='app-container'><h2>Log Daily Health Metrics</h2></div>", unsafe_allow_html=True)
    steps = st.number_input("Steps Walked Today", min_value=0, max_value=50000, step=100)
    sleep = st.number_input("Hours of Sleep", min_value=0.0, max_value=24.0, step=0.5)
    water_intake = st.number_input("Water Intake (oz)", min_value=0, max_value=300, step=1)
    
    if st.button("Save Entry"):
        data["Date"].append(date.today())
        data["Steps"].append(steps)
        data["Sleep (hrs)"].append(sleep)
        data["Water Intake (oz)"].append(water_intake)
        st.success("Health metrics logged successfully!")

# Example of a Metric Tile
st.markdown("<div class='metric-tile'><i class='icon'>📈</i><br>Steps Walked Today</div>", unsafe_allow_html=True)

import streamlit as st
import pandas as pd
from datetime import date

# Apply custom CSS for colors, gradients, and layout styling
st.markdown("""
    <style>
        /* Colors */
        :root {
            --white: #ffffffff;
            --madder: #a41623ff;
            --orange-pantone: #f85e00ff;
            --olive: #918450ff;
            --keppel: #60ab9aff;
        }

        /* Gradient Background */
        .app-container {
            background: linear-gradient(135deg, var(--madder), var(--orange-pantone), var(--olive), var(--keppel));
            padding: 20px;
            border-radius: 10px;
            color: var(--white);
        }

        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: var(--madder);
            color: var(--white);
        }

        /* Tile/Card styling */
        .metric-tile {
            background: var(--orange-pantone);
            padding: 20px;
            border-radius: 10px;
            color: var(--white);
            text-align: center;
            font-size: 20px;
            margin: 10px 0;
        }

        /* Icon style */
        .icon {
            color: var(--keppel);
            font-size: 40px;
        }

        /* Other styling for buttons, headers */
        .stButton>button {
            background-color: var(--olive);
            color: var(--white);
            font-weight: bold;
            border-radius: 8px;
        }

        .stButton>button:hover {
            background-color: var(--keppel);
        }
    </style>
""", unsafe_allow_html=True)

# Set up the app title and description
st.markdown("<div class='app-container'><h1>Digital Mobile Health App</h1><p>Welcome to your personal health and wellness management app. Track your health metrics, set goals, and monitor your progress.</p></div>", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose a section", ["Home", "Log Health Metrics", "Log Menstrual Cycle", "Log Diet & Exercise", "View Dashboard", "Set Goals", "Health Records", "Terms of Service and Privacy Policy"])

# Initialize a DataFrame to store logged metrics
data = {
    "Date": [],
    "Steps": [],
    "Sleep (hrs)": [],
    "Water Intake (oz

