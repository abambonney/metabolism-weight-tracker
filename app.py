import streamlit as st

# Title
st.title("Metabolic Health & Weight Assistant")

# Section 1: Personal Information
st.header("1. Personal Profile")
name = st.text_input("Name")
age = st.number_input("Age", min_value=10, max_value=100)
sex = st.selectbox("Sex assigned at birth", ["Male", "Female"])
height_cm = st.number_input("Height (cm)")
weight_kg = st.number_input("Current Weight (kg)")
goal_weight_kg = st.number_input("Goal Weight (kg)")

activity_level = st.selectbox("Activity Level", [
    "Sedentary (little or no exercise)",
    "Lightly active (light exercise 1–3 days/week)",
    "Moderately active (moderate exercise 3–5 days/week)",
    "Very active (hard exercise 6–7 days/week)",
    "Super active (athlete-level or physical job)"
])

# Section 2: Lifestyle and Behavior
st.header("2. Behavior & Lifestyle")
behavior_changes = st.text_area("Describe any recent behavior changes you've made")
sleep_hours = st.slider("Average sleep per night (hours)", 0, 12, 7)
hydration = st.slider("How many cups of water per day?", 0, 20, 8)
stress = st.slider("Stress level (1 = low, 10 = high)", 1, 10, 5)
metabolism_status = st.selectbox("How would you describe your metabolism?", ["Slow", "Average", "Fast"])

# Section 3: Metabolic Calculations
st.header("3. Metabolic Estimates")

# BMR calculation (Mifflin-St Jeor Equation)
if sex == "Male":
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
else:
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

# TDEE multiplier
activity_multipliers = {
    "Sedentary (little or no exercise)": 1.2,
    "Lightly active (light exercise 1–3 days/week)": 1.375,
    "Moderately active (moderate exercise 3–5 days/week)": 1.55,
    "Very active (hard exercise 6–7 days/week)": 1.725,
    "Super active (athlete-level or physical job)": 1.9
}
tdee = bmr * activity_multipliers[activity_level]

st.subheader("Your Metabolic Summary")
st.write(f"**Basal Metabolic Rate (BMR):** {bmr:.2f} kcal/day")
st.write(f"**Total Daily Energy Expenditure (TDEE):** {tdee:.2f} kcal/day")

if goal_weight_kg > 0:
    st.info("Next step: Caloric deficit planning, recipes, and personalized workouts coming soon.")

# Footer
st.markdown("---")
st.caption("This is an early prototype. Content will be expanded with clinical references, meal plans, and exercise routines.")
