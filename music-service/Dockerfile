FROM python:3.10-slim

# voorkomt interactieve apt errors
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# 🔥 Installeer EXACT de juiste ffmpeg versie voor PyAV / Audiocraft
RUN apt-get update && apt-get install -y \
    ffmpeg=7:4.4.* \
    libsndfile1 \
    build-essential \
    gcc \
    g++ \
    pkg-config \
    libavformat-dev=7:4.4.* \
    libavcodec-dev=7:4.4.* \
    libavdevice-dev=7:4.4.* \
    libavutil-dev=7:4.4.* \
    libavfilter-dev=7:4.4.* \
    libswscale-dev=7:4.4.* \
    libswresample-dev=7:4.4.* \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies eerst (cache voordeel)
COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# app kopiëren
COPY . .

# Railway verwacht PORT env
ENV PORT=8080

# start FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

