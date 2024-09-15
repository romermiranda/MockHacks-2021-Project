from macos_speech import Synthesizer
import macos_speech
import speechrecognition as sr
import smtplib
import wikipedia
from datetime import timedelta
import datetime
import webbrowser
import pyttsx3
import os
import pyaudio

mode = 0

print("Initializing Blue")
speaker = Synthesizer(voice='Alex')

MASTER = "name here"

# Microphone
engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 10)
r = sr.Recognizer()

with sr.Microphone(device_index=None) as source:
    audio = r.listen(source)

try:
    recog = r.recognize_google(audio, language='en-US')
    print("You said: " + recog)
    engine.say("You said: " + recog)
    engine.runAndWait()
except sr.UnknownValueError:
    engine.say("Google Speech Recognition could not understand audio")
    engine.runAndWait()
except sr.RequestError as e:
    engine.say(
        "Could not request results from Google Speech Recognition service; {0}"
        .format(e))
    engine.runAndWait()


# Speak function will pronounce the string which is passed to it
def speak(text):
    speaker.say(text)


# This function will show you the current time


def wishMe():
    date = datetime.datetime.now()
    print(date)
    hour = int(date.strftime("%H"))
    print(hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    speak("I am Blue. How may I help you?")


# This will take command from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=None) as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"user said: {query}\n")

    except Exception:
        print("Say that again ")
        query = None
    return query


#
# Main program starts..
speak("Initializing Blue...")
wishMe()

while True:
    query = takeCommand()
    # Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("search Wikipedia for", "")
        results = wikipedia.summary(query, sentences=1)
        print(results)
        speak(results)

    elif 'open soundcloud' in query.lower():
        webbrowser.open("https://soundcloud.com")
        if mode == 0:
            speak("enjoy your music!")
        elif mode == 1:
            speak("aight bet")

    elif 'open youtube' in query.lower():
        if mode == 0:
            webbrowser.open("https://www.youtube.com")
            speak("have fun watching videos!")
        elif mode == 1:
            webbrowser.open("https://www.utube.com/#url=live")
            speak("heres what i found on universal tubing")

    elif 'open weather' in query.lower():
        if mode == 0:
            webbrowser.open(
                "https://weather.com/weather/tenday/l/Silver+Spring+MD?canonicalCityId=c860de7efef4a6b4c35aefa1a5e20ee9134d25ffc9aea297c0994937e12517b4"
            )
        if mode == 1:
            speak("go outside")

    elif 'the time' in query.lower():
        if mode == 0:
            date = datetime.datetime.now()
            print(date)
            time = date.strftime("%H:%M:%S")
            print(time)
            speak(time)
        if mode == 1:
            speak("time for you to get a watch")

    elif 'switch to purple' in query.lower():
        if mode != 1:
            print("Initializing Purple")
            #include code to change to female voice if u can
            speak("You just woke me up from my nap")
            mode = 1

    elif 'switch to blue' in query.lower():
        if mode != 0:
            print("Initializing Blue")
            mode = 0

    elif 'goodbye blue' in query.lower():
        if mode == 1:
            speak("goodbye who")
        if mode == 0:
            speak("bye bye")
            exit()

    elif 'goodbye purple' in query.lower():
        if mode == 1:
            speak("Finally")
            exit()

    elif 'order a pizza' in query.lower():
        if mode == 1:
            speak("does somebody wanna pizza")
            webbrowser.open("https://www.planetfitness.com/")
        elif mode == 0:
            webbrowser.open("https://www.pizzahut.com")
            speak("enjoy your meal!")
