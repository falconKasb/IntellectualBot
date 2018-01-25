import speech_recognition as sr


with () as source:
    
    audio = r.listen(source)

try:
     print(r.recognize_google(audio, language="ru-RU"))
except sr.UnknownValueError:
    print("Робот не расслышал фразу")
except sr.RequestError as e:
    print("Ошибка сервиса; {0}".format(e))