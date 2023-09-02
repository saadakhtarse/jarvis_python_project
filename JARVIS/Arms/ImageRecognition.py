# Image Recognition source code :
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
            # [take a screenshot of chrome and crop it, then save the image in jarvis folder]
            img = pyautogui.locateCenterOnScreen('Screenshot1.png')
            pyautogui.doubleClick(img)
            time.sleep(1)
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')
            time.sleep(1)
            # [take screenshot where you want to make the click]
            img1 = pyautogui.locateCenterOnScreen('screenshot2.png')
            pyautogui.click(img1)
            time.sleep(2)
            img2 = pyautogui.locateCenterOnScreen('screenshot3.png')
            pyautogui.click(img2)
            time.sleep(1)
            pyautogui.typewrite('How To Manual', 0.1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('esc')
            img3 = pyautogui.locateCenterOnScreen('screenshot4.png')
            pyautogui.click(img3)
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
# If You Face Any Problem tell me in the
# comment section.

takeCommand()
