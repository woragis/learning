import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input('What\'s this? ') or 'This was cs50'
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
