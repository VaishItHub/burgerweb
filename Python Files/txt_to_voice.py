import pyttsx3 as engine
def textToSpeech(text):
    #initialze pyttsx3 engine
    engine=pyttsx3.init()
    # use engine to say txt
    engine.say(text)
    #wait forthe engine to complete task
    engine.runAndWait()
text=input("enter th text you want to convert to speech")
textToSpeech(text)