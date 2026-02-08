from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MUSIC_SERVICE_URL = os.getenv("MUSIC_SERVICE_URL")

class SongPrompt(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"status": "AI Music GPT is running"}

@app.post("/generate-song")
def generate_song(data: SongPrompt):

    # 1 Lyrics maken
    lyrics_response = requests.post(
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
    ).json()

    lyrics = lyrics_response["choices"][0]["message"]["content"]

    # 2 Music service aanroepen
    music_response = requests.post(
        f"{MUSIC_SERVICE_URL}/generate-music"
    ).json()

    return {
        "lyrics": lyrics,
        "music": music_response
    }
