import eel
import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
import threading
import time

# Init eel (web folder)
eel.init("web")

# Voice engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)

running = False


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        return r.recognize_google(audio, language="en-in").lower()
    except:
        return ""


def process_command(command):
    if "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time_now}")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")

    elif "sleep" in command:
        speak("Going back to sleep")


def jarvis_loop():
    global running
    speak("Jarvis is now running")

    while running:
        eel.updateStatus("Sleeping")
        wake = listen()

        if "jarvis" in wake:
            eel.updateStatus("Listening")
            speak("Yes?")
            command = listen()
            process_command(command)

        time.sleep(0.5)


@eel.expose
def start_jarvis():
    global running
    if not running:
        running = True
        threading.Thread(target=jarvis_loop, daemon=True).start()


@eel.expose
def stop_jarvis():
    global running
    running = False
