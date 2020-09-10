import os

def comando(cmd):
    os.system(cmd)

def desligar():
    t = int(raw_input('Quantos minutos para desligar?'))
    t = str(t*60)
    cmd = 'shutdown -s -f -t' + (t)
    comando(cmd)


def main():
    desligar()


main() 