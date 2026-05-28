import streamlit as st
import requests

st.set_page_config(page_title="Car Input", page_icon="🚗")
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

# Sidebar user info
if "user" in st.session_state:
    st.sidebar.success(f"👤 Logged in as: {st.session_state['user']}")
else:
    st.sidebar.warning("⚠️ Not logged in")

st.title("🚗 Enter Car Details")

car_name = st.text_input("Car_Name", value="swift")
year = st.number_input("Year", min_value=1990, max_value=2026, value=2014)
present_price = st.number_input("Present_Price (in lakhs)", min_value=0.0, value=5.59)
kms_driven = st.number_input("Kms_Driven", min_value=0, value=40000)
fuel_type = st.selectbox("Fuel_Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller_Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner_label = st.selectbox("Owner", ["0 (First Owner)", "1 (Second Owner)", "3 (Third Owner)"])
owner = int(owner_label.split()[0])

payload = {
    "Car_Name": car_name,
    "Year": year,
    "Present_Price": present_price,
    "Kms_Driven": kms_driven,
    "Fuel_Type": fuel_type,
    "Seller_Type": seller_type,
    "Transmission": transmission,
    "Owner": owner,
}

if st.button("Predict Price 💰"):

    st.write("Payload:", payload)

    try:
        res = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        st.write("Status Code:", res.status_code)
        st.write("Response:", res.text)

        if res.status_code == 200:

            data = res.json()
            pred = data.get("prediction_price", None)

            st.session_state["prediction"] = pred
            st.session_state["payload"] = payload

            st.switch_page("pages/result.py")

        else:
            st.error("Prediction failed")

    except Exception as e:
        st.error(f"Error: {e}")