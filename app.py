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
