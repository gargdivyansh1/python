import pyttsx3

# this is used when we want the system to speak the information

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()