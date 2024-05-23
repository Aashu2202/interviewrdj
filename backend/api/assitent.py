import os
import random
import time
import speech_recognition as sr
import openai
from gtts import gTTS
import playsound
import pyttsx3
from io import BytesIO

apikey = os.getenv("OPENAI_API_KEY")
openai.api_key = apikey

chatStr = ""

def chat(query):
    global chatStr
    chatStr += f"user: Generate a next basic question based on this text {query} programming language\n A.I: "
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k-0613",
            messages=[{"role": "system", "content": chatStr}],
            temperature=0.7,
            max_tokens=256,
            stop=None
        )
        response_text = response['choices'][0]['message']['content'].strip()
        say(response_text)
        chatStr += response_text
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        with open(f"Openai/prompt-{random.randint(1, 4565)}.txt", "w") as f:
            f.write(chatStr)
        return response_text
    except openai.error.OpenAIError as e:
        print("OpenAI Error:", e)
        return "Some Error..."
    except Exception as e:
        print("Error:", e)
        return "Some Error..."

def say(text):
    print(text)
    tts = gTTS(text)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    playsound.playsound(fp)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print(f"User said: {query}")
        return query
    except Exception as e:
        print(e)
        return "Some Error Occurred, sorry..."

if __name__ == "__main__":
    engine = pyttsx3.init()
    say("hello, I am Jarvin, I am your interviewer...")
    say("please... tell me about yourself.")
    query = takeCommand()
    say("Nice to hear about you")
    say("In which technology do you want to give your interview?")

    i = 1
    while i < 4:
        query = takeCommand()
        chat(query)
        i += 1
    query = takeCommand()
    say("thank you")


# import gtts
# import pygame
# import os
# import random
# import speech_recognition as sr
# import openai

# apikey = os.getenv("OPENAI_API_KEY")

# openai.api_key = apikey


# chatStr = ""

# def chat(query):
#     global chatStr
#     chatStr += f"user: Generate a next basic question based on this text {query} programming language\n A.I: "
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo-16k-0613",
#             messages=[{"role": "system", "content": chatStr}],
#             temperature=0.7,
#             max_tokens=256,
#             stop=None
#         )
#         response_text = response['choices'][0]['message']['content'].strip()
#         say(response_text)
#         chatStr += response_text
#         return response_text
#         if not os.path.exists("Openai"):
#             os.mkdir("Openai")
#         with open(f"Openai/prompt-{random.randint(1, 4565)}.txt", "w") as f:
#             f.write(chatStr)
#     except openai.error.OpenAIError as e:
#         print("OpenAI Error:", e)
#         return "Some Error..."
#     except Exception as e:
#         print("Error:", e)
#         return "Some Error..."

# def say(text):
#     print(text)
#     sound = gtts.gTTS(text, lang="en")
#     if os.path.exists("audio.mp3"):
#         os.remove("audio.mp3")
#     sound.save("audio.mp3")
#     # Set the SDL_AUDIODRIVER environment variable to dummy
#     os.environ["SDL_AUDIODRIVER"] = "dummy"
#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.load("audio.mp3")
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
#     pygame.mixer.quit()  # Release resources
#     pygame.quit()  # Clean up
#     os.remove("audio.mp3")  # Remove the audio file after playback



# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#         try:
#             query = r.recognize_google(audio, language="en-in")
#             print(f"User said: {query}")
#             return query
#         except Exception as e:
#             return "Some Error Occurred, sorry..."


            
# if __name__ == "__main__":
#     say("hello, I am Jarvin, I am your interviewer...")
#     say("please... tell me about yourself.")
#     print("Listening....")
#     query = takeCommand()
#     say("Nice to hear about you")
#     say("In which technology do you want to give your interview?")

#     i = 1
#     while i < 4:
#         print("Listening....")
#         query = takeCommand()
#         chat(query)
#         i += 1
#     print("Listening....")
#     query = takeCommand()
#     say("thank you")
# #-----------------------------------------------------

#     say("ok.. give me defination of Object oriented porgraming...")
#     i = 1
#     while i < 4:
#         print("Listeing....")
#         query = takeCommand()
#         chat(query)
#         i += 1
#     print("Listeing....")
#     query = takeCommand()

#     say("So, What is Data base...")
#     i = 1
#     while i < 4:
#         print("Listeing....")
#         query = takeCommand()
#         chat(query)
#         i += 1
#     print("Listeing....")
#     query = takeCommand()

#     say("So, What is SQL.")
#     i = 1
#     while i < 4:
#         print("Listeing....")
#         query = takeCommand()
#         chat(query)
#         i += 1
#     print("Listeing....")
#     query = takeCommand()

#     say("Please tell me about Project you made during your college time")
#     i = 1
#     while i < 6:
#         print("Listeing....")
#         query = takeCommand()
#         chat(query)
#         i += 1
#     print("Listeing....")
#     query = takeCommand()

#     say("ok, Have you create any other projects.. please tell me yes or no")
#     query = takeCommand()
#     if "yes".lower() in query.lower():
#         say("Please tell me about Other Projects")
#         i = 1
#         while i < 5:
#             print("Listeing....")
#             query = takeCommand()
#             chat(query)
#             i += 1
#         print("Listeing....")
#         query = takeCommand()
#     else:
#         say("No.. problem")

#     say("Please tell me about your hobbies")
#     i = 1
#     while i < 3:
#         print("Listeing....")
#         query = takeCommand()
#         chat(query)
#         i += 1
#     print("Listeing....")
#     query = takeCommand()

#     say("What are your greatest strengths")
#     i = 1
#     while i < 3:
#         print("Listeing....")
#         query = takeCommand()
#         chat(query)
#         i += 1
#     print("Listeing....")
#     query = takeCommand()

#     say("What are your greatest Weaknesses")
#     i = 1
#     while i < 3:
#         print("Listeing....")
#         query = takeCommand()
#         chat(query)
#         i += 1
#     print("Listeing....")
#     query = takeCommand()

#     say("Please tell me about some achievement in your life")
#     i = 1
#     while i < 3:
#         print("Listeing....")
#         query = takeCommand()
#         chat(query)
#         i += 1
#     print("Listeing....")
#     query = takeCommand()

#     say("why do you want to work for our company")
#     i = 1
#     while i < 3:
#         print("Listeing....")
#         query = takeCommand()
#         chat(query)
#         i += 1
#     print("Listeing....")
#     query = takeCommand()

#     say("ok.. thank you...")