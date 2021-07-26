import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import ctypes
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
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
    else:
        speak("Good Evening!")

    speak("I am your assistant sir! Please tell me how may I help you?")


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

        elif 'github' in query:
            speak("Opening Github...")
            webbrowser.open("github.com")

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

        elif 'made you' in query or 'created you' in query or 'developed you' in query:
            pic_dir = 'F:\\My Pic'
            pic = os.listdir(pic_dir)
            webbrowser.open("https://rashed-abir.web.app/")
            os.startfile(os.path.join(pic_dir, pic[131]))
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

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'friday' in query or 'are you here' in query or 'where are you' in query:
            speak("i am here! Please tell me how may I help you sir?")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me friday sir!")

        elif 'search' in query:
            query = query.replace("search", "")
            speak(f"searching {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif 'facebook' in query or 'open facebook' in query:
            speak("Openning Facebook")
            webbrowser.open("https://www.facebook.com/")

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Rashed Khan. further It's a secret")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'today' in query:
            today = datetime.date.today().strftime("%A, %d-%B-%Y")
            speak(f"today is {today}")

        elif 'yesterday' in query:
            today = datetime.date.today()
            yesterday = today - datetime.timedelta(days=1)
            y = yesterday.strftime("%A, %d-%B-%Y")
            speak(f"yesterday was {y}")

        elif 'tomorrow' in query:
            today = datetime.date.today()
            tomorrow = today + datetime.timedelta(days=1)
            t = tomorrow.strftime("%A, %d-%B-%Y")
            speak(f"Tomorow is {t}")

        elif 'exit' in query or 'bye' in query or 'see you later' in query:
            speak("Thanks for giving me your time sir.")
            exit()
