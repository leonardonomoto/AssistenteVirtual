import os

def fechar():
    p = str(input('digite o nome do processo: ')) # definir o nome do processo a ser finalizado.
    os.system('taskkill /im '+(p)) #os.system permite que você digite diretamente no cmd. taskkill /im (nome do processo) é um comando do cmd que finaliza processos.


fechar()