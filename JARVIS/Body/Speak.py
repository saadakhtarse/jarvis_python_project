# Speack function - two speaeck funstions

# Windows based - pip install pyttsx3
# Chrome based - pip install selenium==4.1.3

# Windows Based -------------------------------------------------------
# Advantages = fast, offlice
# Disadvantages = OverSpeak, less voices

import pyttsx3

def Speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 180)
    print("")
    print(f"Buddy: {audio}")
    print("")
    engine.say(audio)
    engine.runAndWait()


# Chrome Based --------------------------------------------------------

# Advantages = More Voices, More Clear, OverSpeak
# Disadvantages = Word limit(buy subscription), Slow

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from time import sleep

# chrome_options = Options()
# chrome_options.add_argument('--log-level=3') # will not allow selium to disturb while listenig(using buddy)
# chrome_options.headless = True
# Path = 'DataBase\\chromedriver.exe'
# driver = webdriver.Chrome(Path, options=chrome_options)
# driver.maximize_window()

# website = r"https://ttsmp3.com/text-to-speech/British%20English/"
# driver.get(website)  #open website
# Button_selection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/textarea'))
# Button_selection.select_by_visible_text('British English / Brian')


# def Speak(Audio):

#     length_of_Audio = len(str(Audio))

#     if length_of_Audio==0:
#         pass
    
#     else:
#         print("")
#         print(f"AI: {Audio}.")
#         print("")

#         Data = str(Audio)

#         x_path_of_sec = '/html/body/div[4]/div[2]/form/textarea'
#         driver.find_element(By.XPATH, value=x_path_of_sec).send_keys(Data)
#         driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]').click()
#         driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()

#         if length_of_Audio>=30:
#             sleep(4)

#         elif length_of_Audio>=40:
#             sleep(6)
#         elif length_of_Audio>=55:
#             sleep(8)
#         elif length_of_Audio>=70:
#             sleep(10)
#         elif length_of_Audio>=100:
#             sleep(13)
#         elif length_of_Audio>=120:
#             sleep(16)
#         else:
#             sleep(2)


