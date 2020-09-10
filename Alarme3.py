import datetime

hora = int(input('Que horas você quer?'))
minuto = int(input('Que minutos você quer?'))

while True:
    if(hora == datetime.datetime.now().hour and minuto == datetime.datetime.now().minute):
        print('Está na hora!')
        break
