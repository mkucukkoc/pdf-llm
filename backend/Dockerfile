FROM python:3.11-slim

# Sistem bağımlılıkları (tesseract, poppler, ghostscript vs.)
RUN apt-get update && apt-get install -y --no-install-recommends     tesseract-ocr     tesseract-ocr-eng     tesseract-ocr-tur     poppler-utils     ghostscript     libgl1     && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED=1     HF_HUB_DISABLE_TELEMETRY=1
