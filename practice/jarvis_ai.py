import datetime
import speech_recognition as sr
import wikipedia
from gtts import gTTS
import os
import pygame
import time

def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        filename = "voice.mp3"
        tts.save(filename)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # wait until audio finishes
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)

        pygame.mixer.quit()
        os.remove(filename)
    except Exception as e:
        print("Error in speak:", e)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning, I am Jarvis sir. Please tell me how can I help you")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, I am Jarvis sir. Please tell me how can I help you")

    else:
        speak("Good Evening, I am Jarvis sir. Please tell me how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        print("Say that again please...")
        return "None"
    return query.lower()


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand()

        if "wikipedia" in query:
            print("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak("According to Wikipedia")
                speak(results)
            except Exception as e:
                speak("Sorry sir, I could not find any result.")
                print("Error:", e)
