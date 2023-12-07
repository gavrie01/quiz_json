import streamlit as st
import json
import random
import base64

correct_answers_counter = 0  # add to st.sidebar
file_path = 'image_by_benzoix_on_Freepic.jpg'
# Function to read an image from a file
def read_image(file_path):
    with open(file_path, 'rb') as file:
        encoded_image = base64.b64encode(file.read()).decode()
    return encoded_image

# Use the read_image function to get the base64 encoded image
encoded_bg_image = read_image(file_path)

# Apply the encoded image to the background style
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/jpeg;base64,{encoded_bg_image}");
    background-position: center; 
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
    right: 2rem;
}}

[data-testid=stSidebar] {{
        background-color: #D6CFC7;
}}
</style>
"""
# Add markdown to the Streamlit sidebar
st.markdown(page_bg_img, unsafe_allow_html=True)
# Add interesting links to the Streamlit sidebar
st.sidebar.markdown("[Matrices & Math_1](http://matrixmultiplication.xyz)")
st.sidebar.markdown("[Matrices & Math_2](https://matrix.reshish.com/)")
st.sidebar.markdown("[Tensors Playground](https://playground.tensorflow.org)")
st.sidebar.markdown("[Binary Cross-Entropy](https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a)")
st.sidebar.markdown("[PyTorch Docs](https://pytorch.org/docs/stable/index.html)")
st.sidebar.markdown("[BERT](https://huggingface.co/blog/bert-101#3-bert-model-size--architecture)")
st.sidebar.markdown("[Attention is all you need](https://arxiv.org/pdf/1706.03762.pdf)")
st.sidebar.markdown("[Dan Jurafsky Book](https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf)")
st.sidebar.markdown("[Graph Sketch](https://graphsketch.com)")
st.sidebar.markdown("[How to generate ...](https://huggingface.co/blog/how-to-generate)")

st.title("Quiz")

# Add a button to clear the session state
clear_state_button = st.button("Clear Session State")

#language selector
#selected_language = st.radio("Select Language", ["English", "German", "Russian"])

# Check if the button is clicked
if clear_state_button:
    st.session_state.clear()

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
            question = question_data["question"].strip()
            options = [option.strip() for option in question_data["options"]]
            correct_answer = question_data["correct_answer"].strip()
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
footer = """



<div style="text-align: center; padding: 10px; background-color: #f0f0f0;">
    <p>&copy; 2023 Quiz | Contact: <a href="mailto:elena.e.gav@gmail.com">Feedback & Questions</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)