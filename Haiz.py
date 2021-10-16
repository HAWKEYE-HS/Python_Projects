import pyttsx3
import wikipedia
import speech_recognition as sr
import os
import webbrowser
import datetime
import random
import pywhatkit as kit


def speak(string):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.say(string)
    engine.runAndWait()


numbers = {"om1": "+919975746158",
           "om2": "+918169440441"}


def send_message(query, content):
    query = query.replace("whatsapp message", "")
    query = query.replace(" ", "")
    print(query)
    kit.sendwhatmsg_instantly(numbers[query], content)


def search(query):
    query=query.replace("explore","")
    query=query.replace(" ","",1)
    kit.search(query)


def yt(query):
    query=query.replace("youtube search","")
    query=query.replace(" ","",1)
    print(query)
    kit.playonyt(query)


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour <= 17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("This is Hailee. How may I help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except:
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            print("Searching")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'google' in query:
            webbrowser.open("www.google.com")
        elif 'code' in query:
            path = "C:\\Users\\colorado.colorado-PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")
        elif 'music' in query:
            mk_dir = r'C:\Users\colorado.colorado-PC\Desktop\Music'
            songs = os.listdir(mk_dir)
            i = random.randint(1, 20)
            os.startfile(os.path.join(mk_dir, songs[i]))
        elif 'top headlines' in query:
            path = r'C:\Users\colorado.colorado-PC\Documents\EXE2\dist\Newsraeder\Newsraeder.exe'
            os.startfile(path)
        elif 'instagram' in query:
            path = r'C:\Users\colorado.colorado-PC\PycharmProjects\pythonProject\instagram_downloader_V-2.py'
            os.startfile(path)
        elif 'firefox' in query:
            path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            os.startfile(path)
        elif 'word' in query:
            path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word 2016.lnk'
            os.startfile(path)
        elif 'chrome' in query:
            path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            os.startfile(path)
        elif 'scan' in query:
            path = r'C:\Windows\twain_32\escndv\escndv.exe'
            os.startfile(path)
        elif 'video player' in query:
            path = r'C:\Program Files\VideoLAN\VLC\vlc.exe'
            os.startfile(path)
        elif 'antivirus' in query:
            path = r'"C:\Program Files\Bitdefender\Bitdefender Security\seccenter.exe"'
            os.startfile(path)
        elif 'photoshop' in query:
            os.startfile(r'C:\Program Files\Adobe\Adobe Photoshop CC 2018\Photoshop.exe')
        elif 'pdf reader' in query:
            os.startfile(r'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"')
        elif 'pycharm' in query:
            os.startfile(r'C:\Program Files\JetBrains\PyCharm Community Edition 2021.2\bin\pycharm64.exe')
        elif 'whatsapp' in query:
            speak("Type the message : ")
            content = input()
            send_message(query, content)
        elif 'explore' in query:
            search(query)
        elif 'youtube' in query:
            yt(query)
        elif 'exit' or 'stop' in query:
            exit()
