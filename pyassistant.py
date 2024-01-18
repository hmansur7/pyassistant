import pyaudio
import speech_recognition as sr
import openai
import pyttsx3

openai.api_key = "API Key Hidden"

def getAudio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")

        try:
            audio = recognizer.listen(source, timeout=7)

        except sr.WaitTimeoutError: 
            print("Sorry, I couldn't hear you, try again. Or Say Bye to exit.")
            return None

    try:
        audio = recognizer.recognize_google(audio)
        return audio
    
    except sr.UnknownValueError:
        print("Sorry, I couldn't hear you, try again. Or Say Bye to exit.")
        return None
    
    except sr.RequestError:
        print("Sorry, I couldn't hear you, try again. Or Say Bye to exit.")
        return None

def responseGen(question):
    response = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = [{"role": "system", "content": "You are a voice assistant and your name is Py."}, {"role": "user", "content": question}])

    reply = response['choices'][0]['message']['content']

    return reply

def textToSpeech(text):
    textToSpeech = pyttsx3.init()

    textToSpeech.say(text)
    
    textToSpeech.runAndWait()

if __name__ == "__main__":
      while True:  
        audio = getAudio()

        if audio == "bye":
            print("Okay then. See you.")
            break  

        if audio:
            print(audio)
            print(responseGen(audio))
            textToSpeech(responseGen(audio))
