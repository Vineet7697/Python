import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
if __name__== "__main__":
    # speak("Hey sir how may i help you")
    speak("Initializing Jarvis......")
    
while True:
#Listen for the wake word "Jarvis"
#obtain audio from the microphone 

    r=sr.Recognizer()
        
        
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio=r.listen(source,timeout=2)
        command=r.recognize_google(audio)
        print(command)
    
    except Exception as e:
        print("error;{0}".format(e))