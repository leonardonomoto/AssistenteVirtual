import speech_recognition as sr
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Pedro')

bot.set_trainer(ListTrainer) #definir treinamento

for __file__ in os.listdir('chats'):
    lines = open('chats/' +__file__, 'r').readlines()
    bot.train(lines)
"""
r = sr.Recognizer()
with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True:
        audio = r.listen(s)
        speech = r.recognize_google(audio, language='pt')
        print('Você disse: ', speech) """