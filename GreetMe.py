import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Hmmm, Suna, de, mitar")
    elif hour >12 and hour<=18:
        speak("Good Afternoon, Shivam")
    else:
        speak("Good Evening,Shivam")

    speak("Hello Shivam,tell me how can i assist you?")
