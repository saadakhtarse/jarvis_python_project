from email.message import EmailMessage
import ssl
import smtplib
import sys
import os

# to get Body.Speak.py from out side. sys.path.append() change the path
sys.path.append(os.path.abspath("C:/JARVIS"))
from Body.Speak import Speak
from Body.Take_Command import take_command


email_sender = 'saadsaifalasad18@gmail.com'
email_password = 'nccjpfbegebivoth'
# email_receiver = 'f2019065077@umt.edu.pk'


# send_email: main email sending fucntion
def send_email(to,content):
    subject = "Buddy AI - Email"
    #content = "you sucessfully sent the mail to Saad. Congratulations!"

    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = email_sender
    # message['To'] = email_receiver
    message['To'] = to
    message.set_content(content)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, to, message.as_string())
        print('\nEmail send by Buddy...')
    


def Email_send():
    Speak("To whom you want to send email?")

    from Data.Contacts.contacts import get_email_address, get_name
    name = ''
    condition = True

    while condition:
        name = take_command('eng')
        name = get_name(name) #get name from contacts
        to = get_email_address(name) #get id from contacts
        if name == 'exit':
            Speak("exiting email process...")
            return
        elif name == 'None':
            Speak("Say name again please!")
            Speak("There is no such name saved in directory ")
        else:
            condition = False
            
    #print(to) #print email id to whom send email

    Speak('What should i say...')
    content = take_command('eng') # get Content of email to send...
    Speak(content)

    Speak(f"Do you want to send this message to {name.title()}?")
    
    # rejection messages to not set email
    print("Send or Regected Email request ?")
    answer = take_command('eng')
    if 'no' in answer.lower() or 'stop' in answer.lower() or'no' in answer.lower() or 'drop' in answer.lower():
        Speak("Email sending process regected by user.")
    else:
        print("Name: " + name.title() + "\nID: " + to + "Content: " + content)
        Speak("Sending...")
        send_email(to, content) # Main email Send function
        Speak('Email has been sent sucessfully!')



def Email_send_demo():
    
    from Data.Contacts.contacts import get_email_address, get_name
    
    name = "jack"

    name = get_name(name) #get name from contacts
    to = get_email_address(name) #get id from contacts

    Speak('What should i say...')
    content = take_command('eng') # get Content of email to send...
    Speak(content)

    Speak(f"Do you want to send this message to {name.title()}?")
    
    # rejection messages to not set email
    print("Send or Regected Email request ?")
    answer = take_command('eng')
    if 'no' in answer.lower() or 'stop' in answer.lower() or'no' in answer.lower() or 'drop' in answer.lower() or 'abort' in answer:
        Speak("Email sending process regected by user.")
    else:
        print("Name: " + name.title() + "\nID: " + to + "Content: " + content)
        Speak("Sending...")
        send_email(to, content) # Main email Send function
        Speak('Email has been sent sucessfully!')