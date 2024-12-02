# Import necessary libraries
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
st.title("🌱 BiYourFusion Mobile Health App")
st.write("Welcome to your personal health and wellness management app. Track your daily health insights, set goals, monitor your progress, and store your health records.")

# Function to display the introduction
def show_intro():
    st.title("WhyBiyourFusion 🌟")
    st.markdown("""
        **BiyourFusion** is an all-in-one health and wellness app designed for maximum convenience and efficiency. 
        Unlike competitors like **MyFitnessPal**, **OurApp**, and **Apple Health**, BiyouFusion consolidates multiple essential features 
        into one platform, helping you track your health goals, fitness, menstrual cycles, and medical records effortlessly.

        ### Key Features:
        - **Health Goals**: Track weight, calorie intake, and nutrition.
        - **Menstrual Cycle**: Log phases, ovulation, contraceptives, and receive tailored tips.
        - **Fitness & Exercise**: Log workouts, monitor activity trends, access workout videos, and create personalized plans.
        - **Health Records**: Upload, update, and share health and immunization records with healthcare providers anytime.

        BiyourFusion makes it easier to manage your health and fitness in one place, offering **convenience, efficiency**, and **easy access** to important health information.
    """)


# Sidebar for navigation with icons
st.sidebar.title("🌐 Navigation")
app_mode = st.sidebar.selectbox("Choose a section", [
    "Home", " WhyBiyourFusion", "Log Health Metrics", "Log Menstrual Cycle", 
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
        st.success("Health metrics logged successfully!")

# Log Menstrual Cycle Page with enhanced features and tips
elif app_mode == "Log Menstrual Cycle":
    st.subheader("Log Menstrual Cycle 🌸")

    # Cycle tracking inputs
    st.write("### Menstrual Cycle Details")
    cycle_start = st.date_input("Start Date")
    cycle_end = st.date_input("End Date", min_value=cycle_start)
    cycle_length = (cycle_end - cycle_start).days
    st.write(f"Cycle Length: {cycle_length} days")

    # Ovulation tracking
    st.write("### Ovulation Tracking")
    ovulation_date = st.date_input("Ovulation Date (estimated)", min_value=cycle_start, max_value=cycle_end)
    st.write(f"Estimated Ovulation Date: {ovulation_date}")

    # Contraceptive use tracking
    st.write("### Contraceptive Use")
    contraceptive_type = st.selectbox("Select Contraceptive Method", [
        "None", "Birth Control Pill", "IUD", "Condom", "Natural Rhythm Method", "Other"
    ])
    contraceptive_notes = st.text_area("Additional Notes on Contraceptive Use (if any)")

    # Conception and sexual activity tracking
    st.write("### Conception and Sexual Activity")
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
    ])

    if phase == "Menstrual Phase":
        st.write("""
        **Tips during your period:**
        - **Foods to Indulge In:** Iron-rich foods (spinach, lentils), magnesium-rich foods (dark chocolate, nuts).
        - **Foods to Avoid:** Processed foods, caffeine, and alcohol.
        - **Exercises to Try:** Light yoga, walking, or stretching.
        - **Exercises to Avoid:** High-intensity workouts if energy levels are low.
        - **Other Tips:** Use heating pads for cramps and prioritize hydration.
        """)

    elif phase == "Follicular Phase":
        st.write("""
        **Tips during the follicular phase:**
        - **Foods to Indulge In:** Protein-rich foods (eggs, chicken, fish), healthy fats (avocado, nuts).
        - **Foods to Avoid:** High-sugar snacks and refined carbs.
        - **Exercises to Try:** Cardio, weight training, or high-energy activities.
        - **Other Tips:** This is the best time to focus on productivity and creative projects.
        """)

    elif phase == "Ovulation Phase":
        st.write("""
        **Tips during ovulation:**
        - **Foods to Indulge In:** Antioxidant-rich foods (berries, leafy greens), hydration-focused foods (watermelon, cucumber).
        - **Foods to Avoid:** Inflammatory foods (fried or overly salty foods).
        - **Exercises to Try:** High-intensity interval training (HIIT), running, or dancing.
        - **Other Tips:** Socialize and take advantage of peak energy and confidence.
        """)

    elif phase == "Luteal Phase":
        st.write("""
        **Tips during the luteal phase:**
        - **Foods to Indulge In:** Complex carbs (sweet potatoes, quinoa), omega-3-rich foods (salmon, flaxseed).
        - **Foods to Avoid:** Excess sodium and caffeine to reduce bloating.
        - **Exercises to Try:** Pilates, moderate-intensity workouts, or swimming.
        - **Other Tips:** Manage mood changes by practicing mindfulness or journaling.
        """)

# Fitness & Exercise Page
elif app_mode == "Fitness & Exercise":
    st.subheader("Fitness & Exercise 🏋️‍♂️")

    # Section 1: Log Exercises
    st.write("### Log Your Exercises")
    exercise_type = st.text_input("Type of Exercise (e.g., running, yoga, weightlifting)")
    duration = st.number_input("Duration (minutes)", min_value=0, step=1)
    calories_burned = st.number_input("Estimated Calories Burned", min_value=0, step=1)

    if st.button("Save Exercise"):
        st.success("Exercise logged successfully!")
        st.write(f"**Exercise Type:** {exercise_type}")
        st.write(f"**Duration:** {duration} minutes")
        st.write(f"**Calories Burned:** {calories_burned}")

    # Section 2: Explore Trainer Tips
    st.write("### Trainer Tips & Free Resources")
    st.write("Access free workout videos and meditations:")
    st.video("https://www.youtube.com/watch?v=example_workout_video")  # Replace with real URLs
    st.video("https://www.youtube.com/watch?v=example_meditation_video")  # Replace with real URLs

    # Section 3: Activity Trends
    st.write("### Track Your Activity Trends")
    steps = st.slider("Steps Taken Today", 0, 20000, step=100)
    standing_time = st.slider("Standing Time (hours)", 0, 24, step=1)
    distance = st.slider("Distance Traveled (miles)", 0.0, 10.0, step=0.1)

    # Display trends
    st.write("### Activity Overview")
    st.bar_chart({"Steps": steps, "Standing Hours": standing_time, "Distance (miles)": distance})

    # Section 4: Custom Plans & Rewards
    st.write("### Personalized Activity Plans")
    custom_plan_name = st.text_input("Name Your Plan")
    weekly_goal = st.slider("Weekly Goal (hours)", 0, 20, step=1)
    st.write("Earn badges for achieving milestones and stay motivated!")

    if st.button("Create Plan"):
        st.success(f"Your plan '{custom_plan_name}' has been created!")
        st.write(f"**Weekly Goal:** {weekly_goal} hours")
        st.write("Keep pushing towards your goal and collect rewards!")

    # Section 5: Social Sharing
    st.write("### Share Your Progress")
    share_option = st.selectbox("Who would you like to share with?", ["Trainers", "Friends", "Both", "None"])
    if share_option != "None":
        st.write(f"Your progress will be shared with: {share_option}")
    st.button("Share Now", key="share_progress")


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

# Set Goals Page with additional features
if app_mode == "Set Goals":
    st.subheader("Set Health Goals 🎯")

    # Input for weight goals
    st.write("### Weight Goals")
    current_weight = st.number_input("Current Weight (lbs)", min_value=50, max_value=500, step=1)
    ideal_weight = st.number_input("Ideal Weight (lbs)", min_value=50, max_value=500, step=1)
    height = st.number_input("Height (inches)", min_value=36, max_value=96, step=1)

    weight_goal = st.selectbox("Do you want to gain or lose weight?", ["Maintain", "Lose", "Gain"])
    
    # Input for food tracking
    st.write("### Food Intake Goals")
    calorie_goal = st.number_input("Daily Calorie Goal (kcal)", min_value=500, max_value=5000, step=50)

    st.write("Track your macronutrients:")
    carb_goal = st.number_input("Carbohydrates (grams/day)", min_value=0, max_value=500, step=1)
    protein_goal = st.number_input("Protein (grams/day)", min_value=0, max_value=300, step=1)
    fat_goal = st.number_input("Fat (grams/day)", min_value=0, max_value=200, step=1)
    sugar_goal = st.number_input("Sugar (grams/day)", min_value=0, max_value=200, step=1)

    # Input for food and brands
    st.write("### Track Your Meals")
    meal = st.text_input("Enter Food Item", placeholder="e.g., Chicken Breast, Banana")
    calories = st.number_input("Calories (kcal)", min_value=0, max_value=2000, step=1)
    carbs = st.number_input("Carbohydrates (g)", min_value=0, max_value=500, step=1)
    protein = st.number_input("Protein (g)", min_value=0, max_value=200, step=1)
    fat = st.number_input("Fat (g)", min_value=0, max_value=100, step=1)
    sugar = st.number_input("Sugar (g)", min_value=0, max_value=100, step=1)

    if st.button("Add Meal"):
        st.success(f"Added {meal} with {calories} kcal, {carbs}g carbs, {protein}g protein, {fat}g fat, and {sugar}g sugar.")

    # Save Goals
    if st.button("Save Goals"):
        st.success("Your health goals have been saved successfully!")
        st.write(f"### Summary of Goals:")
        st.write(f"- Weight Goal: {weight_goal} (Current: {current_weight} lbs, Ideal: {ideal_weight} lbs)")
        st.write(f"- Height: {height} inches")
        st.write(f"- Daily Calorie Goal: {calorie_goal} kcal")
        st.write(f"- Macronutrient Goals: {carb_goal}g carbs, {protein_goal}g protein, {fat_goal}g fat, {sugar_goal}g sugar")


# Health Records Page
elif app_mode == "Health Records":
    st.subheader("Log Health Records 📋")
    conditions = st.text_area("Existing Health Conditions")
    allergies = st.text_area("Known Allergies")
    if st.button("Save Health Records"):
        st.success("Health records saved successfully!")

# Immunization Records Page
elif app_mode == "Immunization Records":
    st.subheader("Store and View Immunization Records 💉")
    st.write("Keep a record of your immunizations for easy reference. You can log new immunizations and view your existing records.")

    # Input fields for logging immunizations
    st.write("### Add a New Immunization Record")
    vaccine_name = st.text_input("Vaccine Name", placeholder="e.g., Influenza, COVID-19")
    date_received = st.date_input("Date Received")
    provider_name = st.text_input("Healthcare Provider", placeholder="e.g., Clinic or Doctor's Name")
    additional_notes = st.text_area("Additional Notes (Optional)", placeholder="e.g., Any side effects or remarks")

    if st.button("Save Immunization Record"):
        st.success(f"Immunization record for {vaccine_name} saved successfully!")

    # Example of displaying stored records (you would replace this with actual data retrieval logic)
    st.write("### Your Immunization Records")
    sample_records = pd.DataFrame({
        "Vaccine Name": ["Influenza", "COVID-19 Booster"],
        "Date Received": ["2023-10-10", "2024-01-15"],
        "Healthcare Provider": ["City Health Clinic", "County Hospital"],
        "Notes": ["No side effects", "Mild fever after injection"]
    })
    st.table(sample_records)

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
