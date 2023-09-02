# import datetime
# import os

# def alarm():
#     nn = int(datetime.datetime.now().hour)
#     # if nn == 15:
#     if True:
#         file = os.path.abspath("C:\\JARVIS\Data")
#         music = os.listdir(file)
#         os.startfile(os.path.join(file, music[0]))






#  NEW CODE FROM HERE

# import sys, os
# sys.path.append(os.path.abspath("C:/JARVIS/Features"))

# def alarm(query):
#     timehere = open("Alarmtext.txt","w")
#     timehere.write(query)
#     timehere.close()
#     os.startfile("Alarm.py")

# alarm("06 and 20 and 00")







# Now make a new file & name it alarm.py and paste the following code:-

import pyttsx3
import datetime
import os, sys

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
    timenow = timenow.replace(" + ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        # currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        currenttime = datetime.datetime.now().strftime("%H:%M")
        currenttime = currenttime + ":00"
        print(f"Alrm TIME set bt you is : {currenttime}")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            sys.path.append(os.path.abspath("C:/JARVIS/Features"))
            os.startfile("alarm.mp3") #You can choose any music or ringtone 
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

# ring(time)