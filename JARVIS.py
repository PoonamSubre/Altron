import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hi Poonam, Good Morning !")

    elif hour >= 12 and hour < 18:
        speak("Hi Poonam, Good Afternoon !")

    else:
        speak("Hi Poonam, Good Evening !")

    speak("I am Jarvis. Please tell me how may I help you ? ")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'what is the' in query:
            speak('Searching in my brain...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to me")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'who are you' in query:
            speak(
                "i name is Jarvis , i am created by my onwer Poonam and I am using AI domain , my onwer got these idea from avenger caracter called ironman, nice to meet you ")

        elif 'how was your day' in query:
            speak("i enjoy my all day by learing new things and now i am here to share these things to you ")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'song' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"mam, the time is {strTime}")

        elif 'VScode' in query:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'quit' in query:
            speak("ok, bye Poonam catch you later ")

        elif '    ' in query:
            speak("Poonam are you there hello ")

        elif 'mail to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "poojasubre@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry mam ,but I am not able to send this email")
