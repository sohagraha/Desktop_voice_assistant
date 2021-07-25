import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('abir97bd@gmail.com', 'password')
    server.sendmail('abir97bd@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipidia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipidea")
            speak(results)

        elif 'youtube' in query:
            speak("Oppening Youtube...")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")
    
        elif 'stack overflow' in query:
            speak("Opening stackoverflow...")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or 'play songs' in query or 'play song' in query:
            music_dir = 'E:\\MP3 Songs'
            songs = os.listdir(music_dir)
            speak("Playing Music...")
            os.startfile(os.path.join(music_dir, songs[0]))
    
        elif 'play videos' in query or 'play video' in query:
            video_dir = 'D:\\Video Songs'
            videos = os.listdir(video_dir)
            speak("Playing Video...")
            os.startfile(os.path.join(video_dir, videos[0]))

        elif 'made you' in query or 'create you' in query or 'developed you' in query:
            pic_dir = 'F:\\My Pic'
            pic = os.listdir(pic_dir)
            webbrowser.open("https://rashed-abir.web.app/")
            os.startfile(os.path.join(pic_dir, pic[128]))
            speak("its Rashed Khan")

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"the time is {time}")

        elif 'open code' in query or 'vs code' in query:
            codePath = 'C:\\Users\\rashe\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            speak("Openning code...")
            os.startfile(codePath)

        elif 'open postman' in query or 'postman' in query:
            postmanPath = 'C:\\Users\\rashe\\AppData\\Local\\Postman\\Postman.exe'
            speak("Openning postman...")
            os.startfile(postmanPath)

        elif 'open popcorn' in query or 'pop corn' in query or 'showtime' in query or 'show time' in query:
            popcornPath = 'C:\\Program Files (x86)\\Popcorn Time\\PopcornTimeDesktop.exe'
            speak("Enjoy your time, sir...")
            os.startfile(popcornPath)

        elif 'send a mail' in query:
            try:
                speak("what should I say?")
                conntent = takeCommand()
                print(f"your messege: {conntent}\n")
                speak("whome should i send")
                to = input("Mail to: ")
                sendEmail(to, conntent)
                speak("Email has been sent !")
            except Exception as e:
            # print(e)
                speak("I am not able to send this email")

        elif 'friday' in query:
            speak("i am here! Please tell me how may I help you sir?")
    
        elif 'exit' in query or 'bye' in query or 'see you later' in query:
            speak("Thanks for giving me your time sir.")
            exit()