import streamlit as st

# ================= LOGIN PROTECTION =================
if "user" not in st.session_state:
    st.switch_page("pages/Login.py")

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Prediction Result",
    page_icon="📊",
    layout="centered"
)

# ================= SIDEBAR =================
st.sidebar.success(
    f"👤 Logged in as: {st.session_state['user']}"
)

st.sidebar.write("---")

if st.sidebar.button("🚪 Logout"):

    st.session_state.pop("user", None)
    st.session_state.pop("prediction", None)
    st.session_state.pop("payload", None)

    st.switch_page("pages/Login.py")

# ================= CSS =================
st.markdown("""
<style>

/* Main Background */
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

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #f8fafc !important;
    border-right: 1px solid #e2e8f0;
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

/* Alert Boxes */
[data-testid="stAlert"] {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ================= PAGE TITLE =================
st.title("📊 Prediction Result")

# ================= RESULT =================
if "prediction" in st.session_state:

    prediction = st.session_state["prediction"]

    st.success(
        f"✅ Predicted Selling Price: ₹ {prediction:.2f} Lakhs"
    )

    st.write("")

    st.subheader("🚗 Car Details")

    payload = st.session_state.get("payload", {})

    if payload:
        st.json(payload)

else:
    st.warning(
        "⚠️ No prediction found. Please run prediction first."
    )

# ================= BUTTONS =================
st.write("")
st.write("---")

col1, col2 = st.columns(2)

with col1:

    if st.button("⬅ Back To Home"):
        st.switch_page("pages/Home.py")

with col2:

    if st.button("🔄 New Prediction"):

        st.session_state.pop("prediction", None)
        st.session_state.pop("payload", None)

        st.switch_page("pages/Home.py")