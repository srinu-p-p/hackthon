import openai
import os
from dotenv import load_dotenv

# Load the API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, AI! How are you?"}]
)

print(response["choices"][0]["message"]["content"])
