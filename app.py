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

# Section 2: Behavior & Lifestyle Diagnostic
st.header("2. Behavior & Lifestyle Diagnostic")

st.subheader("Eating Habits")
meals_per_day = st.slider("How many meals do you eat per day?", 1, 6, 3)
snacks_per_day = st.slider("How many snacks do you eat per day?", 0, 5, 2)
night_eating = st.selectbox("Do you eat late at night (after 9 PM)?", ["Never", "Sometimes", "Often", "Always"])
sugar_intake = st.selectbox("How often do you consume sugary foods/drinks?", ["Rarely", "1–2x/week", "Daily", "Multiple times/day"])
emotional_eating = st.selectbox("Do you eat when you're stressed or emotional?", ["Never", "Occasionally", "Often", "Always"])

st.subheader("Sleep Hygiene")
sleep_duration = st.slider("Average sleep duration (hours)", 3, 12, 7)
sleep_quality = st.selectbox("How would you rate your sleep quality?", ["Poor", "Fair", "Good", "Excellent"])
sleep_consistency = st.selectbox("Do you go to bed/wake up at consistent times?", ["Rarely", "Sometimes", "Usually", "Always"])

st.subheader("Stress & Mental Health")
stress_level = st.slider("Stress level (1 = very low, 10 = very high)", 1, 10, 5)
stress_source = st.multiselect("What are your biggest sources of stress?", ["Work", "Health", "Relationships", "Finances", "Time management", "Other"])
stress_coping = st.selectbox("How do you typically cope with stress?", ["Exercise", "Food", "Sleep", "Talking to someone", "Not sure", "Other"])

st.subheader("Hydration & Energy")
water_cups = st.slider("Cups of water per day", 0, 20, 8)
caffeine_use = st.selectbox("Do you use caffeine (coffee/energy drinks)?", ["No", "1x/day", "2x/day", "3+ times/day"])
daytime_fatigue = st.selectbox("How often do you feel tired during the day?", ["Never", "Sometimes", "Often", "Always"])

st.subheader("Physical Activity")
sitting_hours = st.slider("How many hours a day are you sitting?", 0, 16, 8)
preferred_workouts = st.multiselect("What kinds of exercise do you enjoy?", ["Walking", "Jogging", "Weightlifting", "Yoga", "HIIT", "Dancing", "Other"])
steps_per_day = st.slider("Estimated steps per day", 0, 20000, 5000)
workout_consistency = st.selectbox("How consistent is your workout habit?", ["Not consistent", "1–2x/week", "3–4x/week", "5+ days/week"])

st.subheader("Behavior Change Readiness")
change_stage = st.selectbox("How ready are you to change your habits?", ["Not ready", "Thinking about it", "Taking small steps", "Actively changing"])
recent_changes = st.text_area("What health changes have you made in the past month?")
support_system = st.selectbox("Do you have a support system for your health journey?", ["Yes", "No", "Somewhat"])

# Section 3: Metabolic Estimates
st.header("3. Metabolic Estimates")

if sex == "Male":
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
else:
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

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

# Section 4: Meal Plan - Breakfast Ideas
st.header("4. Sample Meal Plan: Breakfast Ideas")

with st.expander("High-Protein Greek Yogurt Bowl (350 kcal)"):
    st.markdown("""
    **Ingredients:**
    - 3/4 cup plain Greek yogurt (non-fat)
    - 1/4 cup granola
    - 1/2 banana, sliced
    - 1 tbsp chia seeds
    - Handful of berries

    **Macros:** ~25g protein, 35g carbs, 10g fat

    **Instructions:**
    1. Layer yogurt in a bowl.
    2. Add banana, granola, and berries.
    3. Sprinkle chia seeds on top.
    4. Enjoy chilled.
    """)

with st.expander("Oatmeal with Peanut Butter & Cinnamon (380 kcal)"):
    st.markdown("""
    **Ingredients:**
    - 1/2 cup oats
    - 1 tbsp peanut butter
    - 1/2 cup almond milk
    - Dash of cinnamon
    - Optional: sliced apple or banana

    **Macros:** ~10g protein, 45g carbs, 15g fat

    **Instructions:**
    1. Cook oats in almond milk.
    2. Stir in peanut butter and cinnamon.
    3. Top with fruit.
    """)

st.markdown("---")
st.caption("This prototype will soon include lunch, dinner, and exercise plans.")
