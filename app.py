import streamlit as st
import pandas as pd
import joblib

# Load the trained model
data = joblib.load("student_rating_model.joblib")
model = data["model"]

# App title
st.title("Student Rating Prediction System")

st.write("Enter the student's LMS activities to predict their rating.")

# Student LMS input form
with st.form("student_form"):

    submission = st.text_input("Submission Actions", "0")
    quiz = st.text_input("Quiz Actions", "0")
    forum = st.text_input("Forum Actions", "0")
    create = st.text_input("Create Actions", "0")
    read = st.text_input("Read Actions", "0")
    update = st.text_input("Update Actions", "0")
    delete = st.text_input("Delete Actions", "0")
    days = st.text_input("Days Logged In", "0")

    # Submit button
    predict = st.form_submit_button("Predict Rating")

# Prediction
if predict:

    try:
        # Convert inputs into integers
        values = [
            int(submission),
            int(quiz),
            int(forum),
            int(create),
            int(read),
            int(update),
            int(delete),
            int(days)
        ]

        # Check for negative values
        if any(value < 0 for value in values):
            st.error("Please enter non-negative numbers only.")

        else:
            # Prepare input data
            columns = data["features"]
            student_data = pd.DataFrame([values], columns=columns)

            # Predict student rating
            prediction = model.predict(student_data)[0]

            # Display result
            st.subheader("Prediction Result")

            if prediction == "High":
                st.success("Student Rating: HIGH")
            else:
                st.warning("Student Rating: LOW")

    except ValueError:
        st.error("Please enter valid whole numbers in all fields.")