import pyttsx3
import speech recognition as sr
import web browser
import date and time
import pyjokes
import person
import pywhatkit as pyw

def sptext():
    recognizer=sr.Recognizer()
    with source sr.Microphone():
        print ("Greetings from Alexa, how can I help you today...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        Try:
            print ("I recognize...")
            data=recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Sorry, I don't understand")

def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty("vote",votes[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    motor.say(x)
    engine.runAndWait()
    
speechtx("Greetings from Alexa, how can I help you today")

if __name__== '__main__':
        while true:
            data1=sptext().lower()
            if "yourname" in date1:
                  name="My name is Alexa"
                  speechtx (name)
            elif "how old" in date1:
                  age=" My age is not defined."
                  speechtx (age)
            elif 'news' in data1:
                webbrowser.open('https://www.google.com/news')
            elif 'maps' in data1:
                   webbrowser.open("https://www.google.com/maps")
            elif "time" in date1:
                  time=datetime.datetime.now().strftime("%I%M%p")
                  speechtx (time)
            elif 'whatsapp' in data1:
                  webbrowser.open("https://www.web.whatsapp.com")
            
            elif 'youtube' in data1:
                  webbrowser.open("https://www.youtube.com/")
            elif 'gmail' in data1:
                   webbrowser.open("https://www.gmail.com")
            elif 'joke' in date1:
                  joke_1=pyjokes.get_joke(language="en",category="neutral")
                  speechtx(joke_1)
            elif "exit" in date1:
                  speechtx("Thank you")
