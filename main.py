print('Loading...')
# from selenium import webdriver 
# from selenium.webdriver.chrome.options import Options 
# from selenium.webdriver.support.ui import WebDriverWait
import time
import pyttsx3 #pip install pyttsx3
# from tkinter import *
import os
import random
import speech_recognition as sr #pip install speech_recognition
import datetime
try:
    import pywhatkit # pip install pywhatkit
except Exception as e:
    print(e)
    
import webbrowser
import pyglet
import wikipedia #pip install wikipedia
import smtplib
import pyautogui
# import pyjokes
# import pyPDF2 #pip install pyPDF2

replies_howru = ["Nice", "Fine", "Just doing my Job",
 "I was fine until you asked... Just kidding, hahaha",
 "Physically? Mentally? Spiritually? Socioeconomically? Financially? I'm not sure how to answer that!?!",
 "Sorry I'm busy"]
replies_whoru = ["You don't remember who I am? This must be starting signs of old age.",
 "An inteligent A.I on a stupid computer",
 "I don't know, I've always wondered that myself.",
 "I am Jarvis, a simple A.I who can do various tasks like opening stuff, playing songs, sending email, and other things."]
replies_wsup = ["Sky", "Ceiling. Just kidding, I'm homeless"]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
emailDict = {'name': 'email', 'name2': 'email2'}
contactDict = {'name': 'Phone no.'}
# game_dir = "C:\\Users\\User\\Desktop\\Game_shortcut"
full_list = os.listdir('C:\\Users\\User\\Desktop\\Game_shortcut')
games_lst = []
for i in full_list:
    if '.lnk' in i:
        a=i.replace('.lnk', '')
        games_lst.append(a)
game_short = "C:\\Users\\User\\Desktop\\Game_shortcut"
# root = Tk()
# root.title('Jarvis')

# Function of  whatsapp
hour_time = 0

min_time = 0
def tryAgainh():
    '''
    This will try again if user gave wrong input
    '''
    global hour_time
    try:
        print("Hour: ")
        hour_time = input()
        int(hour_time)
        if hour_time not in range(0,25):
            print('Invalid Input')
            tryAgainh()
    except:
        var = True
        print("Invalid Input")
        while var == True:
            tryAgainh()
def tryAgainm():
    '''
    This will try again if user gave wrong input
    '''
    global min_time
    try:
        print("Minute: ")
        min_time = input()
        int(min_time)
        if min_time not in range(0,60):
            print("Invalid Input")
            tryAgainm()
    except:
        var = True
        print("Invalid Input")
        while var == True:
            tryAgainm()
def sendmsg():
    global min_time
    global hour_time
    speak('Please enter the Phone Number')
    phoneNo = input("Phone no.: ")
    speak("What should I send?")
    content = takeCommand().lower()
    speak("Please enter the time you want send the message")
    tryAgainh()
    tryAgainm()
    pywhatkit.sendwhatmsg(phoneNo, content, hour_time, min_time)

def sendmsg2(phoneNo):
    global min_time
    global hour_time
    speak("What should I send?")
    content = takeCommand().lower()
    speak("Please enter the time you want send the message")
    tryAgainh()
    tryAgainm()
    pywhatkit.sendwhatmsg(phoneNo, content, hour_time, min_time)


def speak(audio):
    '''
    This will take audio from pyttsx3
    And will give output
    '''
    engine.say(audio)
    engine.runAndWait()
    return True
def wishMe():
    '''
    It takes hour from datetime module
    and according to hour it wishes us
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning!")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. Please tell me how may i help you?")
def takeCommand():
    '''
    This will take microphone input command from user
    and gives a string output
    '''
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration = 1)
        # r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")  
        query = r.recognize_google(audio, language = 'en-in')      
        print(f"User said {query}\n")
    except Exception as e:
        print(e)
        #This will run if query is not being recognized by jarvis
        print("Sorry sir, I was unable to recognize. Say that again please...\n")
        return "None"
    return query
def sendEmail(to, content):
    '''
    This will take to Person and content as arguments
    And will send email from given id and password
    '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', "password")
    server.sendmail('email', to, content)
    server.close()
fail = 0
def checkEmail():
    '''
    This fuction will Take the person and will check it if it's in emailDict
    If it's not in it will ask again, or-
    It will then ask to  What to send
    '''
    speak("To whom do you want send email?")
    person = takeCommand().lower()
    try:
        global fail
        if person in emailDict:
            speak("What do you want to send?")
            cont = takeCommand()
            speak("Sending email...")
            sendEmail(emailDict[person], cont)
            speak("Email has been sent!")
        
        if fail == 3:
            speak("Looks like the person you are trying to send email is not in cotact. Please say add to add the person or say continue")
            continue_add = takeCommand()
            if 'add' in continue_add:
                speak("Please write the name below.")
                name = input()
                speak("What do you want to send?")
                content = takeCommand()
                speak("Sending email...")
                sendEmail(name, content)
            elif 'continue' in continue_add:
                pass

        while person not in emailDict:
            speak("Sorry sir, I was unable to send email. Kindly check the name of reciver.")
            fail += 1
            checkEmail()
        
    except Exception as e:
        speak("Sorry sir, I was unable to send email. An error Has occured")
        print(e)
def wishBye():
    '''
    This is made to wish bye if the user quits
    If its night it will Wish Good Night
    or it will just say Bye
    '''
    hour =int(datetime.datetime.now().hour)
    if hour > 18:
        speak("Good Night Sir!")
    else:
        speak("Bye...")
def startStop():
    '''
    This fuction does the same thing as takeCommand,
    But it does'nt print listening or recognizing
    it runs a while loop on line 269 till user says "start"
    When the user says "start" it exits the loop in the elif statement on line 266
    '''
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        # r.pause_threshold = 2
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language = 'en-in')
        true = False
    except:
        true = True
    if true:
        query = ''
    return query
def gameSelect():
    global game_short
    speak("Which one should i open")
    i = 1
    for game in games_lst:
        print(f"{i}. {game}")
        i += 1
    open_game = takeCommand()
    if open_game in games_lst:
        speak(f"Opening {open_game}")
        short_name = "\\" + open_game + ".lnk"
        game_start ="C:\\Users\\User\\Desktop\\Game_shortcut" + short_name
        os.startfile(game_start)
    else:
        speak("Sorry sir, I can't open the game you want. Do you want to tell it again?")
        game_again = takeCommand()
        if 'yes' in game_again:
            gameSelect()
        else:
            speak('Ok')
    
if __name__ == "__main__":
    wishMe()
    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks given by user
        # Wikipidia search -
        if 'Hi' in query:
            speak('Hello')

        elif 'wikipedia' in query:
            '''
            From command or "query" this takes what user said,
            Then it searches in wikipedia through internet, 
            Then reads and displays wikipidea's first 3 sentences  
            '''
            try:
                speak('Searching wikipedia....')
                query = query.replace('wekipedia', '')
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak('Sir, please check your internet connection.')

        # Browser search -
        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")

        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")
        
        elif 'open amazon' in query:
            webbrowser.get('chrome').open("amazon.in")

        elif 'open quara' in query:
            webbrowser.get('chrome').open("quara.com")
        
        elif 'open vedantu' in query:
            webbrowser.get('chrome').open("vedantu.in")
        
        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open("stackoverflow.com")

        elif 'open classroom' in query:
            webbrowser.get('chrome').open("classroom.google.com")

        elif 'open meet' in query:
            webbrowser.get('chrome').open("meet.google.com")

        elif 'open github' in query:
            webbrowser.get('chrome').open("github.com/VedantGawande/")
        
        elif 'open computer' in query:
            pyautogui.keyDown('win')
            pyautogui.keyDown('e')
            pyautogui.keyUp('win')
            pyautogui.keyUp('e')
        # (Location can be changed through music_dir)To play music from YT-
        elif 'play' in query:
            try:
                song = query.replace('play', '')
                speak('Playing '+ song)
                pywhatkit.playonyt(song)
            except Exception as e:
                print(e)
                speak("You are offline. Playing songs from computer")
                music_dir = "C:\\Users\\Public\\Music\\Sample Music\\Music"
                songs = os.listdir(music_dir)
                # random_songs = ""
                os.startfile(os.path.join(music_dir, random.choice(songs)))

        # elif 'play music' in query:
        # Tells the time
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M")
            print(str_time)
            speak(f'Sir, the time is {str_time}')
            
        elif 'the exact time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S:%f")
            print(str_time)
            speak(f'Sir, the time is {str_time} miliseconds')
            
        # Telling jokes
        elif 'joke' in query:
            speak("LOL")

        # Reapeating what user says
        elif 'repeat say' in query:
            speak("What should i say?")
            toSay = takeCommand()
            speak(toSay)

        # Sitching windows
        elif 'switch window' in query:
            pyautogui.keyDown('alt')
            pyautogui.keyDown('tab')
            pyautogui.keyUp('alt')
            pyautogui.keyUp('tab')

        elif 'volume up' in query:
            pyautogui.press('volumeup', presses=5)
            speak('should I increase it more?')
            do_dont = takeCommand().lower()
            if do_dont == 'yes':
                pyautogui.press('volumeup', presses=5)
            else:
                pass

        elif 'volume down' in query:
            pyautogui.press('volumedown', presses=5)
            do_dont = takeCommand().lower()
            speak('should I decrease it more?')
            do_dont = takeCommand().lower()
            if do_dont == 'yes':
                pyautogui.press('volumedown', presses=5)
            else:
                pass

        elif 'mute unmute' in query:
            pyautogui.press('volumemute')

        # Opening applications
        elif 'open counter strike' in query:
            # csPath = os.path.join(game_dir, "\\Counter-strike 1.6 Original\\cstrike.exe")
            csPath = "F:\\Game\\Counter-strike\\cstrike.exe"
            os.startfile(csPath)

        elif 'open fahrenheit' in query:
            # fPath = os.path.join(game_dir, "Fahrenheit\\Fahrenheit.exe")
            fPath = "F:\\Game\\Fahrenheit\\Fahrenheit.exe"
            os.startfile(fPath)

        elif 'open gta vice city' in query:
            print('opening...')
            gtaVcPath = "E:\\GTA VC\\gtavc.exe"
            os.startfile(gtaVcPath)


        elif 'open code' in query:
            codePath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # Sending email
        elif 'send email' in query:
            checkEmail()

        # Stop listening
        elif 'stop listening' in query:
            speak("Ok sir. Please say start to start me.")
            # This basically listens evrything but not react to it or print it
            # out in the console
            k = startStop().lower()
            print('2')
            while 'start' not in k:
                print('1')
                k = startStop().lower()

        elif 'open game' in query:
            gameSelect()
            fail1 = 0    
        # exiting the program
        elif 'close'in query:
            wishBye()
            exit()

        elif 'shut down' in query:
            speak("Shutting down.")
            speak("Do you still want to continue?")
            shutdown = takeCommand().lower()
            if 'yes' in shutdown:
                speak('Shutting down the system in 10 seconds.')
                pywhatkit.shutdown(time=10)
                cancel = takeCommand().lower()
                if 'cancel' in cancel:
                    pywhatkit.cancelShutdown()
                else:
                    pass
            elif 'no' in shutdown:
                speak("System shutdown canceled.")
            # os.system("shutdown /s /t 5")
        
        elif 'send message to' in query:
            query.replace('send message to', '')
            try:
                no = contactDict[query]
                sendmsg2(no)
            except:
                speak('The person you are trying to send message is not in the contact list...')
                sendmsg()
        elif 'send message' in query:
            sendmsg()

        # Replies on normal questions
        elif 'how are you' in query:
            speak(random.choice(replies_howru))
        
        elif "who are you" in query:
            speak(random.choice(replies_whoru))

        elif "what's up" in query:
            speak(random.choice(replies_wsup))

        elif 'laugh' in  query:
            speak('hahahahahahahahahahahahahahahahahahahahah...hahahah...haha...ha')
