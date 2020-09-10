import os
import datetime
from playsound import playsound

os.system('cleart')
h = int(input('Digite as horas:'))
m = int(input('Digite os minutos:'))
os.system('cleart')
print('Esperando pelo alarme...', h, m)

while True:
    if(h == datetime.datetime.now().hour and m == datetime.datetime.now().minute):
        print('Está na hora!')
        playsound('Som-alarme.mp3')
        break
