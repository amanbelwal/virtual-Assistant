from datetime import datetime
from importlib.resources import contents
from logging import exception
from logging.config import listen
from threading import main_thread
from pip import main
import pyttsx3                           #install pyttsx3
import datetime
import speech_recognition as sr           #install speechrecognition
import wikipedia                          #install wikipedia
import webbrowser
import os
import smtplib

def sendemail(to,content):
  server=smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.login('amanbelwal.cse2019@ritroorkee.com','roorkee123')
  server.sendmail('amanbelwal.cse2019@ritroorkee.com',to,content)
  server.close()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am edith , please tell me how may i help you")

 
def takeCommand():
 #it takes mic input from user and its output is string
    r=sr.Recognizer() 
    with sr.Microphone() as source:
       print("listening...")
       r.pause_threshold =1
       r.energy_threshold =300
       audio = r.listen(source)
 
    try:
       print("recognising....")
       query=r.recognize_google(audio,language='en-in')
       print(f"user said :{query}\n")   
    
    except Exception as e:
        #print(e)
        print ("say that again plz...")
        return "None"
    return query

if __name__==  "__main__":
    wishme()
    if 1:
      query=takeCommand().lower()

      #logic for executing task
      if 'wikipedia' in query:
          speak("searching wikipedia")
          query=query.replace("wikipedia","")
          results=wikipedia.summary(query,sentences =2)
          speak("according to wikipedia")
          speak(results)
          print(results)


      elif 'open youtube ' in query:  
         webbrowser.open("youtube.com")

      
      elif 'open youtube ' in query:  
         webbrowser.open("google.com")   

      
      elif 'open youtube ' in query:  
         webbrowser.open("stackoverflow.com") 
      
      elif 'play music' in query:
         music_dir="D\\songs\\favourite_song"     
         songs = os.listdir(music_dir) 
         print(songs)
         os.startfile(os.path.join(music_dir,songs[0]))

      elif 'the time' in query:
        strtime =datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir the time is {strtime}")  
      
      elif 'send email to dikshant' in query:
        try:
            speak("what should i say ? ")
            content =takeCommand()
            to= "dikshantbohra.ece2019@ritroorkee.com"
            sendemail(to,content)
            speak("email has been sent")

        except Exception as e:
            print(e)
            speak("i am not able to send email")   
            