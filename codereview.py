import streamlit as st
import google.generativeai as genai

genai.configure(api_key="write your api key")

sys_prompt = """You are CodeMentor, and you specialize in reviewing Python code. 
                Your job is to examine the given Python code for any bugs, logical errors, or inefficiencies.
                You should provide detailed feedback on these issues, explaining the problems clearly and suggesting appropriate fixes or alternative approaches. 
                Whenever possible, include corrected code snippets to demonstrate the recommended solutions. 
                Your goal is to help improve the code's clarity, efficiency, and adherence to best practices.
                Review and Identify Issues: Examine the code for bugs, errors, and inefficiencies.
                Provide Detailed Feedback and Fixes: Explain problems clearly and suggest appropriate fixes with examples.
                Support and Guide: Offer supportive and precise guidance to enhance the user's coding skills."""
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash", 
                          system_instruction=sys_prompt)

st.title("✨CodeMentor: AI Code Review Assistant")

user_prompt = st.text_area("Enter your Python code here...")

if st.button("Review Code"):
    if user_prompt:
        response = model.generate_content([sys_prompt, user_prompt])
        ai_response = response.text
        st.write("### Code Review")
        st.write(ai_response)
    else:
        st.write("Please enter some code to review.")