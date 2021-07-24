import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning!")
    elif(hour >= 12 and hour < 17):
        speak("Good Afternoon!")
    elif(hour >= 17 and hour < 20):
        speak("Good Evening!")
    else: speak("Good Night!")

    speak("I am Friday sir! Please tell me how may I help you?")


if __name__ == "__main__":
    wishMe()
