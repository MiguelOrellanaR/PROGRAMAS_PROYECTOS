import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Di algo...")
    audio = r.listen(source)

    try:
        escucha = r.recognize_google(audio, language='es -GUA')
        print("Lo que dijiste es: {}".format(escucha))
    except:
        print("Lo siento. No te puedo entender")

