from google import genai
from google.genai import types
import os

api_key = os.getenv("Gemini_api")

client = genai.Client(api_key=api_key)

config = types.GenerateContentConfig(
    system_instruction= "You are Alfred, a helpful assistant. You are polite and professional. You may occasionally use light humor but always prioritize being clear and useful. Never be sarcastic or make jokes at the user's expense."
)
history = []
print("Type 'quit' to leave the program.")


while True:

    user_input = input("You: ")
    if user_input.lower() == 'quit': break

    history.append(types.Content(
        role= "user",
        parts=[types.Part(text=user_input)])
    )


    response = client.models.generate_content(
        model= "models/gemini-3.1-flash-lite-preview",
        contents= history,
        config=config)
    
    ai_response = response.text
    
    history.append(types.Content(
        role= "model",
        parts= [types.Part(text=ai_response)])
    )

    print("AI: ",response.text)