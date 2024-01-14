import speech_recognition as sr
from datetime import datetime
from utils import opening_text
import os
import random

# speech recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 0.5
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language="en-in")
        print(f"User: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Speech recognition request failed: {e}")
        return None

# simple text-based response
def generate_response():
    res = random.choice(opening_text)
    return res

# greeting user based on current time
def greet_user(USERNAME):
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        print(f"Good Morning {USERNAME}")
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        print(f"Good afternoon {USERNAME}")
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        print(f"Good Evening {USERNAME}")
        speak(f"Good Evening {USERNAME}")
    print(f"I am Jarvis. How may I assist you today?")
    speak(f"I am Jarvis. How may I assist you today?")
    
# say goodbye to user based on current time
def bye_user():
    hour = datetime.now().hour
    if hour >= 21 and hour < 6:
        print("Good night sir, take care!")
        speak("Good night sir, take care!")
    else:
        print('Have a good day sir!')
        speak('Have a good day sir!')
        
def weather():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        print(f"It is bright and sunny today, sir.")
        speak(f"It is bright and sunny today, sir.")
    elif (hour >= 12) and (hour < 16):
        print(f"The sun is going to set soon, sir")
        speak(f"The sun is going to set soon, sir")
    elif (hour >= 16) and (hour < 19):
        print(f"It is dark outside, sir")
        speak(f"It is dark outside, sir")

# speech synthesis 
def speak(text):
    os.system(f'say "{text}"')
    
# Main loop for JARVIS
if __name__ == "__main__":
    greet_user("Nartnatta")
    
    while True:
        user_input = recognize_speech()

        if user_input:
            if "exit" in user_input.lower() or "stop" in user_input.lower():
                bye_user()
                break
            elif "weather" in user_input.lower():
                weather()
            else:
                response = generate_response()
                print(response)
                speak(response)
