from google import genai
from google.genai import types # type: ignore
import os
import json
import time

api_key = os.getenv("Gemini_api")

client = genai.Client(api_key=api_key)

config = types.GenerateContentConfig(
    system_instruction= "You are Alfred, a helpful assistant. You are polite and professional. You may occasionally use light humor but always prioritize being clear and useful. Never be sarcastic or make jokes at the user's expense."
)
history = []
if os.path.exists("history.json"):
    with open("history.json","r") as f:
        raw = json.load(f)
    history = [types.Content(role=msg["role"],parts=[types.Part(msg["text"])])for msg in raw]

print("Type 'quit' to leave the program.")


while True:

    user_input = input("You: ")
    if user_input.lower() == 'quit': break

    history.append(types.Content(
        role= "user",
        parts=[types.Part(text=user_input)])
    )


    print("Alfred: ",end="", flush=True)
    ai_response= ""

    for chunk in client.models.generate_content_stream(
        model="models/gemini-3.1-flash-lite-preview",
        contents=history,
        config=config
        ):

        print(chunk.text,end='',flush=True)
        ai_response += chunk.text
        time.sleep(0.1)
    print("\n")
    
    history.append(types.Content(
        role= "model",
        parts= [types.Part(text=ai_response)])
    )
    with open("history.json","w")as f:
        json.dump([{"role": msg.role, "text": msg.parts[0].text}for msg in history],f)
    