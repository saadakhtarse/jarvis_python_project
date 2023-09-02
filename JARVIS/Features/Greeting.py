from Body.Speak import Speak
import datetime
import random

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak('Good Morning!')
    elif hour>18 and hour<20:
        Speak('Good Afternoon!')
    else:
        Speak('Good Evening!')


def ask_help():
    _rand = random.randint(0,4)
    if _rand==0:
        Speak('How may I help you Sir!')
    elif _rand==1:
        Speak('How can I help you Sir!')
    elif _rand==2:
        Speak("How may I assist you Sir!")
    elif _rand==3:
        Speak("What's going on")
    else:
        pass
