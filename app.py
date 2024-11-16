import streamlit as st
import google.generativeai as genai
def result(code):
    key="AIzaSyAHi-rg6OcKjfcXm-QNYrOP7HXVJE-xMYE"
    genai.configure(api_key=key)
    model=genai.GenerativeModel(model_name="gemini-1.5-pro")
    
    prompt=f"""You are an expert Python developer. Please review the following code for bugs, errors, or inefficiencies:
        code is: {code}
        Provide bug report and fixed code only."""
    response=model.generate_content(prompt)

    return response.text

# Set title
st.title("📃 An AI Code Reviewer")

# Input widget with increased height
code = st.text_area("Enter your Python code here:", height=300)

# Submit button
if st.button("Generate"):
    if code:
        res=result(code)
        st.write("Code Review :")
        st.write(res)
    else:
        st.warning("Please enter code before Generating!")
# from openai import OpenAI

# OpenAI API Key (replace with your key or use environment variable for security)

# key = "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"
# c=OpenAI(api_key=key)
# c.models.list()
# import openai
# import os

# # Access the API key securely from the environment
# openai.api_key = "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"

# # List models
# models = openai.Model.list()
# for model in models['data']:
#     print(model['id'])

# import google.generativeai as genai
# key="AIzaSyAHi-rg6OcKjfcXm-QNYrOP7HXVJE-xMYE"
# genai.configure(api_key=key)
# model=genai.GenerativeModel(model_name="gemini-1.5-flash")

# prompt="""You are an expert Python developer. Please review the following code for bugs, errors, or inefficiencies:
#     code is: print("hello"}
#     Provide bug report and fixed code only."""
# response=model.generate_content(prompt)
# print(response.text)