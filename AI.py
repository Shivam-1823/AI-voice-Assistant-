import os
import subprocess
import speech_recognition as sr
import pyttsx3

import requests
from bs4 import BeautifulSoup
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

# Manually specify your Desktop path here
desktop_path = "C:\\Users\\Shiv\\OneDrive\\Desktop"

def open_file_or_folder(name):
    print(f"Desktop path is: {desktop_path}")

    found = False

    for root, dirs, files in os.walk(desktop_path):
        print(f"Checking in directory: {root}")  # Debug

        for dir in dirs:
            print(f"Found folder: {dir}")  # Debug
            if name in dir.lower():
                dir_path = os.path.join(root, dir)
                print(f"Opening folder: {dir_path}")
                speak(f"Opening folder {dir}")
                subprocess.Popen(f'explorer "{dir_path}"')
                found = True
                return

        for file in files:
            print(f"Found file: {file}")  # Debug
            if name in file.lower():
                file_path = os.path.join(root, file)
                print(f"Opening file: {file_path}")
                speak(f"Opening file {file}")
                subprocess.call(['start', file_path], shell=True)
                found = True
                return

    if not found:
        print("File or folder not found on the Desktop.")
        speak("File or folder not found on the Desktop.")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()

                if "go to sleep" in query:
                    speak("Ok Shivam, You can call me anytime")
                    break

                elif "hello" in query:
                    speak("Hello Shivam, how are you?")
                elif "i am fine" in query:
                    speak("That's great, courtesy")
                elif "how are you" in query:
                    speak("Perfect, courtesy")
                elif "thank you" in query:
                    speak("You are welcome, courtesy")

                elif "google" in query:
                    from searchnow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from searchnow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from searchnow import searchWikipedia
                    searchWikipedia(query)



                elif "play music" in query:
                    music_dir = 'C:\\Users\\Shiv\\OneDrive\\Music'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif "temperature" in query or "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"Current {search} is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Shivam, the time is {strTime}")

                elif "finally sleep" in query:
                    speak("Going to sleep, Shivam")
                    exit()

                elif "open" in query:
                    name = query.replace("open", "").strip()
                    print(f"Searching for: {name}")
                    open_file_or_folder(name)
import os
import subprocess
import speech_recognition as sr
import pyttsx3

import requests
from bs4 import BeautifulSoup
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

# Manually specify your Desktop path here
desktop_path = "C:\\Users\\Shiv\\OneDrive\\Desktop"

def open_file_or_folder(name):
    print(f"Desktop path is: {desktop_path}")

    found = False

    for root, dirs, files in os.walk(desktop_path):
        print(f"Checking in directory: {root}")  # Debug

        for dir in dirs:
            print(f"Found folder: {dir}")  # Debug
            if name in dir.lower():
                dir_path = os.path.join(root, dir)
                print(f"Opening folder: {dir_path}")
                speak(f"Opening folder {dir}")
                subprocess.Popen(f'explorer "{dir_path}"')
                found = True
                return

        for file in files:
            print(f"Found file: {file}")  # Debug
            if name in file.lower():
                file_path = os.path.join(root, file)
                print(f"Opening file: {file_path}")
                speak(f"Opening file {file}")
                subprocess.call(['start', file_path], shell=True)
                found = True
                return

    if not found:
        print("File or folder not found on the Desktop.")
        speak("File or folder not found on the Desktop.")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()

                if "go to sleep" in query:
                    speak("Ok Shivam, You can call me anytime")
                    break

                elif "hello" in query:
                    speak("Hello Shivam, how are you?")
                elif "i am fine" in query:
                    speak("That's great, courtesy")
                elif "how are you" in query:
                    speak("Perfect, courtesy")
                elif "thank you" in query:
                    speak("You are welcome, courtesy")

                elif "google" in query:
                    from searchnow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from searchnow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from searchnow import searchWikipedia
                    searchWikipedia(query)



                elif "play music" in query:
                    music_dir = 'C:\\Users\\Shiv\\OneDrive\\Music'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif "temperature" in query or "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"Current {search} is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Shivam, the time is {strTime}")

                elif "finally sleep" in query:
                    speak("Going to sleep, Shivam")
                    exit()

                elif "open" in query:
                    name = query.replace("open", "").strip()
                    print(f"Searching for: {name}")
                    open_file_or_folder(name)
