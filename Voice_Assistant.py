import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import pywhatkit as pyw

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Greetings from Alexa,How may i help you today...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Recognizing...")
            data=recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Sorry,Not understood")

def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty("voice",voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
    
speechtx("Greetings from Alexa,How may i help you today")

if __name__== '__main__':
        while True:
            data1=sptext().lower()
            if "your name" in data1:
                  name="My name is Alexa"
                  speechtx(name)
            elif "how old" in data1:
                  age=" My age ain't defined."
                  speechtx(age)
            elif 'news' in data1:
                webbrowser.open('https://www.google.com/news')
            elif 'maps' in data1:
                   webbrowser.open("https://www.google.com/maps")
            elif "time" in data1:
                  time=datetime.datetime.now().strftime("%I%M%p")
                  speechtx(time)
            elif 'whatsapp' in data1:
                  webbrowser.open("https://www.web.whatsapp.com")
            
            elif 'youtube' in data1:
                  webbrowser.open("https://www.youtube.com/")
            elif 'gmail' in data1:
                   webbrowser.open("https://www.gmail.com")
            elif 'joke' in data1:
                  joke_1=pyjokes.get_joke(language="en",category="neutral")
                  speechtx(joke_1)
            elif "exit" in data1:
                  speechtx("Thank you")
                
           
