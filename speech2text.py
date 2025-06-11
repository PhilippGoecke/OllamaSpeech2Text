import sounddevice as sd
import numpy as np
import wave
import requests
import json

# Configuration
OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen3:8b"

def record_audio(filename, duration=5, fs=16000):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wave.write(filename, fs, audio)
    print(f"Saved recording to {filename}")

def transcribe_audio_with_ollama(audio_path):
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()
    # Ollama does not natively support audio, so you need a model that can handle speech-to-text,
    # or use a local Whisper API. Here, we assume you have a Whisper endpoint running.
    whisper_url = "http://localhost:9000/asr"  # Example Whisper API endpoint
    files = {'audio': (audio_path, audio_bytes, 'audio/wav')}
    response = requests.post(whisper_url, files=files)
    if response.status_code == 200:
        transcript = response.json().get("text", "")
        return transcript
    else:
        print("Error transcribing audio:", response.text)
        return ""

def summarize_with_ollama(text):
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": f"Transcribe and summarize the following speech: {text}"
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    if response.status_code == 200:
        result = response.json()
        return result.get("response", "")
    else:
        print("Error from Ollama:", response.text)
        return ""

if __name__ == "__main__":
    audio_file = "speech.wav"
    record_audio(audio_file, duration=5)
    transcript = transcribe_audio_with_ollama(audio_file)
    print("Transcript:", transcript)
    if transcript:
        summary = summarize_with_ollama(transcript)
        print("Ollama summary:", summary)
