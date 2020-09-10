import os

def desligarPC():
    os.system('shutdown /s')

def reiniciarPC():
    os.system('shutdown /r /t 0')

def hibernar():
    os.system('shutdown /h')
