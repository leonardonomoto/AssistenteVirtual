import os

def desligarPC():
    os.system('shutdown /s') #os.system permite que você digite diretamente no cmd. shutdown /s é um comando do cmd para desligar a máquina

def reiniciarPC():
    os.system('shutdown /r /t 0') #shutdown /r /t 0 é um comando do cmd para reiniciar a máquina.

def hibernarPC():
    os.system('shutdown /h') #shutdown /h é um comando do cmd para hiberna a máquina

reiniciarPC()