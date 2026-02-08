from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class SongPrompt(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"status": "AI Music GPT is running"}

@app.post("/generate-lyrics")
def generate_lyrics(data: SongPrompt):

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {"role":"system","content":"You write professional song lyrics."},
                {"role":"user","content":data.prompt}
            ]
        }
    )

    lyrics = response.json()["choices"][0]["message"]["content"]

    return {"lyrics": lyrics}
