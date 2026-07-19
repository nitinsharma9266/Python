import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import random
import datetime
import time
import requests

# -------------------- SETTINGS --------------------
WEATHER_KEY = "6458cc56f2eaa036c3bc2d08c1acc150"  # Replace with your OpenWeatherMap API key

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)  # Max volume

# Try selecting a clear voice
voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)

def speak(text):
    print(f"Jarvis: {text}")  # Debug print
    engine.say(text)
    engine.runAndWait()

# -------------------- WEATHER --------------------
def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_KEY}&units=metric"
        response = requests.get(url).json()
        if response.get("cod") != 200:
            speak("City not found or API error.")
            return
        temp = response['main']['temp']
        desc = response['weather'][0]['description']
        speak(f"The temperature in {city} is {temp}°C with {desc}")
    except:
        speak("Sorry, I couldn't fetch the weather right now.")

# -------------------- MOTIVATION --------------------
def motivate_me():
    quotes = [
        "Believe in yourself! Every journey begins with a single step.",
        "Do something today that your future self will thank you for.",
        "Hard work beats talent when talent doesn't work hard."
    ]
    speak(random.choice(quotes))

# -------------------- PROCESS COMMAND --------------------
def processCommand(c):
    c = c.lower()
    now = datetime.datetime.now()

    # Websites
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    # Music
    elif c.startswith("play "):
        song_name = " ".join(c.split(" ")[1:])
        if song_name.lower() == "random":
            song = random.choice(list(musicLibrary.music.keys()))
            link = musicLibrary.music[song]
            speak(f"Okay! Playing a surprise song for you: {song}")
            webbrowser.open(link)
        elif song_name in musicLibrary.music:
            link = musicLibrary.music[song_name]
            speak(f"Playing {song_name}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, {song_name} not found in library.")

    # Time & Date
    elif "time" in c:
        speak(f"The current time is {now.strftime('%I:%M %p')}")
    elif "date" in c:
        speak(f"Today is {now.strftime('%A, %B %d, %Y')}")

    # Weather
    elif "weather" in c:
        if "in" in c:
            city = c.split("in")[-1].strip()
            get_weather(city)
        else:
            speak("Please tell me the city. Example: weather in Delhi")

    # Jokes
    elif "joke" in c or "make me laugh" in c:
        jokes = [
            "Why did the computer show up at work late? It had a hard drive!",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "I would tell you a UDP joke, but you might not get it..."
        ]
        speak(random.choice(jokes))

    # Motivation
    elif "motivate me" in c or "quote" in c:
        motivate_me()

    else:
        speak("Sorry, I can't do that.")

# -------------------- MAIN LOOP --------------------
if __name__ == "__main__":
    speak("Hey! May I help you?")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)  # Reduce noise
                print("Listening for wake word...")
                audio = r.listen(source, timeout=15, phrase_time_limit=5)
                word = r.recognize_google(audio)

            if "jarvis" in word.lower():
                speak("Yes?")
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    print("Active Jarvis...")
                    audio = r.listen(source, timeout=20, phrase_time_limit=10)
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")
                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
            continue
