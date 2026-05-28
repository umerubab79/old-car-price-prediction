import streamlit as st
import os

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗"
)

# ================= SMART ROUTING =================

# User already logged in
if "user" in st.session_state:
    st.switch_page("pages/Home.py")

# Check if any account exists
if not os.path.exists("users.json"):
    st.switch_page("pages/Signup.py")

else:
    try:
        import json

        with open("users.json", "r") as f:
            users = json.load(f)

        # No users found
        if len(users) == 0:
            st.switch_page("pages/Signup.py")

        # Existing users found
        else:
            st.switch_page("pages/Login.py")

    except Exception:
        st.switch_page("pages/Signup.py")