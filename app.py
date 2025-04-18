import streamlit as st
from bot import generate_meal_plan

def app():
    st.success(f"Welcome, {st.session_state.username}!")
    st.title("🥗 Diet Recommendation")

    st.markdown(
        """
        <style>
        .stForm {
            background-color: #f0f0f5;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stForm input {
            background-color: #e8e8f1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.form(key='bmr_form', clear_on_submit=True):
        st.subheader("🧮 Enter your details")

        gender = st.radio("Select Gender", ["Male", "Female"], horizontal=True)
        age = st.number_input("Enter Age (in years)", min_value=1, max_value=120, value=30)
        weight = st.number_input("Enter Weight (in kg)", min_value=1, value=70)
        height = st.number_input("Enter Height (in cm)", min_value=1, value=170)

        st.markdown("**Select Activity Level**")
        
        activity_level = st.radio(
            "Activity Level",
            [
                "Sedentary: little or no exercise",
                "Exercise 1-3 times/week",
                "Exercise 4-5 times/week",
                "Daily exercise or intense exercise 3-4 times/week",
                "Intense exercise 6-7 times/week",
                "Very intense exercise daily, or physical job"
            ]
        )
        selected_meals = st.multiselect(
            "Choose meals to include in your plan:",
            ["Breakfast", "Brunch", "Lunch", "Dinner"],
            default=["Breakfast", "Lunch", "Dinner"]
        )

        submit_button = st.form_submit_button(label="✅ Submit")

        if submit_button:
            if gender == "Male":
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161

            activity_multipliers = {
                "Sedentary: little or no exercise": 1.2,
                "Exercise 1-3 times/week": 1.375,
                "Exercise 4-5 times/week": 1.55,
                "Daily exercise or intense exercise 3-4 times/week": 1.725,
                "Intense exercise 6-7 times/week": 1.9,
                "Very intense exercise daily, or physical job": 2.0,
            }
            tdee = bmr * activity_multipliers[activity_level]
            st.write(f"**Your BMR is:** `{bmr:.2f}` kcal/day")
            st.write(f"**Your estimated TDEE is:** `{tdee:.2f}` kcal/day based on your activity level.")

            with st.spinner("Generating your personalized meal plan…"):
                plan = generate_meal_plan(gender, age, weight, height, activity_level, tdee, selected_meals)
            with st.container():
                st.markdown("### 🍽️ Your AI‑Generated Meal Plan")
                st.markdown(plan)

def login():
    st.set_page_config(page_title="Diet App Login", page_icon="🍏", layout="centered")

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""

    if st.session_state.logged_in:
        app()
        st.divider()
        col1, col2, _ = st.columns([1, 1, 3])
        with col1:
            if st.button("🔒 Log Out"):
                st.session_state.logged_in = False
                st.session_state.username = ""
                st.rerun()
    else:
        st.title("🍏 Diet App Login")
        st.caption("Please enter your credentials to continue.")

        with st.container():
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            col1, col2, _ = st.columns([1, 1, 3])
            with col1:
                login_clicked = st.button("Login")

            if login_clicked:
                if username == "Swayam" and password == "password":
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Login successful! Redirecting...")
                    st.rerun()
                else:
                    st.error("Invalid credentials, please try again.")

login()
