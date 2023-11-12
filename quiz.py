import streamlit as st
import json
import random
import time

correct_answers_counter = 0  # add to st.sidebar


st.title("Quiz ☕")

uploaded_file = st.file_uploader("Upload your json or select existing in 'data/' folder", type=["json"])

if uploaded_file:
    try:
        quiz_data = json.load(uploaded_file)

        # Check if the order has been shuffled before
        if "shuffled_order" not in st.session_state:
            # If not, shuffle the order and store it in the session state
            st.session_state.shuffled_order = list(range(len(quiz_data)))
            random.shuffle(st.session_state.shuffled_order)

        
        for idx, question_idx in enumerate(st.session_state.shuffled_order, start=1):
            question_data = quiz_data[question_idx]
            question = question_data["question"]
            options = question_data["options"]
            correct_answer = question_data["correct_answer"]
            image_path = question_data.get("image_path", None)

            # Use question index as a part of the key to ensure uniqueness
            radio_key = f"question_{idx}"
            
            # Display the question with Markdown (including an image if available)
            st.markdown(f"**Question {idx}:** {question}", unsafe_allow_html=True)
            if image_path:
                st.image(image_path, use_column_width="auto")
            
            user_answer = st.radio(f"Select your answer for Question {idx}:", options, key=radio_key, index=None)

            if user_answer:
                if user_answer == correct_answer:
                    correct_answers_counter += 1
                    st.success("Correct!")
                else:
                    st.error(f"The correct answer is: {correct_answer}")

        # Display the correct answers counter in the sidebar
        st.sidebar.header("Correct / Total")
        st.sidebar.write(correct_answers_counter, "/", len(quiz_data))

    except json.JSONDecodeError:
        st.error("Invalid JSON file. Please upload a valid JSON file.")
