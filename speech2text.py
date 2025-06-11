import whisper
import sounddevice as sd
import wave

# This script records audio from the microphone
def record_audio(filename, duration=5, fs=16000):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes for 'int16'
        wf.setframerate(fs)
        wf.writeframes(audio.tobytes())
    print(f"Saved recording to {filename}")

# This function transcribes the recorded audio using Whisper
def transcribe_audio(audio_path):
    model = whisper.load_model("turbo")
    result = model.transcribe(audio_path, language="de", task="transcribe")
    return result["text"]

# Main function to record audio and transcribe it
if __name__ == "__main__":
    audio_file = "speech.wav"
    record_audio(audio_file, duration=5)
    transcript = transcribe_audio(audio_file)
    print("Transcript:", transcript)
