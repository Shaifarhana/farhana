from gtts import gTTS
import speech_recognition as sr
import playsound
import uuid
import os
'''speech=gTTS('Hey how are you')
speech.save('hey.mp3')'''
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("start talking") #own statement
        audio=r.listen(source,phrase_time_limit=5)
    data=""
    #Exception handling
    try:
        data=r.recognize_google(audio,language='en-IN')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
#listen()
def respond(String):
    print(String)
    tts=gTTS(text=String,lang='en-us')
    tts.save("speech.mp3")
    filename="Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
respond('hey,iam in internship class')





