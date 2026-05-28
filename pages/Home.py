import streamlit as st
import requests

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

# ================= LOGIN PROTECTION =================
if "user" not in st.session_state:
    st.switch_page("pages/Login.py")

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
h1,h2,h3,h4,h5,h6 {
    color: #0f172a !important;
    font-weight: 700;
}

/* Inputs */
.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background-color: #ffffff;
    color: #0f172a;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
}

/* Select Box */
.stSelectbox > div > div {
    background-color: #ffffff;
    color: #0f172a;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
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

section[data-testid="stSidebar"] {
    background-color: #f8fafc !important;
}

</style>
""", unsafe_allow_html=True)

# ================= PAGE =================
st.title("🚗 Car Price Prediction")

st.success(f"Welcome, {st.session_state['user']} 👋")

car_name = st.text_input("Car Name", value="swift")

year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2026,
    value=2014
)

present_price = st.number_input(
    "Present Price (Lakhs)",
    min_value=0.0,
    value=5.59
)

kms_driven = st.number_input(
    "Kms Driven",
    min_value=0,
    value=40000
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Dealer", "Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner_label = st.selectbox(
    "Owner",
    [
        "0 (First Owner)",
        "1 (Second Owner)",
        "3 (Third Owner)"
    ]
)

owner = int(owner_label.split()[0])

# ================= PREDICTION DATA =================
payload = {
    "Car_Name": car_name,
    "Year": year,
    "Present_Price": present_price,
    "Kms_Driven": kms_driven,
    "Fuel_Type": fuel_type,
    "Seller_Type": seller_type,
    "Transmission": transmission,
    "Owner": owner
}

# ================= PREDICT =================
if st.button("💰 Predict Price"):

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload,
            timeout=30
        )

        if response.status_code == 200:

            result = response.json()

            prediction = result.get("prediction_price")

            if prediction is not None:

                st.session_state["prediction"] = prediction
                st.session_state["payload"] = payload

                st.switch_page("pages/result.py")

            else:
                st.error("Prediction value not found in API response.")

        else:
            st.error(f"API Error ({response.status_code})")
            st.write(response.text)

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Cannot connect to FastAPI.\n\n"
            "Run:\n\n"
            "uvicorn main:app --reload --port 8000"
        )

    except Exception as e:
        st.error(f"Error: {e}")