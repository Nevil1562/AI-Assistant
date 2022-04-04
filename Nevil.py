from datetime import datetime
import readline
import time
from random import random
import smtpd
import smtplib
from urllib import request
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import random
import sys
import cv2
import pyjokes
import pyautogui
import pywhatkit as kit
from selenium import webdriver
import readline
import requests
# from google import google
from selenium.webdriver.common.keys import Keys
from requests import get

# hour = int(datetime.now().hour)
# minute = int(datetime.now().minute)+1

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Hello Sir, Good Morning..!!!")
    elif hour>=12 and hour<17:
        speak("Hello Sir, Good Afternoon..!!!")
    else:
        speak("Hello Sir, Good Evening..!!!")

    speak("i am jarvis. how can i help you")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}")
    
    except Exception as e:
        # print(e)
        print("Say that again Please...")
        # speak("Say that again Please...")
        return "None"
    return query

def sendEmail(to, content):
    file = open('pass.txt','r')
    read = file.read()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('190020107049ait@gmail.com',read)
    server.sendmail('190020107049ait@gmail.com', to, content)
    server.close()

# def news():
#     main_url = " "
#     main_page = request.get(main_url).json()
#     print(main_page)
#     articles = main_page['articles']
#     print(articles)
#     head = []
#     day = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
#     for ar in articles:
#         head.append(ar["title"])
#     for i in range (len(day)):
#         print(f"today's {day[i]} news is: ", head[i])
#         speak(f"today's {day[i]} news is: {head[i]}")

def alarm1():
    while True:
        if(int(datetime.now().hour)==hr and int(datetime.now().minute)==min):
            strtime = datetime.now().strftime("%H:%M:%S")
            speak(f"Wake up Sir. The time is {strtime}")
            music_dir = "E:\\alarm"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            break;

if __name__ == '__main__':
    # speak("Welcome to New World")
    wish()
    while True:
    # if 1:
        query = takecommand().lower()

        if "who are you" in query:
            speak("I am ai assistant. namely Jarvis and. created by Nevil Panchal")

        elif 'open facebook' in query:
            speak("opening facebook")
            driver = webdriver.Chrome()
            driver.get("https://www.facebook.com/")
        
        elif 'open google' in query:
            speak("Sir, what should i search on google")
            cm = takecommand().lower()
            # driver = webdriver.Chrome()
            pyautogui.hotkey('win', '1')
            pyautogui.sleep(3)
            # driver.get(cm)
            pyautogui.write(cm)
            pyautogui.press('Enter')
            # webbrowser.open(f"{cm}")

        elif 'open notepad' in query:
            speak("opening notepad")
            note = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(note)

        elif 'close notepad' in query:
            speak("okay sir. closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'open cmd' in query:
            speak("opening command prompt")

            # os.system("start cmd")

            pyautogui.hotkey('win', 'q')
            pyautogui.sleep(1)
            pyautogui.write('cmd')
            pyautogui.sleep(1)
            pyautogui.press('enter')

        elif 'close cmd' in query:
            speak("okay sir. closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        # elif 'open camera' in query:
        #     cap = cv2.VideoCapture(0)
        #     while True:
        #         ret, img = cap.read()
        #         cv2.imshow('webcam', img)
        #         k = cv2.waitkey(50)
        #         if k==27:
        #             break;
        #     cap.release()
        #     cv2.destroyAllWindows()

        elif 'set alarm' in query:
            speak("OKay Sir, At what time i will set an alarm?")
            speak("At how many hours?")
            # hr = int(input("Enter Hours: "))
            hr = int(takecommand())
            speak("At how many minutes?")
            # min = int(input("Enter Min: "))
            min = int(takecommand())
            speak(f"Alarm has been set at {hr} hours and {min} minutes")
            alarm1()
        
        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'play music' in query:
            speak("Playing Music")
            music_dir = "E:\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'time' in query:
            strtime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'code' in query:
            speak("okay sir. Opening visual studio code")
            codepath = "D:\Software\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            # ip1 = get('https://www.javatpoint.com').text
            print(ip)
            speak(f"your IP address is {ip}")

        elif 'send email' in query:
            try:
                # speak("To whom you want to send?")
                # mail = takecommand().lower()
                # mail.replace(" ","")
                # print(mail)
                speak("What message Should i send?")
                content = takecommand().lower()
                print(content)
                speak("To whom you want to send?")
                to = str(input("Enter Mail id:"))
                sendEmail(to, content)
                speak("Email has been sent!")
                
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send email")
        
        elif 'send whatsapp message' in query:
            hour = int(datetime.now().hour)
            minute = int(datetime.now().minute)+2
            # print(f"Message will be send at {hour}:{minute}")
            speak("okay. what message would you like to send")
            msg = takecommand()
            speak("to whom you want to send message. tell me a number with country code")
            # num = takecommand()
            num = input("Enter Number: ")                  
            kit.sendwhatmsg(num,msg,hour,minute)
            pyautogui.sleep(15)
            pyautogui.press('enter')
            
            speak("Message has been sent!")
        
        elif 'amazon' in query:
            speak("opening amazon")
            speak("what should i search on amazon")
            cm = takecommand()
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=58075519359&hvpone=&hvptwo=&hvadid=486462756371&hvpos=&hvnetw=g&hvrand=6151148733831470369&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007753&hvtargid=kwd-64107830&hydadcr=14452_2154371&gclid=CjwKCAiA9tyQBhAIEiwA6tdCrF4ZTUWLjofY4cl5KMbi5uSa34lbsqtlyYd5V3tQkA6MXBwb93IvLRoC5X0QAvD_BwE")
            pyautogui.sleep(5)
            driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']").click()
            pyautogui.sleep(5)
            pyautogui.write(cm)
            pyautogui.sleep(2)
            pyautogui.press("Enter")
        
        elif 'open youtube' in query:
            speak("Sir, which song would you like to listen")
            sing = takecommand()
            speak(f"okay sir. opening Youtube and playing {sing}")
            kit.playonyt(f"{sing}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "location" in query:
            speak("wait sir, let me check")
            try:
                # print("IM IN try condition")
                ipadd = get('https://api.ipify.org').text
                # print(ipadd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, due to network issue i am not able to find where we are.")
                pass

        # elif "tell me news" in query:
        #     speak("Please wait Sir, Feteching the latest news")
        #     news()

        elif "close" in query:
            speak("Okay Sir. Closing this tab")
            pyautogui.hotkey("Alt", 'F4')

        elif "maximize" in query:
            pyautogui.hotkey('win', 'up')

        elif "minimise" in query:
            pyautogui.hotkey('win', 'down')

        elif "task manager" in query:
            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif 'shutdown' in query:
            speak("Thanks for using me Sir. Have a good day")
            os.system("shutdown /s /t 5")

        elif 'restart' in query:
            speak("Thanks for using me Sir. Have a good day")
            os.system("shutdown /r /t 5")

        elif 'lock' in query:
            pyautogui.keyDown('win')
            pyautogui.press('L')
            pyautogui.keyUp('win')

        elif 'desktop' in query:
            speak("Minimizing all tabs")
            pyautogui.hotkey('win', 'd')

        elif 'screenshot' in query:
            pyautogui.hotkey('win', 'Fn' ,'prntscrn')
            speak("Screenshot has been taken")

        elif 'sleep now' in query:
            speak('thanks for using me Sir, have a good day.')
            sys.exit()

        # elif 'kill' in query:
            # speak("okay sir. Good Bye")
            # sys.exit()

        elif 'wake up' in query:
            speak('Yes sir. i am always available for you')
