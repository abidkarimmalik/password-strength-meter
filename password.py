import re
import streamlit as st

def check_password(password):
    strength = 0

    # Checking length
    if len(password) >= 8:
        strength += 1
    if len(password) >= 12:
        strength += 1

    # Checking for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1

    # Checking for numbers
    if re.search(r'[0-9]', password):
        strength += 1

    # Checking for special characters
    if re.search(r'[!@#$%^&*()_+]', password):
        strength += 1

    # Password strength classification
    if strength <= 2:
        return "Weak ❌", "red"
    elif strength == 3:
        return "Medium ⚠️", "orange"
    elif strength == 4:
        return "Strong ✅", "blue"
    else:
        return "Very Strong 💪", "green"

# Streamlit UI
st.title("🔒 Password Strength Checker")

password = st.text_input("Enter a password:", type="password")

if password:
    strength, color = check_password(password)
    st.markdown(f"<h3 style='color:{color};'>Password Strength: {strength}</h3>", unsafe_allow_html=True)

    st.write("Created by Abid Karim Malik")

    st.write("Thank you for using my password strength checker!")
