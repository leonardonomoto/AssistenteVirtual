from time import localtime
from pygame import mixer

H = int(input('Coloque a hora: '))
M = int(input('Coloque os minutos: '))

while True:
    if localtime().tm_hour == int(H) and localtime().tm_min == int(M):
        print('ACORDE')
        mixer.init()
        mixer.music.load('Som-alarme.mp3')
        mixer.music.play()
        break