import speech_recognition as sr
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Jarvis', read_only=True)
"""
bot.set_trainer(ListTrainer) #definir treinamento


for __file__ in os.listdir('chats'): #percorre todos os arquivos em chats
    lines = open('chats/' +__file__, 'r').readlines() #Lê as linhas 
    bot.train(lines)"""

r = sr.Recognizer()
with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True:
        audio = r.listen(s)
        speech = r.recognize_google(audio, language='pt')
        print('Você disse: ', speech) 
        print('Bot: ', bot.get_response(speech))