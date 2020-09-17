import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Fale algo: ') 
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='pt')
        print('Você disse: {}'.format(text))
    except:
        print('Desculpe, eu não entendi.')