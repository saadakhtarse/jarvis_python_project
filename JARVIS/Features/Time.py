from Body.Speak import Speak
from datetime import datetime

#time_Tell() function tells time in 'HOURS' and 'MINUTES' with 'AM/PM'
#Time in 12Hour formate------------------------------------------------------------- 
def time_Tell():
    time_call = datetime.now()
    tick = (datetime.now())

    if time_call.hour>=0 and time_call.hour<=1:
        Speak(f'It is 12 and {time_call.minute} minute AM')
    elif time_call.hour>=1 and time_call.hour<=11:
        Speak(f'It is {time_call.hour} and {time_call.minute} minute AM')
    elif time_call.hour==12:
        Speak(f'It is 12 and {time_call.minute} minute PM')
    elif time_call.hour>=12:
        Speak(f'It is {time_call.hour-12} and {time_call.minute} minute PM')
    else:
        Speak(f'It is {time_call.hour} and {time_call.minute} minute Sir')


#Time in 24Hour formate-------------------------------------------------------------
# def time_Tell():
#     time_call = datetime.now()
#     tick = (datetime.now())
#     if time_call.hour>=0 and time_call.hour<12:
#         Speak(f'It is {time_call.hour} hour and {time_call.minute} minute AM')
#     else:
#         Speak(f'It is {time_call.hour} hour and {time_call.minute} minut PM')


