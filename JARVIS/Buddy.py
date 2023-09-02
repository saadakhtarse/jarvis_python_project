from Body.Speak import Speak
from Body.Take_Command import take_command

from Features.Search_features import search_features
from Features.Greeting import greeting
from Features.Greeting import ask_help
from Brain.Brain import main
from Features.Wifi import *

# import Main

import datetime, os

def MainExe():
    print("Buddy File Running...")

    greeting()
    ask_help()
    language = 'eng'
    while True:        
        # query = "'shut down the system' "
        query = take_command(language).lower()
        # query = 'send email' # for non speakable word or unable to talk use this OOOOOOOOOOOOOOOOOOO
        #START----------------------------------------------------------------------------------------
        if "hello" in query:
            Speak("hello sir i am Buddy")
            Speak("What you want me to do?")                
        # talking to AI------------------------------------------------------------------------------
        elif "let's talk" in query:
            Speak("Sure Sir!")
            main()

        #language change------------------------------------------------------------------------------
        elif 'in urdu' in query or 'into urdu' in query:
            language = 'hin'
            Speak("Converting input language from English to Urdu...")
        elif 'in english' in query or 'into english' in query:
            language = 'eng'
            Speak("Converting input language from Urdu to English...")
        #END------------------------------------------------------------------------------------------
        elif "shut down" in query and 'computer' in query:
            Speak("Shutting down your Computer. Good bye Sir!")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            # Main.startExecution.start()

        elif 'bye-bye' in query:
            Speak("Computer is Shutting Down in 5 seconds...") # message will take 3 sec
            os.system("shutdown /s /t 5") # 5 mean 5 sec to shutdown
            #This code uses the shutdown command with the 
            # /s flag to indicate a shutdown operation and the /t 
            # 0 flag to specify that the shutdown should occur immediately (0 seconds delay).
        elif "log off" in query:
            os.system("shutdown /l") # log off computer

        elif 'shut down' in query and 'system' in query:
            Speak("I am shutting down. Good bye Sir!")
            Speak("It was very nice to meet you!")
            exit()

        # Wifi ------------------------------------------------------------------------------------------
        elif "Wi-Fi" in query and "on" in query:
            turn_wifi_on()
            Speak("Wi-Fi turned on!")

        elif "Wi-Fi" in query and "off" in query:
            turn_wifi_off()
            Speak("Wi-Fi turned off!")

        
        else:
            pass

        search_features(query)


# MainExe()