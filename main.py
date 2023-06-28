import os
import datetime
from urllib.request import urlopen

import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import smtplib
import ctypes
from bs4 import BeautifulSoup as soup


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommandMicrophone():
    # Принимает на входе аудио от микрофона, возвращает строку с нашими словами
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Используем google для распознания голоса.
        print(f"User said: {query}\n")  # Запрос пользователя выведен.
    except Exception as e:
        # print(e)  используйте только если хотите видеть ошибку!
        print("Say that again please...")  # будет выведено, если речь не распознаётся
        return "None"  # вернётся строка "Пусто"
    return query

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak('I am Sofia, your Artificial intelligence assistant. Please tell me how may I help you')
    #takeCommand()

def sendingEmails():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('baggy.puma0705@gmail.com', 'zjsz skmq ijsn hnwf')
    server.sendmail("baggy.puma0705@gmail.com", "baggy.puma0908@yandex.by", "hello friend. how are you?")
    server.close()

def main():
    greetings()


if __name__ == '__main__':
    main()
    while True:
        query = takeCommandMicrophone().lower()  # Приведём запрос к нижему регистру
        # выполнение задач в соответствии с запросом
        if 'wikipedia' in query:  # если wikipedia встречается в запросе, выполнится блок:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open weather' in query:
            webbrowser.open("gismeteo.by")
        elif 'open university' in query:
            webbrowser.open("gsu.by")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open.' in query: #open dot
            webbrowser.open("dot3.gsu.by")
        elif 'open kinogo' in query:
            webbrowser.open("kinogo.la")
        elif 'open 21 century' in query:
            webbrowser.open("21vek.by")
        elif 'open ticket train' in query:
            webbrowser.open("pass.rw.by")
        elif 'open exchange rates' in query:
            webbrowser.open("myfin.by/currency/")
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
        elif 'open tik-tok' in query:
            webbrowser.open("tiktok.com")
        elif 'open mail' in query:
            webbrowser.open("mail.ru")
        elif 'open kind com' in query:
            webbrowser.open("kind.com")
        elif 'open fishing' in query:
            webbrowser.open("spincity.by")
        elif 'play music' in query:
            music_dir = 'music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open notepad' in query:
            codePath = "C:/Program Files/Notepad++/notepad++.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'open chrome' in query:
            codePath = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'open pascal' in query:
            codePath = "C:/Program Files (x86)/PascalABC.NET/PascalABCNET.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'open cpp' in query:
            codePath = "C:/Program Files (x86)/Dev-Cpp/devcpp.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'open unity' in query:
            codePath = "C:/Program Files/Unity/Hub/Editor/2021.3.9f1/Editor/Unity.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'open wart' in query: #уорд
            codePath = "C:/Program Files/Microsoft Office/root/Office16/WINWORD.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'open powerpoint' in query:
            codePath = "C:/Program Files/Microsoft Office/root/Office16/POWERPNT.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'open access' in query:
            codePath = "C:/Program Files/Microsoft Office/root/Office16/MSACCESS.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'open excel' in query:
            codePath = "C:/Program Files/Microsoft Office/root/Office16/EXCEL.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'open discord' in query:
            codePath = "C:/Users/baggy/AppData/Local/Discord/app-1.0.9007/Discord.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'open yandex' in query:
            codePath = "C:/Users/baggy/AppData/Local/Yandex/YandexBrowser/Application/browser.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'open slack' in query:
            codePath = "C:/Users/baggy/AppData/Local/slack/slack.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'open slack' in query:
            codePath = "C:/Users/baggy/AppData/Local/slack/slack.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'open game' in query:
            codePath = "C:/GOG Games/Machinarium Collector's Edition/Machinarium.exe"  # путь к приложению
            os.startfile(codePath)
        elif 'desktop picture' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:/Users/baggy/Downloads/d7191f0be7d3c209650c74fb00524ff725674bd7.jpg' , 0)
        elif 'news for today' in query:
            try:
                news_url = "https://news.google.com/news/rss"
                Client = urlopen(news_url)
                xml_page = Client.read()
                Client.close()
                soup_page = soup(xml_page, "xml")
                news_list = soup_page.findAll("item")
                for news in news_list[:15]:
                    speak(news.title.text.encode('utf-8'))
            except Exception as e:
                speak(e)
        elif 'email to name' in query:
            try:
                #speak("What should I say?")
                #content = takeCommand()
                #to = "receiver's email id"
                sendingEmails()
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'stop' in query:
            speak("Goodluck. Goodbye!")
            break