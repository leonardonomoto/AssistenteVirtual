import speech_recognition as sr
from chatterbot.trainers import ListTrainer



r = sr.Recognizer()

"""
with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True:
        audio = r.listen(s)
        speech = r.recognize_google(audio, language='pt')
        print('Você disse: ', speech) """