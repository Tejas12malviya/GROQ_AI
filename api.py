from fastapi import FastAPI
import requests

app=FastAPI()

API_URL="https://api.groq.com/openai/v1/chat/completions"
API_Auth="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"

@app.post("/call_API")
def call(user_message:str):
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer API_Auth"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    return  response.json()
