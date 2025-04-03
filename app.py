import streamlit as st

# Title
st.title("Metabolic Health & Motivation Assistant")

# Section 1: Personal Info
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

# Section 2: Metabolic Calculations
st.header("2. Metabolic Estimates")
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

st.write(f"**BMR:** {bmr:.2f} kcal/day")
st.write(f"**TDEE:** {tdee:.2f} kcal/day")

# Section 3: Breakfast with health tips and motivation
st.header("3. Breakfast Recipes with Health Benefits")

with st.expander("🌿 High-Protein Greek Yogurt Bowl (350 kcal)"):
    st.markdown("""
    **Ingredients:**
    - 3/4 cup plain Greek yogurt (non-fat)
    - 1/4 cup granola
    - 1/2 banana, sliced
    - 1 tbsp chia seeds
    - Handful of berries

    **Macros:** ~25g protein, 35g carbs, 10g fat

    **Health Benefits:**
    - Greek yogurt is rich in probiotics, great for gut health.
    - Chia seeds and berries provide fiber to keep you full longer.
    - Bananas offer quick-release energy with potassium.

    **Motivation:** Start your morning with protein and color—fuel your success!
    """)

with st.expander("🍎 Oatmeal with Peanut Butter & Cinnamon (380 kcal)"):
    st.markdown("""
    **Ingredients:**
    - 1/2 cup oats
    - 1 tbsp peanut butter
    - 1/2 cup almond milk
    - Dash of cinnamon
    - Optional: sliced apple or banana

    **Macros:** ~10g protein, 45g carbs, 15g fat

    **Health Benefits:**
    - Oats are complex carbs that stabilize blood sugar.
    - Peanut butter adds healthy fats and protein.
    - Cinnamon may support blood sugar control.

    **Motivation:** You’re building habits, not restrictions. Every meal matters.
    """)

# Section 4: Exercise Routine
st.header("4. 15-Min Belly Fat Burn Routine (No Equipment)")

st.markdown("""
**Do this circuit 3 times:**  
1. 🏃‍♂️ Jumping Jacks — 30 seconds  
2. 🧘‍♀️ Mountain Climbers — 30 seconds  
3. 🔥 Russian Twists — 20 reps  
4. 💪 Plank — 30 seconds  
5. ⬆️ Leg Raises — 15 reps  

**Rest:** 60 seconds between rounds  
**Goal:** Burn fat and strengthen your core.

**Motivation:** Consistency beats intensity. Keep showing up—you’ve got this!
""")

# Section 5: Health Tips
st.header("5. Daily Health & Motivation Tip 💡")

st.info("Drink a glass of water before each meal. Hydration supports digestion and curbs cravings.")

st.success("You’re not alone. Progress takes time, but every step forward counts.")

# Footer
st.markdown("---")
st.caption("Next version: add lunch/dinner meals, daily tracker, and exportable summary.")
