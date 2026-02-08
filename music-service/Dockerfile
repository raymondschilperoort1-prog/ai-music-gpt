FROM python:3.10-slim

WORKDIR /app

# system deps voor ffmpeg + audio
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel

# eerst normale deps
RUN pip install --no-cache-dir -r requirements.txt

# DAN PyTorch via officiële CPU index
RUN pip install --no-cache-dir \
    torch==2.1.0 \
    torchaudio==2.1.0 \
    torchvision==0.16.0 \
    --index-url https://download.pytorch.org/whl/cpu

# DAN Audiocraft zonder dependency resolver drama
RUN pip install --no-cache-dir git+https://github.com/facebookresearch/audiocraft.git --no-deps

COPY . .

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
