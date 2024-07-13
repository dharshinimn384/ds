import streamlit as st
import requests
import json

st.title("AI Text Generator")
st.write("Enter a prompt to generate text using the PaLM API.")

prompt = st.text_input("Enter your prompt here:")

if st.button("Generate Text"):
    if prompt:
        # Send POST request to Flask API
        url = "http://127.0.0.1:5000/generate-text"
        headers = {'Content-Type': 'application/json'}
        data = {"prompt": prompt}
        
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            if response.status_code == 200:
                result = response.json()
                st.write("Generated Text:")
                st.write(result.get("AI", "No response from API"))
            else:
                st.error(f"Failed to generate text. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt.")
