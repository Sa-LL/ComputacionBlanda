import speech_recognition as sr
import os
def volverTexto(url):
    url = "C://Users//David Cediel//Google Drive//UTP//Inteligencia Artificial - Comp Blanda - Machine Learning//Blanda//AudioTema" + url

    r = sr.Recognizer()
    with sr.AudioFile(url) as source:
        #print("Speak Anything :")
        audio = r.listen(source)
        text = ''
        try:
            text = r.recognize_google(audio_data = audio, language = "es-MX")
            print(f"You said : {text}")
        except:
            print("Sorry could not recognize what you said")
        return text
