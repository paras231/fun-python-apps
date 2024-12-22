import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



def process_command(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    elif "joke" in command:
        speak("Here is joke for you...")    
    else:
        speak("Sorry, I can't do that yet.")


def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        if command:
            if "exit" in command or "bye" in command:
                speak("Goodbye!")
                break
            process_command(command)

if __name__ == "__main__":
    main()
