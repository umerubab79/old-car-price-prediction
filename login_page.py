import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔑")

# --- Background color CSS ---
st.markdown(
    """
    <style>

    /* ================= GLOBAL BACKGROUND ================= */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #f8fafc 100%);
        color: #0f172a;
    }

    /* ================= HEADINGS ================= */
    h1, h2, h3, h4, h5, h6 {
        color: #0f172a !important;
        font-weight: 700;
    }

    /* ================= INPUT FIELDS ================= */
    .stTextInput>div>div>input,
    .stNumberInput>div>div>input {
        background-color: #ffffff;
        color: #0f172a;
        border: 1px solid #cbd5e1;
        border-radius: 10px;
        padding: 8px;
    }

    /* ================= SELECTBOX ================= */
    .stSelectbox>div>div {
        background-color: #ffffff;
        color: #0f172a;
        border-radius: 10px;
        border: 1px solid #cbd5e1;
    }

    /* ================= BUTTON ================= */
    .stButton>button {
        background-color: #2563eb;
        color: white !important;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white !important;
    }
/* ================= SIDEBAR LIGHT ================= */
section[data-testid="stSidebar"] {
    background-color: #f8fafc !important;
    color: #0f172a;
    border-right: 1px solid #e2e8f0;
}

/* ================= SIDEBAR NAV ================= */
section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] {
    background-color: #f8fafc !important;
}

/* ================= PAGE LINKS ================= */
section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] a {
    color: #0f172a !important;
    font-weight: 500;
    padding: 8px 10px;
    border-radius: 8px;
}

/* Hover effect */
section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] a:hover {
    background-color: #e2e8f0 !important;
    color: #0f172a !important;
}

/* Active page */
section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] a[aria-current="page"] {
    background-color: #2563eb !important;
    color: #ffffff !important;
    border-radius: 8px;
}

    /* ================= LABELS ================= */
    label {
        color: #1f2937 !important;
        font-weight: 500;
    }

    /* ================= SUCCESS / ERROR BOX ================= */
    .stSuccess {
        background-color: #dcfce7;
        color: #166534;
    }

    .stError {
        background-color: #fee2e2;
        color: #991b1b;
    }

    /* ================= HEADER BAR (optional fix) ================= */
    header[data-testid="stHeader"] {
       background: linear-gradient(135deg, #0f172a 0%, #f8fafc 100%);
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔑 Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Sign In"):
    if username and password:  # simple check, you can replace with DB validation
        st.session_state["user"] = username
        st.success("Login successful ✅")
        st.switch_page("pages/Home.py")
        
    else:
        st.error("Please enter both username and password")

st.write("---")
st.caption("Don't have an account?")
if st.button("Sign Up"):
    st.info("Sign Up functionality can be added here (DB or file storage).")
