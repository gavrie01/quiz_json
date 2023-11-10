import streamlit as st
import json
import random

st.title("Quiz ☕")

uploaded_file = st.file_uploader("Upload your json or select existing in 'data/' folder", type=["json"])

if uploaded_file:
    try:
        quiz_data = json.load(uploaded_file)
        random.shuffle(quiz_data)
        for idx, question_data in enumerate(quiz_data, start=1):
            question = question_data["question"]
            options = question_data["options"]
            correct_answer = question_data["correct_answer"]
            image_path = question_data.get("image_path", None)  # Get the image path (if available)

            # Display the question with Markdown (including an image if available)
            st.markdown(f"**Question {idx}:** {question}", unsafe_allow_html=True)
            if image_path:
                st.image(image_path, use_column_width="auto")
            user_answer = st.radio("Select your answer:", options, index=None)

            if user_answer:
                if user_answer == correct_answer:
                #if all(answer in correct_answers for answer in user_answers):
                    st.success("Correct!")
                else:
                    st.error(f"The correct answer is: {correct_answer}")
    except json.JSONDecodeError:
        st.error("Invalid JSON file. Please upload a valid JSON file.")
