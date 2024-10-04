import pyttsx3
import datetime as d
import speech_recognition as sr
import wikipedia
import webbrowser as wb

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def intro():
    speak('hii boss')
    speak('my name is friday')
    speak('kernel version 3.1.0.24')
    speak('i was created on 1st march 2024 and my job is to serve you')
    speak('what can i do for you')

def samay():
    h = int(d.datetime.now().hour)
    m = int(d.datetime.now().minute)
    st = ('it is' , h , 'hours and' ,m ,'minutes now')
    speak(st)

def takeinput():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recognizing...')
        query = r.recognize_google(audio , language = 'en-in')
        print('command given : ' , query)

    except Exception as e:
        print("say that again please...")
        speak("say that again please...")
        takeinput()
        return "none"

    return query

def main():
    flag = 1
    intro()
    while flag>0 :
        query = takeinput().lower()
        a= query.split()
        for i in a:
            if i == 'time':
                samay()
                break

            elif i == 'search' or i == 'who':
                speak('lets see what i found on web')
                query = query.replace(i , '')
                result = wikipedia.summary(query , sentences = 2)
                print(result)
                speak(result)
                break

            elif i == 'youtube' :
                query = query.replace(i , '')
                temp = query.replace(' ' , '+')
                link = "youtube.com/results?search_query=" + temp
                speak('opening youtube for you')
                wb.open(link)

            elif i =='google':
                query = query.replace(i , '')
                temp = query.replace(' ' , '+')
                link = "google.com/search?q=" + temp
                speak('opening google for you')
                wb.open(link)

            elif i =='netflix':
                query = query.replace(i , '')
                wb.open("netflix.com")
            
            elif i =='exit':
                flag = 0


main()
