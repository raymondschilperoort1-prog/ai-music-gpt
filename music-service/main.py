from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Music service running"}

@app.post("/generate-music")
def generate_music():
    return {"message": "Music service alive"}
