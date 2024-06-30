import pyttsx3
import speech_recognition as sr
import cv2
import os
import random
import webbrowser
from datetime import datetime

# Inisialisasi engine untuk sintesis suara
engine = pyttsx3.init()

# Fungsi untuk berbicara
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Fungsi untuk mendengarkan suara
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-US')  # Bahasa Inggris Amerika
            print(f"User: {query}")
            return query
        except Exception as e:
            print("Could not understand audio.")
            return ""

# Fungsi untuk membuka kamera
def open_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # Keluar dari loop jika tombol 'q' ditekan
    cap.release()
    cv2.destroyAllWindows()

# Fungsi untuk membuka YouTube
def open_youtube():
    webbrowser.open("https://youtube.com")

# Fungsi untuk memeriksa waktu
def check_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")
    print(f"The current time is {current_time}")  # Mencetak waktu di terminal

# Fungsi untuk membuka YouTube dan memutar musik
def play_youtube_music(video_url):
    webbrowser.open(video_url)

# Fungsi untuk menjalankan asisten
def virtual_assistant():
    speak("Hi Luthfi, I'm your virtual assistant. How can I help you?")
    while True:
        query = listen().lower()

        if "hi mike" in query:
            speak("Hi, how can I help you?")
        elif "thank you mike" in query:
            speak("Anytime")
            break
        elif "camera" in query:
            speak("Opening camera...")
            open_camera()
        elif "time" in query:
            speak("What time is it...")
            check_time()
        elif "youtube" in query:
            speak("Opening YouTube...")
            open_youtube()
        elif "play music" in query:
            speak("Playing music...")
            play_youtube_music("https://www.youtube.com/watch?v=syFZfO_wfMQ")
        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    virtual_assistant() 
