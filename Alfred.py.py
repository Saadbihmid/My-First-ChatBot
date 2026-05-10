from google import genai
import os

api_key = os.getenv("Gemini_api")

client = genai.Client(api_key=api_key)

question = input("Ask me Anything: ")
response = client.models.generate_content(
    model= "models/gemini-3.1-flash-lite-preview",
    contents= question)

print("AI: ",response.text)