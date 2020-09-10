import os

def comando(cmd):
    os.system(cmd)

def desligar():
    t = int(input('Quantos minutos para desligar?'))
    t = str(t*60)
    cmd = 'shutdown -s'+(t)
    comando(cmd)


def main():
    desligar()


os.system('shutdown -s')
print('Desligando')