import requests
from ntpath import join
import pyttsx3  # For audio packages
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from googlesearch import search
from pywhatkit import search
import smtplib
import pywhatkit

engine = pyttsx3.init('sapi5')  # To take input for voice
voices = engine.getProperty('voices')
print(voices[1].id)  # To select the type of voice either male or female
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)  # To speak up the input
    engine.runAndWait()
    pass  # For now, we will write the conditions later.


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak(" I am your personal assistant. How may i help you? ")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query


def message():
    try:
        # sending message to receiver
        # using pywhatkit
        No = input("Enter the number to send message to.")
        pywhatkit.sendwhatmsg("+919419245594",
                              "Hello from GeeksforGeeks",
                              12, 5)
        print("Successfully Sent!")

    except:
        # handling exception
        # and printing error message
        print("An Unexpected Error!")


def google_search():
    # importing the search function from the pywhatkit library
    # initializing a variable with the input
    # text that user wants to search
    speak("What should i search for")
    query1 = takeCommand().lower()
    print(f"Searching...")
    # searching the text using the search() function
    search(query1)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    Id = input("Enter your E-mail ID ")
    PWD = input("Enter your Mail ID Password ")
    server.login('guotaaaarav44@gmail.com', 'deanambrose123')
    server.sendmail('guptaaaarav44@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open' in query:
            comSplit = query.split(" ")
            Website = join(comSplit[1], ".com")
            webbrowser.open(Website)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\acer\\AppData\Local\\Programs\\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'google search' in query:
            google_search()

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = input("Enter the E-mail Id of the reciever ")
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry!. I am not able to send this E-mail")

        elif 'send Whatsapp message' in query:
            message()
