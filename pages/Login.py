import streamlit as st
import json
import os

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Login",
    page_icon="🔑",
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

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #f8fafc 100%);
    color: #0f172a;
}

/* Header */
header[data-testid="stHeader"] {
    background: linear-gradient(135deg, #0f172a 0%, #f8fafc 100%);
}

/* Title */
h1 {
    text-align: center;
    font-weight: 700;
    color: #0f172a !important;
}

/* Labels */
label {
    color: #1f2937 !important;
    font-weight: 600;
}

/* Text Inputs */
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

p {
    color: #334155;
}

</style>
""", unsafe_allow_html=True)

# ================= UI =================
st.title("🔑 Login")
st.write("Please sign in to continue")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

# ================= LOGIN =================
if st.button("Sign In"):

    if not username.strip() or not password.strip():
        st.error("Please enter username and password")

    elif not os.path.exists("users.json"):
        st.error("No account found. Please create an account first.")

    else:
        try:
            with open("users.json", "r") as f:
                users = json.load(f)

            if username in users and users[username] == password:

                # Save logged in user
                st.session_state["user"] = username

                st.success("Login successful ✅")

                # Go to Home Page
                st.switch_page("pages/Home.py")

            else:
                st.error("Invalid username or password")

        except Exception:
            st.error("Unable to read user data.")

# ================= SIGNUP =================
st.write("---")
st.caption("Don't have an account?")

if st.button("📝 Create Account"):
    st.switch_page("pages/Signup.py")