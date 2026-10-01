import streamlit as st

st.title("Student Grade System")

mark = st.number_input(
    "Enter your mark (0–100):",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=1.0
)

if mark >= 90:
    grade = "A"
elif mark >= 80:
    grade = "B"
elif mark >= 70:
    grade = "C"
elif mark >= 60:
    grade = "D"
else:
    grade = "F"

st.success(f"Mark:  {mark:g} -> Grade:  {grade}.")
