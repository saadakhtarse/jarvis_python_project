


from datetime import time
import datetime
import sys
import winsound
import os
# root = os.path.dirname(os.path.abspath("C:\JARVIS\Data"))
# os.path.abspath("C:\JARVIS\Data")

# to get Body.Speak.py from out side. sys.path.append() change the path
sys.path.append(os.path.abspath("C:/JARVIS/Features"))


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

def alarm(set_alarm):
    # Infinite Loop
    while True:
        # Set Alarm
        # set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one seconds
        time.sleep(1)
 
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
 
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm:
            print("Time to Wake up")
            # Playing sound
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)


# sys.path.append(os.path.abspath(r"C:\JARVIS\Features"))
# os.path.abspath("C:/JARVIS")
# winsound.PlaySound.playsound("NOKIA_3310.mp3",True)

# print(datetime.datetime.now().strftime("%H:%M:%S"))

# winsound.PlaySound('alarm.mp3',False)


#winsound.PlaySound("NOKIA_3310.mp3",winsound.SND_ASYNC)
# os.startfile(os.path.join(root, "NOKIA_3310.mp3"))
actual_time()
# print("ply.........")














# BUG PART HERE



    # # error in Temperature + Weather XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    # elif 'temperature' in query:
    #     city_name = "Lahore"
    #     url = f"https://www.weather.com/weather/today/l/{city_name}"
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.content, "html.parser")

    #     temperature_element = soup.find("span", class_="CurrentConditions--tempValue--3KcTQ")
    #     if temperature_element:
    #         temperature = temperature_element.text
    #         return temperature
    #     else:   
    #         Speak("Temperature element not found.")
    #         return None


    #     # search = "temperature in Lahore"
    #     # url = f"https://www.google.com/search?q={query}"
    #     # r = requests.get(url)
    #     # data = BeautifulSoup(r.text,'html.parser')
    #     # # temp = data.find("div", class_ = "BNeawe").text() # Get Celceius Temperature

    #     # element = data.find("div", class_="BNeawe")
    #     # if element is not None:
    #     #     temp = element.text
    #     #     # Further processing with the temperature value
    #     # else:
    #     #     # Handle the case when the element is not found
    #     #     print("Temperature element not found.")


    #     # Speak(f"current {search} is {element}")

    #     # import requests
    #     # from bs4 import BeautifulSoup

    #     # def get_current_temperature(city_name):
    #     #     url = f"https://www.weather.com/weather/today/l/{city_name}"
    #     #     response = requests.get(url)
    #     #     soup = BeautifulSoup(response.content, "html.parser")

    #     #     temperature_element = soup.find("span", class_="CurrentConditions--tempValue--3KcTQ")
    #     #     if temperature_element:
    #     #         temperature = temperature_element.text
    #     #         return temperature
    #     #     else:
    #     #         Speak("Temperature element not found.")
    #     #         return None

    #     # Replace "City Name" with the name of the city you want to retrieve the temperature for
    #     city_name = "Lahore"

    #     temperature = get_current_temperature(city_name)
    #     if temperature is not None:
    #         Speak("Current temperature in", city_name, "is", temperature)

    #     elif 'weather' in query:
    #         # query = "weather in Lahore"
    #         url = f"https://www.google.com/search?q={query}"
    #         r = requests.get(url)
    #         data = BeautifulSoup(r.text,'html.parser')
    #         temp = data.find("div", class_ = "BNeawe").text() # Get Celceius Temperature

    #     # Speak(f"current {search} is {temp}")

    # # error in Temperature XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



    # # OFFLINE FUNCTIONS ------------------------------------------------------------------------------------------


    # # Error in ALARM XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    # # watch this video to get ir RIGHT
    # # https://www.youtube.com/watch?v=rgGDTO8g2Pg