import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import random
import requests
import pyautogui
from pynput.keyboard import Key, Controller

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)
keyboard = Controller()


emails = {
    ' sohan': 'senapati.sohan31@gmail.com',
    ' subhranshu': 'subhransupatra7324@gmail.com',
    ' rohan': 'senapati.rohan23@gmail.com',
    ' anamika': 'patianamika@gmail.com',
    ' sam': 'luciasam282@gmail.com',
    ' alok': 'alokranjanjoshi07657@gmail.com',
    ' liza': 'lizapatra2002@gmail.com',
    ' bro': 'p18roshan@iima.ac.in'
}

numbers = {
    'sohan': '+919078283132',
    'rohan': '+919100454825',
    'sam': '+919437003500',
    'bro': '+917531987282',
    'Subhransu' : '+919777318748'
}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("please tell Me How may i help you ")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        print("Say That again please")
        speak("Say That again please")
        return "None"
    return query


def beginner():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say the command to activate....")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print("Recognizing....")
        command = r.recognize_google(audio, language='en-in')
        print(f"User Said: {command}\n")

    except Exception as e:
        print(e)
        return "None"
    return command


email_id = os.environ['email_id']
email_pswd = os.environ['email_pswd']

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email_id, email_pswd)
    server.sendmail(email_id, to, content)
    server.close()


while True:
    command = beginner().lower()
    if "jarvis" in command:
        wishme()
        while True:
            query = takecommand().lower()

            if "search wikipedia for" in query:
                speak("Surfing through wikipedia...")
                query = query.replace("search wikipedia for", "")
                results = wikipedia.summary(query, sentences=2)
                speak("I found that")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("www.youtube.com")

            elif 'open google' in query:
                webbrowser.open("www.google.com")

            elif 'open whatsapp' in query:
                webbrowser.open("https://web.whatsapp.com/")

            elif 'open stack overflow' in query:
                webbrowser.open("www.stackoverflow.com")

            elif 'open github' in query:
                webbrowser.open("www.github.com")

            elif 'open facebook' in query:
                webbrowser.open("www.facebook.com")

            elif 'open snapchat' in query:
                webbrowser.open("www.snapchat.com")

            elif 'open instagram' in query:
                webbrowser.open("www.instagram.com")

            elif 'play music' in query:
                music_dir = 'C:\\music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, random.choice(songs)))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"Sir the time is {strTime}")

            elif "the date" in query:
                day = int(datetime.datetime.now().day)
                month = int(datetime.datetime.now().month)
                year = int(datetime.datetime.now().year)
                print(f"{day}/{month}/{year}")
                speak(f"sir the date is {day} {month} {year}")

            elif 'open code' in query:
                codePath = "C:\Microsoft VS Code\Code.exe"
                os.startfile(codePath)

            elif 'open chrome' in query:
                codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(codePath)

            elif 'open edge' in query:
                codePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                os.startfile(codePath)

            elif 'send an email' in query:
                try:
                    query = query.replace("send an email to", "")
                    speak("what should i send")
                    content = takecommand()
                    to = emails[query]
                    sendemail(to, content)
                    speak("Email has been sucessfully sent")
                except Exception as e:
                    print(e)
                    speak("Sorry Boss! i am not able to send the email")

            elif 'send whatsapp message' in query:
                speak("whom should i send the message to ?")
                contact_name = takecommand().lower()
                speak("what should i send")
                message = takecommand()
                pywhatkit.sendwhatmsg_instantly(numbers[contact_name], message)
                pyautogui.press("enter", 1, 5)
        

            elif 'group message' in query:
                speak("what shld i send")
                hour = int(datetime.datetime.now().hour)
                minute = int(datetime.datetime.now().minute) + 0.2
                group_message = takecommand()
                codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(codePath)
                pywhatkit.sendwhatmsg_to_group("L05OubINfe5226ZEMAZEVP", group_message, 18, 00, 2)

            elif 'web search' in query:
                speak("From google i found that")
                query = query.replace("web search", "")
                pywhatkit.search(query)

            elif "shut down my laptop" in query:
                pywhatkit.shutdown()

            elif "cancel shutdown" in query:
                pywhatkit.cancelShutdown()

            elif "close jarvis" in query:
                speak("Have a Good Day sir")
                exit()

            elif "show the weather" in query:
                speak("which city's weather do you want to know about sir?")
                user_api = "1318a0fc30fc99cc8c183a4bfed36423"
                weather_city = takecommand()
                api_link_complete = "http://api.openweathermap.org/data/2.5/weather?q="+weather_city+"&appid="+user_api
                api_link = requests.get(api_link_complete)
                api_data = api_link.json()
                #api_data for the city is below#
                temp_city = ((api_data['main']['temp']) - 273.15)
                feel_temp = ((api_data['main']['feels_like']) - 273.15)
                weather_desc = api_data['weather'][0]['description']
                hmdt = api_data['main']['humidity']
                wind_spd = api_data['wind']['speed']
                print("---------------------------------------------------------------")
                print(f"weather stats for {weather_city} is")
                print("---------------------------------------------------------------")
                speak(f"weather stats for {weather_city} is")
                print(f"The Temperature is {temp_city:.2f} degree celcius.You will feel the temperature to be {feel_temp:.2f} degree celcius.The Humidity is {hmdt}.Weather can be described as {weather_desc}.Wind is blowing at a speed of {wind_spd} Km/h")
                speak(f"The Temperature is {temp_city:.2f} degree celcius . You will feel the temperature to be {feel_temp:.2f} degree celcius . The Humidity is {hmdt} . Weather can be described as {weather_desc} . Wind is blowing at a speed of {wind_spd} kilometer per hour")

            elif "who are you" in query:
                name = "Jarvis"
                created_on = datetime.date(2020, 5, 28)
                present_date = datetime.datetime.now().day
                present_month = datetime.datetime.now().month
                present_year = datetime.datetime.now().year
                created_date = 28
                created_month = 5
                created_year = 2021
                day_from_birth = abs(int(present_date) - int(created_date))
                year_from_birth = abs(int(present_year) - int(created_year))
                month_from_birth = abs(int(present_month) - int(created_month))

                speak(f"Sir i am An Programme made to make Your work easier my name is {name} . I was created on {created_on} . i am {day_from_birth} days {month_from_birth} months {year_from_birth} years old . I am still Devloping")



            elif "play a song" in query:
                speak("which song do you want to listen ? ")
                song_name = takecommand()
                pywhatkit.playonyt(song_name)

                
                
            elif "volume up" in query:
                pyautogui.press("volumeup", 3)

            elif "volume down" in query:
                pyautogui.press("volumedown", 3)

            elif "volume mute" in query:
                pyautogui.press("volumemute")

            elif "what are you doing" in query:
                speak("Sir i am at your service . I listen to your commands and respond accordingly.")


            elif "how are you" in query:
                speak("i am doing great . how about you sir ? ")
                speak("how's your day going ? ")
                answer = takecommand()
                if "yes its a great day" in answer:
                    speak("awesome hope u enjoy a lot . ")

                elif "lot of work to do" in answer:
                    speak("best of luck . sir you can upgrade me so that i can be of more help to you")
                    
                else:
                    speak("sir are u doing well . you don't sound well ? ")
                    answer_1 = takecommand()
                    if "yes i am fine" in answer_1:
                        speak("okay sir . do take a break periodically . hope your day goes well .")
                    elif "no just a bit tired" in answer_1:
                        speak("sir i am closing the program and the device is going to sleep . do take care")
                    else:
                        speak("may everyday be the most happiest day for you")

                
            elif "" in query:
                speak("")

 
    else:
        speak("Jarvis did not activate")
    
