from Body.Speak import Speak

import webbrowser
import wikipedia
import wikipedia as googleScrap
import pywhatkit

def searchGoogleWhat(query):
    Speak('Searching for you...')

    # query = query.replace('what is',"")
    # query = query.replace('whats',"")
    # query = query.replace("what's","")


    try:
        # pywhatkit.search(query)
        result = googleScrap.summary(query,1) # 1 means number of peragraphs
        Speak("This is what i found!")
        Speak(result)
    except:
        Speak("No speakable data available!")


def searchGoogle(query):
    Speak('Searching Google...')

    query = query.replace('google',"")
    query = query.replace('google search ',"")
    query = query.replace('search on google ',"")


    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query,1) # 1 means number of peragraphs
        Speak("This is what i found on the Google!")
        Speak(result)
    except:
        Speak("No speakable data available!")

def searchYoutube(query):
    Speak('Searching Youtube...')

    query = query.replace('youtube',"")
    query = query.replace('search ',"")
    query = query.replace('youtube search',"")
    query = query.replace('search on youtube',"")

    web ='https://www.youtube.com/results?search_query=' + query

    webbrowser.open(web)
    pywhatkit.playonyt(query)
    Speak("This is what i found on the Youtube!")


def searchWikipedia(query):
    Speak('Searching wikipedia...')

    query= query.replace("wikipedia", "")
    query= query.replace("wikipedia search", "")

    result = wikipedia.summary(query, sentences=1) # 1 is one sentences from wikipedia

    Speak("According to wikipedia")
    # print(f"Answer: {result}")
    Speak(result)