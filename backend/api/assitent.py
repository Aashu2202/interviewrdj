import os
import random
import speech_recognition as sr
import openai
import pyttsx3
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv('OPEN_AI_ROOT')
openai.api_key = apikey

engine = pyttsx3.init()

chatStr = ""
def call():
    def chat(query):
        global chatStr
        chatStr += f"user: Generate a next basic question based on this text {query} programming language\n A.I: "
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k-0613",
                messages=[{"role": "system", "content": "You: " + chatStr}],
                temperature=0.7,
                max_tokens=256,
                stop=None
            )
            response_text = response.choices[0].message['content'].strip()
            say(response_text)
            print(response_text)
            chatStr += response_text
            return response_text
            if not os.path.exists("Openai"):
                os.mkdir("Openai")
            with open(f"Openai/prompt-{random.randint(1, 4565)}.txt", "w") as f:
                f.write(chatStr)
        except openai.error.OpenAIError as e:
            print("OpenAI Error:", e)
            return "Some Error..."
        except Exception as e:
            print("Error:", e)
            return "Some Error..."

    def say(text):
        try:
            print(text)
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print("Error occurred while speaking:", e)

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language="en-in")
                print(f"User said: {query}")
                return query
            except Exception as e:
                return "Some Error Occurred, sorry..."

    if __name__ == '__main__':
        print('pycharm')
        say("hello, i am jarvin, am your interviewer...")
        say("please... tell me about yourself.")
        query = takeCommand()
        say("Nice to hear about you")
        say("In which technology do you want to give your interview?")
        i = 1
        while i < 4:
            print("Listening....")
            query = takeCommand()
            chat(query)
            i += 1
        print("Listening....")
        query = takeCommand()
        say("ok.. thank you...")
