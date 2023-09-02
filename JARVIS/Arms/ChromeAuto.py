# Chrome Automation Source Code :
import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e: 
        print("Say that again please...") 
        return "None"
    return query
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'open chrome' in query:
            os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        elif 'maximize this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')
        elif 'google search' in query:
            query = query.replace("google search", "")
            pyautogui.hotkey('alt', 'd')
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
        elif 'youtube search' in query:
            query = query.replace("youtube search", "")
            pyautogui.hotkey('alt', 'd')
            time.sleep(1)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
        elif 'open new window' in query:
            pyautogui.hotkey('ctrl', 'n')
        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')
        elif 'minimise this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')
        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')
        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl', 'j')
        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        elif 'next tab' in query:
            pyautogui.hotkey('ctrl', 'tab')
        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')
        elif 'close window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'w')
        elif 'clear browsing history' in query:
            pyautogui.hotkey('ctrl', 'shift', 'delete')
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")