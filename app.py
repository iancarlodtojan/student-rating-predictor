
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
data = joblib.load("student_rating_model.joblib")
model = data["model"]

# Title
st.title("Student Performance Prediction")

st.write("Enter the student's LMS activity data below.")

# Input form
with st.form("prediction_form"):

    submission = st.text_input("Submission Actions", "0")
    quiz = st.text_input("Quiz Actions", "0")
    forum = st.text_input("Forum Actions", "0")
    create = st.text_input("Create Actions", "0")
    read = st.text_input("Read Actions", "0")
    update = st.text_input("Update Actions", "0")
    delete = st.text_input("Delete Actions", "0")
    days = st.text_input("Days Logged In", "0")

    predict = st.form_submit_button("Predict")

# Prediction
if predict:
    try:
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

        if any(value < 0 for value in values):
            st.error("Please enter non-negative numbers.")

        else:
            # Prepare student data
            student_data = pd.DataFrame(
                [values],
                columns=data["features"]
            )

            # Predict rating
            result = model.predict(student_data)[0]

            # Display result
            st.subheader("Prediction Result")

            if result == "High":
                st.write("Likely to Pass")
                st.write("Predicted Rating: High")
            else:
                st.write("Likely to Fail")
                st.write("Predicted Rating: Low")


    except ValueError:
        st.error("Please enter valid whole numbers.")
