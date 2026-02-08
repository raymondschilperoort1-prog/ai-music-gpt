from fastapi import FastAPI
from audiocraft.models import MusicGen
import uuid

app = FastAPI()

print("Loading MusicGen model...")
model = MusicGen.get_pretrained("facebook/musicgen-small")
print("Model loaded!")

@app.get("/")
def home():
    return {"status": "Music service running"}

@app.post("/generate-music")
def generate_music():
    prompt = ["romantic french chanson with piano"]

    wav = model.generate(prompt)

    filename = f"{uuid.uuid4()}.wav"
    model.save_wav(wav, filename)

    return {"file": filename}
