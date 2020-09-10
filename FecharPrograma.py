import os

def fechar():
    p = str(input('digite o nome do processo: '))
    os.system('taskkill /im '+(p))


fechar()