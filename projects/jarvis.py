import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import random
import datetime
import time
import requests
import pyaudio
import os
import wikipedia


#  SETTINGS 

WEATHER_KEY = "6458cc56f2eaa036c3bc2d08c1acc150"


#  SPEECH ENGINE

"""engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 165)

engine.setProperty('volume', 1.0)


def speak(text):

    print("Jarvis:", text)

    engine.stop()

    engine.say(text)

    engine.runAndWait(),"""
    


engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


#  STARTUP 

def startup():

    time.sleep(3)

    speak("Hello Nitin")

    speak("All systems are online")

    speak("How can I help you")


#  WEATHER 

def get_weather(city):

    try:

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_KEY}&units=metric"

        response = requests.get(url).json()

        if response.get("cod") != 200:

            speak("City not found")

            return

        temp = response['main']['temp']

        desc = response['weather'][0]['description']

        speak(f"The temperature in {city} is {temp} degree Celsius with {desc}")

    except:

        speak("Weather error")


# MOTIVATION 

def motivate_me():

    quotes = [

        "Believe in yourself",

        "Never give up",

        "Success is coming",

        "You can do it"

    ]

    speak(random.choice(quotes))


# WIKIPEDIA

def search_wikipedia(query):

    try:

        result = wikipedia.summary(query, sentences=2)

        speak(result)

    except:

        speak("I could not find that on Wikipedia")


#  PROCESS COMMAND 

def processCommand(c):

    print("Processing:", c)

    c = c.lower()

    now = datetime.datetime.now()


# OPEN WEBSITES

    if "open google" in c:

        speak("Opening Google")

        webbrowser.open("https://google.com")


    elif "open youtube" in c:

        speak("Opening YouTube")

        webbrowser.open("https://youtube.com")


# TIME DATE

    elif "time" in c:

        speak(now.strftime("%I:%M %p"))


    elif "date" in c:

        speak(now.strftime("%d %B %Y"))


# WEATHER

    elif "weather" in c:

        city = c.replace("weather in", "").strip()

        get_weather(city)


# MUSIC

    elif "play" in c:

        song = c.replace("play", "").strip()

        if song in musicLibrary.music:

            speak("Playing " + song)

            webbrowser.open(musicLibrary.music[song])

        else:

            speak("Song not found")


# OPEN APPS

    elif "open notepad" in c:

        speak("Opening Notepad")

        os.system("notepad")


    elif "open calculator" in c:

        speak("Opening Calculator")

        os.system("calc")


    elif "open chrome" in c:

        speak("Opening Chrome")

        os.system("start chrome")


# WIKIPEDIA

    # WIKIPEDIA

    elif any(word in c for word in [

        "who is",
        "what is",
        "where is",
        "where was",
        "where are",
        "who was",
        "what are",
        "when is",
        "when was",
        "why is",
        "why was",
        "how is",
        "how to",
        "tell me about",
        "define",
        "explain"

    ]):

        search_wikipedia(c)


# MOTIVATION

    elif "motivate me" in c:

        motivate_me()


# THANK YOU

    elif "thank you" in c:

        speak("You are welcome")


# EXIT

    elif "exit jarvis" in c or "stop jarvis" in c:

        speak("Goodbye Nitin")

        exit()


# DEFAULT

    else:

        speak("Sorry, I can't help with that yet")


# MAIN LOOP 

if __name__ == "__main__":

    startup()

    while True:

        r = sr.Recognizer()

        try:

            with sr.Microphone() as source:

                print("\nListening for wake word...")

                r.adjust_for_ambient_noise(source, duration=1)

                audio = r.listen(source)

                word = r.recognize_google(audio)

                print("You said:", word)


            if "jarvis" in word.lower():

                speak("Yes")

                with sr.Microphone() as source:

                    print("Listening for command...")

                    r.adjust_for_ambient_noise(source, duration=0.5)

                    audio = r.listen(source)

                    command = r.recognize_google(audio)

                    print("Command:", command)

                    processCommand(command)


        except Exception as e:

            print("Error:", e)   
            


