import streamlit as st
import requests

# Set up the title and description
st.title("AI-Powered Personalized Learning Assistant")
st.write("Ask any question related to your learning journey, and I’ll assist you!")

# Input box for user question
user_input = st.text_input("Ask a question:")

# When the user clicks the "Ask" button
if st.button("Get Answer"):
    if user_input:
        # Send the user input to the FastAPI backend and get the response
        response = requests.post("http://127.0.0.1:8000/chat/", json={"question": user_input})
        
        # Display the response from the backend (AI)
        if response.status_code == 200:
            ai_response = response.json().get("response")
            st.write("AI's Response: " + ai_response)
        else:
            st.write("Sorry, something went wrong.")
    else:
        st.write("Please enter a question.")
