import streamlit as st
from utils.data_loader import load_data

# Set page configuration
st.set_page_config(
    page_title="🧠 Text Classifier by Kevin Philips Tanamas",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables
if 'trained_model' not in st.session_state:
    st.session_state.trained_model = None
if 'vectorizer' not in st.session_state:
    st.session_state.vectorizer = None
if 'model_name' not in st.session_state:
    st.session_state.model_name = None
if 'label_column' not in st.session_state:
    st.session_state.label_column = None

# Load data
if 'df' not in st.session_state:
    st.session_state.df = load_data()

# ---------- HEADER ----------
st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>📚 Modul 2 - Single-label Text Classification</h1>
    <h4 style='text-align: center; color: gray;'>by <i>Kevin Philips Tanamas</i></h4>
""", unsafe_allow_html=True)

st.markdown("""---""")

# ---------- INTRODUCTION ----------
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("🚀 Welcome!")
        st.markdown("""
        This interactive application demonstrates single-label text classification using popular machine learning models such as:
        - ✅ Support Vector Machine (SVM)
        - 🌲 Random Forest
        - 📈 Multinomial Naive Bayes

        **Explore, Train, and Predict** using the navigation sidebar on the left!
        """)
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3437/3437364.png", width=200)

# ---------- DATASET OVERVIEW ----------
st.markdown("""---""")
st.subheader("🔍 Dataset Overview")

df = st.session_state.df
col1, col2 = st.columns(2)
col1.metric("Total Samples", df.shape[0])
col2.metric("Total Features", df.shape[1])

st.dataframe(df.head(5), use_container_width=True)

# ---------- FOOTER ----------
st.markdown("""---""")
st.markdown(
    "<p style='text-align: center; color: gray;'>© 2025 Kevin Philips Tanamas | All Rights Reserved</p>",
    unsafe_allow_html=True
)
