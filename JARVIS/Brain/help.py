# Make a new file & name it as Dictapp and paste the following code:-

import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
        
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")







# Alarm
elif "set an alarm" in query:
    print("input time example:- 10 and 10 and 10")
    speak("Set the time")
    a = input("Please tell the time :- ")
    alarm(a)
    speak("Done,sir")



# 2nd part

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


# Now make a new file & name it alarm.py and paste the following code:-

import pyttsx3
import datetime
import os 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            os.startfile("music.mp3") #You can choose any music or ringtone 
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)




# 3. Youtube Controls like Play, Pause , Mute , Volume up and down 

elif "pause" in query:
    pyautogui.press("k")
    speak("video paused")
elif "play" in query:
    pyautogui.press("k")
    speak("video played")
elif "mute" in query:
    pyautogui.press("m")
    speak("video muted")

elif "volume up" in query:
    from keyboard import volumeup
    speak("Turning volume up,sir")
    volumeup()
elif "volume down" in query:
    from keyboard import volumedown
    speak("Turning volume down, sir")
    volumedown()


# Now make a new file & name it keyboard.py and paste the following code:-

from pynput.keyboard import Key,Controller

from time import sleep

keyboard = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)



# 4. Reminder

elif "remember that" in query:
    rememberMessage = query.replace("remember that","")
    rememberMessage = query.replace("jarvis","")
    speak("You told me to remember that"+rememberMessage)
    remember = open("Remember.txt","a")
    remember.write(rememberMessage)
    remember.close()
elif "what do you remember" in query:
    remember = open("Remember.txt","r")
    speak("You told me to remember that" + remember.read())


# 2. Calculator

# IMP : - Here first go to "https://www.wolframalpha.com/" and make an account on it then get your own api key and paste in instead 


# Or watch my video if you are unable to get an api key..


elif "calculate" in query:
    from Calculatenumbers import WolfRamAlpha
    from Calculatenumbers import Calc
    query = query.replace("calculate","")
    query = quer




# Now make a new file & name it "Calculatenumbers.py" and write the following code in it :-


import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = "#paste your api key"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")






# 3.Whatsapp automation 


elif "whatsapp" in query:
    from Whatsapp import sendMessage
    sendMessage()


# Now make a new file & name it "Whatsapp.py" and write the following code in it :-

import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do you wan to message")
    a = int(input('''Person 1 - 1
    Person 2 - 2'''))
    if a == 1:
        speak("Whats the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+91000000000",message,time_hour=strTime,time_min=update)
    elif a==2:
        pass







# 5. Temperature

 elif "temperature" in query:
    search = "temperature in Lahore"
    url = f"https://www.google.com/search?q={search}"
    r  = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    speak(f"current{search} is {temp}")
elif "weather" in query:
    search = "temperature in Lahore"
    url = f"https://www.google.com/search?q={search}"
    r  = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    speak(f"current{search} is {temp}")








# 4. Searching from web

elif "google" in query:
    from SearchNow import searchGoogle
    searchGoogle(query)
elif "youtube" in query:
    from SearchNow import searchYoutube
    searchYoutube(query)
elif "wikipedia" in query:
    from SearchNow import searchWikipedia
    searchWikipedia(query)



# Then make a new file and name it SearchNow.py in Vscode and paste the following code :-


import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)