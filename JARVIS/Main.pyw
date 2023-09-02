import typing
from PyQt5.QtWidgets import QWidget
import speech_recognition as sr
import os, sys
from Buddy import MainExe
#from Features.Clap import Tester
from Body.Speak import Speak
# GUI Libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from GUI.Ui import Ui_MainWindow


# MainExe()


# def take_command(): #listeninig...
#     # take microphone input from the user and return string output
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listning...")
#         r.pause_threshold = 0.5 #less the number, more it hears
#         audio = r.listen(source,0,6) # 0,6 means cut and listen after every 6 SECONDS 
    
#     try:
#         print('Recognizing...')
#         query = r.recognize_google(audio, language='eng-in') #for English
#         #query = r.recognize_google(audio, language='hi-In') #for Hindi
#         print(f'Me:"{str(query)}"\n')
#     except Exception as e:
#         # print(e) #show full error
#         print("Say that again please...")
#         return "None"
#     return query

# def wakeup_command():
#     print("Sleeping...")
    
#     query = take_command()

#     if 'wake up' in query:
#         print('"Wake Up" Detected...')

#         MainExe()
#     else:
#         pass


# GUI part here

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.wakeup_command()

    def take_command(self): #listeninig...
        # take microphone input from the user and return string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...")
            r.pause_threshold = 0.5 #less the number, more it hears
            audio = r.listen(source,0,7) # 0,7 means cut and listen after every 6 SECONDS 
        
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='eng-in') #for English
            #query = r.recognize_google(audio, language='hi-In') #for Hindi
            print(f'Me:"{str(query)}"\n')
        except Exception as e:
            # print(e) #show full error
            print("...")
            return "None"
        return query

    def wakeup_command(self):
        print("Sleeping...")
        Speak("Buddy-AI, ready to use... System is in sleep mode.")
        while True:
            self.query = self.take_command()

            if 'wake up' in self.query:
                print('"Wake Up" Detected...')
                MainExe()
            else:
                print("I am sleeping...")



startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # for gifloader.gif
        self.ui.movie = QtGui.QMovie("C:/JARVIS/GUI/gifloader.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        # for initiating.jpeg
        self.ui.movie = QtGui.QMovie("C:/JARVIS/GUI/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        # Time date time bars
        self.current_time = QTime.currentTime() 
        self.current_date = QDate.currentDate()
        # self.label_time = self.current_time.toString('hh:mm:ss') # if you want to show 'seconds' as well 
        self.label_time = self.current_time.toString('TIME: ' + 'hh:mm')
        self.lable_date = self.current_date.toString("dd:MM:yyyy")

        self.ui.textBrowser.setText(self.label_time)
        self.ui.textBrowser_2.setText(self.lable_date)

        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ EXTRA CODE FOR TIME IF NEED
        # self.setWindowTitle("Live Time")
        # self.label_time = QLabel(self)
        # self.label_time.setGeometry(10, 10, 200, 30)
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.update_time)
        # self.timer.start(1000)  # Update time every 1000 milliseconds (1 second)

        # def update_time(self):
        #     current_time = QTime.currentTime()
        #     label_time = current_time.toString('hh:mm:ss')
        #     self.label_time.setText(label_time)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ EXTRA CODE FOR TIME IF NEED
        
        self.ui.pushButton.clicked.connect(self.startTask) # Start Button
        self.ui.pushButton_2.clicked.connect(self.close) # Exit Button

    def startTask(self):
        # for gifloader.gif
        # self.ui.movie = QtGui.QMovie("C:/JARVIS/GUI/gifloader.gif")
        # self.ui.label.setMovie(self.ui.movie)
        # self.ui.movie.start()

        # # for initiating.jpeg
        # self.ui.movie = QtGui.QMovie("C:/JARVIS/GUI/initiating.jpeg")
        # self.ui.label_2.setMovie(self.ui.movie)
        # self.ui.movie.start()

        # timer = QTimer(self)
        # timer.timeout.connect(self.showTime)
        # timer.start(5000)

        startExecution.start()

    def showTime(self):
        self
        # current_time = QTime.currentTime()
        # current_date = QDate.currentDate()
        # label_time = current_time.toString('hh:mm')
        # # lable_date = current_date.toString(Qt.DateFormat)
        # lable_date = current_date.toString(Qt.ISODate)

        # self.ui.textBrowser.setText(label_time)
        # self.ui.textBrowser_2.setText(lable_date)

# # GUI + System run...
app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())




# def wakeUp_call_by_clap():
#     data = Tester()
#     if "True-Mic" == data:
#         print("Wake Up by Clap Detection...")
#         MainExe()


# Speak("i am sleeping...")
# print("Awak by Clap...")
# while True:
#    wakeup_command()