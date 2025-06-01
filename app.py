import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

# Set page config
st.set_page_config(page_title="Internship Success Predictor", layout="centered")

st.title("🎓 Internship Success Predictor")
st.markdown("Enter the student's profile to predict their internship success likelihood using a machine learning model.")

# Load model and scaler
@st.cache_resource
def load_model_and_scaler():
    if os.path.exists("success_model.pkl") and os.path.exists("scaler.pkl"):
        model = pickle.load(open("success_model.pkl", "rb"))
        scaler = pickle.load(open("scaler.pkl", "rb"))
        return model, scaler
    return None, None

model, scaler = load_model_and_scaler()

if not model or not scaler:
    st.warning("⚠️ Model and scaler files not found. Please train the model first by running `student_success_model.py`.")
else:
    with st.form("predict_form"):
        st.subheader("🔧 Enter Student Profile")

        col1, col2 = st.columns(2)
        with col1:
            cgpa = st.number_input("📚 CGPA", min_value=0.0, max_value=10.0, step=0.1, format="%.2f", value=8.0)
            attendance = st.slider("📅 Attendance (%)", 0, 100, 85)
            projects = st.number_input("💻 Projects Done", min_value=0, step=1, value=2)
        with col2:
            skills = st.number_input("🧠 Skills Count", min_value=0, step=1, value=4)
            certifications = st.number_input("📜 Certifications", min_value=0, step=1, value=1)

        submitted = st.form_submit_button("🔍 Predict")

    if submitted:
        # Use a DataFrame with correct column names to avoid warnings
        feature_names = ['CGPA', 'Attendance', 'Projects_Done', 'Skills_Count', 'Certifications']
        input_df = pd.DataFrame([[cgpa, attendance, projects, skills, certifications]], columns=feature_names)

        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)[0]
        prob = model.predict_proba(input_scaled)[0][prediction]

        if prediction == 1:
            st.success(f"✅ This student is likely to succeed in the internship! (Confidence: {prob:.2%})")
        else:
            st.error(f"⚠️ This student might need improvement to succeed in the internship. (Confidence: {prob:.2%})")

# Footer
st.markdown("---")
st.markdown("*Made for Micro IT Company 🚀")

