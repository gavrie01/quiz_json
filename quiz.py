import streamlit as st
import json

# Load questions and answers from the JSON file
with open('data/Questions_and_Answers.json', 'r') as json_file:
    quiz_data = json.load(json_file)
print(type(quiz_data))

# Create a Streamlit web app
st.title("Quiz")

question_idx = 0

while question_idx < len(quiz_data):
    question_data = quiz_data[question_idx]
    st.write(f"Question {question_idx + 1}: {question_data['question']}")

    with st.form(key=f'question_form_{question_idx}'):
        # Set user_answer initially to None
        user_answer = st.radio("Select your answer:", question_data['answers'], index=None, key=f'radio_{question_idx}')

        if st.form_submit_button("Submit"):
            correct_index = question_data['answers'].index(question_data['correct_answer'])
            user_index = question_data['answers'].index(user_answer)

            # Check if the user's answer index matches the correct answer index
            if user_index == correct_index:
                st.success("Correct!")
                question_idx += 1  # Move to the next question
            else:
                st.error("Incorrect!")