import speech_recognition as sr
import pyttsx3
import time

# Initialize recognizer and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Saying:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        response = recognizer.recognize_google(audio)
        print("You said:", response)
        return response.lower()
    except sr.UnknownValueError:
        return "I didn't catch that"
    except sr.RequestError as e:
        return f"Request failed; {e}"

# Main interaction
response = listen()
speak("You said " + response)

# Loop to keep listening
while True:
    phrase = listen()
    if phrase == "goodbye":
        speak("Goodbye!")
        break
    speak(phrase)
    time.sleep(0.5)
