import streamlit as st
import json

st.title("Python Quiz")

uploaded_file = st.file_uploader("Upload your json, example is in 'data/'", type=["json"])

if uploaded_file:
    try:
        quiz_data = json.load(uploaded_file)
        for idx, question_data in enumerate(quiz_data, start=1):
            question = question_data["question"]
            options = question_data["options"]
            correct_answer = question_data["correct_answer"]

            #st.write(f"Question {idx}: {question}")
            st.markdown(f"**Question {idx}:** {question}")
            user_answer = st.radio("Select your answer:", options, index=None)

            if user_answer:
                if user_answer == correct_answer:
                    st.success("Correct!")
                else:
                    st.error(f"The correct answer is: {correct_answer}")
    except json.JSONDecodeError:
        st.error("Invalid JSON file. Please upload a valid JSON file.")
