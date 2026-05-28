import streamlit as st
import json
import os

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Sign Up",
    page_icon="📝",
    layout="centered"
)

# ================= AUTO REDIRECT =================
if "user" in st.session_state:
    st.switch_page("pages/Home.py")

# ================= CSS =================
st.markdown("""
<style>

/* Hide Sidebar */
[data-testid="stSidebar"] {
    display: none;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #f8fafc 100%);
    color: #0f172a;
}

/* Header */
header[data-testid="stHeader"] {
    background: linear-gradient(135deg, #0f172a 0%, #f8fafc 100%);
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #0f172a !important;
    font-weight: 700;
}

/* Labels */
label {
    color: #1f2937 !important;
    font-weight: 600;
}

/* Inputs */
.stTextInput > div > div > input {
    background-color: white;
    color: #0f172a;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    padding: 10px;
}

/* Buttons */
.stButton > button {
    width: 100%;
    background-color: #2563eb;
    color: white !important;
    border-radius: 10px;
    border: none;
    padding: 0.7rem;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #1d4ed8;
}

/* Caption */
p {
    color: #334155;
}

</style>
""", unsafe_allow_html=True)

# ================= UI =================
st.title("📝 Create Account")
st.write("Create your account to continue")

new_user = st.text_input("Username")
new_pass = st.text_input("Password", type="password")
confirm_pass = st.text_input("Confirm Password", type="password")

# ================= CREATE ACCOUNT =================
if st.button("Create Account"):

    if not new_user.strip() or not new_pass.strip() or not confirm_pass.strip():
        st.error("Please fill all fields")

    elif new_pass != confirm_pass:
        st.error("Passwords do not match")

    else:

        users = {}

        # Load existing users
        if os.path.exists("users.json"):
            try:
                with open("users.json", "r") as f:
                    users = json.load(f)
            except:
                users = {}

        # Check duplicate username
        if new_user in users:
            st.error("Username already exists")

        else:
            users[new_user] = new_pass

            # Save user
            with open("users.json", "w") as f:
                json.dump(users, f, indent=4)

            st.success("Account created successfully ✅")

            # Redirect to Login page
            st.switch_page("pages/Login.py")

# ================= LOGIN BUTTON =================
st.write("---")
st.caption("Already have an account?")

if st.button("🔑 Login"):
    st.switch_page("pages/Login.py")