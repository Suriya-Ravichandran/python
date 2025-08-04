import tkinter as tk
from tkinter import messagebox
from tensorflow.keras.mixed_precision import experimental
import automatic_speech_recognition as asr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os

# Constants
AUDIO_FILE = "mic_input.wav"
SAMPLE_RATE = 16000  # 16 kHz
DURATION = 5  # seconds to record

# Load ASR model
try:
    pipeline = asr.load('deepspeech2', lang='en')
    pipeline.model.summary()
except Exception as e:
    pipeline = None
    print(f"Error loading ASR model: {e}")

# Initialize Tkinter
root = tk.Tk()
root.title("Speech Recognition from Mic")
root.geometry("400x300")

# Function to record audio from microphone
def record_audio():
    try:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "Recording... Please speak.")
        root.update()

        recording = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished

        # Save to WAV file
        wav.write(AUDIO_FILE, SAMPLE_RATE, recording)
        return True
    except Exception as e:
        messagebox.showerror("Recording Error", f"Could not record audio:\n{e}")
        return False

# Function to recognize speech from recorded file
def recognize_speech():
    if not pipeline:
        messagebox.showerror("Error", "ASR model not loaded.")
        return

    if not record_audio():
        return

    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, "Transcribing...")
    root.update()

    try:
        sample = asr.utils.read_audio(AUDIO_FILE)
        sentences = pipeline.predict([sample])
        result_text = sentences[0] if sentences else "No speech detected."
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, result_text)
    except Exception as e:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, f"Transcription failed:\n{str(e)}")

# UI Elements
recognize_button = tk.Button(root, text="Record & Transcribe", command=recognize_speech)
recognize_button.pack(pady=20)

text_output = tk.Text(root, height=5, width=40)
text_output.pack(pady=20)

# Run the GUI
root.mainloop()

# Cleanup (optional)
if os.path.exists(AUDIO_FILE):
    os.remove(AUDIO_FILE)
