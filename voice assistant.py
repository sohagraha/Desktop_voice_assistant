import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voice', voices[2].id)
newVoiceRate = 145
engine.setProperty('rate', newVoiceRate)

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

def takeCommand():
    s = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        s.pause_threshold = 1
        audio = s.listen(source)

        try:
            print("Recognizing...")
            query = s.recognize_google(audio, language='en-bn')
            print(f"You Said: {query}\n")
        except Exception as e:
            # print(e)
            print("Say That Again...")
            return "none"
        return query

if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak("Searching Wikipidia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipidea")
        speak(results)

