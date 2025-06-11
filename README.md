# OllamaSpeech2Text
Ollama Speech2Text

apt install python3-virtualenv  
python3 -m venv .  
source bin/activate

apt install portaudio19-dev  
python3 -m pip install sounddevice numpy requests  

https://github.com/ahmetoner/whisper-asr-webservice
podman run -d -p 9000:9000 -e ASR_MODEL=base -e ASR_ENGINE=openai_whisper docker.io/onerahmet/openai-whisper-asr-webservice:latest

python3 speech2text.py  
