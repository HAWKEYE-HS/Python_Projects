import json
import requests


def speak(str):
    import pyttsx3
    engine = pyttsx3.init()
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty("voice", voice_id)
    engine.say(str)
    engine.runAndWait()


def news_country(link):
    r = requests.get(link)

    news = json.loads(r.text)

    news1 = news['articles']
    for i in range(1, 31):
        main_news = news1[i]['title']
        link = news1[i]['url']
        print(main_news)
        print(f"Click on the following link to know more : {link}")
        if i == 1 or i == 21:
            speak(f"{i}st News : {main_news}")
            speak("Click on the following link to know more")
        elif i == 2 or i == 22:
            speak(f"{i}nd News : {main_news}")
            speak("Click on the following link to know more")
        elif i == 3 or i == 23:
            speak(f"{i}rd News : {main_news}")
            speak("Click on the following link to know more")
        elif 4 <= i <= 10:
            speak(f"{i}th News : {main_news}")
            speak("Click on the following link to know more")
        elif 24 <= i <= 30:
            speak(f"{i}th News : {main_news}")
            speak("Click on the following link to know more")


program_over = False
while not program_over:
    print("Select which country you want to hear the news from : ")
    print("Press 1 for India\n"
          "2 for US\n"
          "3 for UK\n"
          "4 for Australia\n"
          "5 for Japan\n"
          "6 for France\n"
          "7 for Germany\n")
    speak("Select which country you want to hear the news from : ")
    speak("Press 1 for India\n"
          "2 for US\n"
          "3 for UK\n"
          "4 for Australia\n"
          "5 for Japan\n"
          "6 for France\n"
          "7 for Germany\n")
    choice = int(input())
    if choice == 1:
        news_country("https://newsapi.org/v2/top-headlines?country=in&apiKey=b48088826bd94f0ba3489d729d31d38a")
    elif choice == 2:
        news_country("https://newsapi.org/v2/top-headlines?country=us&apiKey=b48088826bd94f0ba3489d729d31d38a")
    elif choice == 3:
        news_country("https://newsapi.org/v2/top-headlines?country=gb&apiKey=b48088826bd94f0ba3489d729d31d38a")
    elif choice == 4:
        news_country("https://newsapi.org/v2/top-headlines?country=au&apiKey=b48088826bd94f0ba3489d729d31d38a")
    elif choice == 5:
        news_country("https://newsapi.org/v2/top-headlines?country=jp&apiKey=b48088826bd94f0ba3489d729d31d38a")
    elif choice == 6:
        news_country("https://newsapi.org/v2/top-headlines?country=fr&apiKey=b48088826bd94f0ba3489d729d31d38a")
    elif choice == 7:
        news_country("https://newsapi.org/v2/top-headlines?country=de&apiKey=b48088826bd94f0ba3489d729d31d38a")
    print("Want to hear more news from another country ? (Y/N)")
    select = input()
    if select == "Y" or select == "y":
        continue
    else:
        program_over = True
print("Press 'Enter' key to exit : ")
input()
