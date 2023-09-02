from Body.Speak import Speak
from Body.Take_Command import take_command

from Features.Time import time_Tell
from Features.Mail import *
from Features.Dictionary import Get_meaning
from Features.Music_search import *
from Features.Alarm import ring
from Features.Key_operations import *
from Features.Brows import *
from Features.Brows import searchGoogleWhat 
import os
import requests
from bs4 import BeautifulSoup

    

def search_features(query):
    #logic for executing tasks based on query
       
        
    # KEYBOARD FUNCTIONS
    if 'ok' in query or 'okay' in query or 'press' in query or 'click' in query:
        press_enter_key() # Press Enter if the tab on any Button
    
    elif 'scroll up' in query or 'up' in query or 'move up' in query:
        scroll_up()
    
    elif 'scroll' in query or 'scroll down' in query or 'move down' in query:
        scroll_down()

    elif 'switch' in query or 'change' in query or 'other' in query and 'window' in query:
        switch_to_previous_window()

    # show not working as it should ???????????????????????????????????????????????
    elif 'show this window' in query:
        show_window()
    
    elif 'close' in query and 'window' in query or 'close' in query and 'this' in query or "stop it too" in query:
        close_current_window()

    elif 'minimize' in query and 'window' in query:
        minimize_current_window()
    
    elif 'dictionary' in query:
        Speak("Tell me the word to search...")
        word = take_command("eng")
        Speak(Get_meaning(word))

    elif 'time' in query:
        time_Tell()

    elif 'song' in query or 'music' in query:
        music_search_demo(query)




        


    elif 'alarm' in query:
        Speak("Alarm function initiating...")
        print("Input time example:- 10 and 10 and 10 ")
        Speak("Set the time")
        # _input = input("Please enter the time:- ")
        _input = take_command('eng')
        ring(_input)
    # Error in ALARM XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    # inhance  OPEN code XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    elif 'open' in query:
        dictapp = {"commandprompt" : "cmd",
                    "paint" : "mspaint" ,
                    "my computer": "explorer",
                    "recycle bin": "explorer.exe shell:RecycleBinFolder",

                    "notepad": "notepad",  # Open Notepad
                    "browser": "chrome",  # Open a web browser (replace 'chrome' with the appropriate browser command on your system)
                    "calculator": "calc",  # Open the calculator
                    "calendar": "outlookcal:",  # Open the default calendar application (e.g., Outlook Calendar)
                    "email": "start outlook:",
                    "command prompt": "cmd",  # Open Command Prompt
                    "terminal": "start cmd",
                    "task manager": "taskmgr",  # Open Task Manager
                    "control panel": "control",  # Open Control Panel
                    "file explorer": "explorer",  # Open File Explorer
                    "settings": "ms-settings:",  # Open the Windows Settings app
                    "system info": "systeminfo",  # Display system information in the command prompt
                    "device manager": "devmgmt.msc",  # Open Device Manager

                    "download": "explorer \"C:\\Path\\To\\Downloads\\Folder\"",
 
                    "word" : "winword" , 
                    "excel" : "excel" , 
                    "chrome" : "chrome" , 
                    "vs code" : "code" ,
                    "powerpoint" : "powerpnt"}
        
        # def openAppWeb(query):
        if ".com" in  query or ".co.in" in  query or ".org" in  query or ".edu" in  query or ".in" in query:
            query = query.replace("open","")
            query = query.replace("launch","")
            query = query.replace(" ","")
            webbrowser.open(f"https://www.{query}")

            Speak("Launching, Sir!")
        else:
            keys = list(dictapp.keys())
            for app in keys:
                if app in query:   
                    os.system(f"start {dictapp[app]}") 

                    query = query.replace("open","")   
                    Speak(f"Launching,{query} Sir!") 
    # inhance  OPEN code XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    

    

    # ONLINE FUNCTIONS ------------------------------------------------------------------------------------------


    elif 'Google search' in query or "search on google" in query or "search" in query and "on google" in query:
        searchGoogle(query)
    
    elif 'youtube search' in query or "search" in query and "on youtube" in query:
        searchYoutube(query)

    elif 'wikipedia' in query:
        searchWikipedia(query)
    
    elif 'send' in query and "email" in query:
        Email_send_demo()
    
    elif (('open' or 'play') and 'youtube') in query:
        webbrowser.open("youtube.com")

        Speak("opening youtube")
        print("YouTube opening....")

    elif ('open' and 'google') in query:
        webbrowser.open("google.com")
        
        Speak("opening google")
        print("Google opening....")

    elif "what" in query and "is" in query or "who" in query and "is" in query or "how" in query and "to" in query:
        searchGoogleWhat(query)
    





    elif 'open' in query:            #it must wrote before ELSE part
        Speak("Open what ?")
    else:
        pass

    query = ""