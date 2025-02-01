from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Define the input format for user query
class UserQuery(BaseModel):
    question: str

# Define the API route to handle user queries
@app.post("/chat/")
async def chat_with_ai(user_query: UserQuery):
    try:
        # Use OpenAI API to get a response based on the user's question
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change it to gpt-4 if available
            messages=[{"role": "user", "content": user_query.question}]
        )

        # Extract the response content from OpenAI's API response
        ai_response = response["choices"][0]["message"]["content"]
        return {"response": ai_response}

    except Exception as e:
        return {"error": str(e)}
    