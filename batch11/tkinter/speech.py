import tkinter as tk
import speech_recognition as sr

# Initialize the Tkinter window
root = tk.Tk()
root.title("Speech Recognition")
root.geometry("400x300")

# Function to recognize speech and display the result
def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone for input
    with sr.Microphone() as source:
        text_output.delete(1.0, tk.END)  # Clear previous text
        text_output.insert(tk.END, "Listening...")  # Show listening message
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Capture audio
        
        try:
            # Recognize speech using Google Speech API
            recognized_text = recognizer.recognize_google(audio)
            text_output.delete(1.0, tk.END)  # Clear listening message
            text_output.insert(tk.END, recognized_text)  # Show recognized text
        except sr.UnknownValueError:
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, "Sorry, I could not understand the audio.")
        except sr.RequestError:
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, "Sorry, there was an error with the speech service.")

# Create a Button to start recognition
recognize_button = tk.Button(root, text="Start Recognition", command=recognize_speech)
recognize_button.pack(pady=20)

# Create a Text widget to display the recognized speech
text_output = tk.Text(root, height=5, width=40)
text_output.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()