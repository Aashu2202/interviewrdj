# import os
# import random

# import speech_recognition as sr
# import openai
# import pyttsx3
# from pyttsx3.drivers import sapi5
# import sys
# # if sys.platform == 'win32':
# #     import win32com.client



# apikey = ""
# openai.api_key = apikey
# #  sp = win32com.client.Dispatch("SAPI.SpVoice")
# # engine = pyttsx3.init()
# engine = pyttsx3.init(driverName="sapi5")
# # Set properties (optional)
# engine.setProperty('rate', 150)  # Speed of speech (words per minute)
# engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)



# chatStr = ""
# def call():
#   def chat(query):
#       global chatStr
#       chatStr += f"user: Generate a next basic question based on this text{query} programing language\n A.I: "
#       try:
#           response = openai.ChatCompletion.create(
#               model="gpt-3.5-turbo-16k-0613",
#               messages=[{"role": "system", "content": "You: " + chatStr}],
#               temperature=0.7,
#               max_tokens=256,
#               stop=None
#           )
#           response_text = response.choices[0].message['content'].strip()
#           sp.Speak(response_text)
#           print(response_text)
#           chatStr += response_text
#           return response_text
#           if not os.path.exists("Openai"):
#               os.mkdir("Openai")
#           with open(f"Openai/prompt-{random.randint(1, 4565)}.txt", "w") as f:
#               f.write(chatStr)
#       except openai.error.OpenAIError as e:
#           print("OpenAI Error:", e)
#           return "Some Error..."
#       except Exception as e:
#           print("Error:", e)
#           return "Some Error..."



#       # try:
#       #     response = openai.ChatCompletion.create(
#       #         model="gpt-3.5-turbo-16k-0613",
#       #         messages=[{"role": "system", "content": "You: " + tr}],
#       #         temperature=0.7,
#       #         max_tokens=256,
#       #         stop=None
#       #     )
#       #     response_text = response.choices[0].message['content'].strip()
#       #     sp.Speak(response_text)
#       #     print(response_text)
#       #     tr += response_text
#       #     return response_text
#       #     if not os.path.exists("Openai"):
#       #         os.mkdir("Openai")
#       #     with open(f"Openai/prompt-{random.randint(1, 4565)}.txt", "w") as f:
#       #         f.write(chatStr)
#       # except openai.error.OpenAIError as e:
#       #     print("OpenAI Error:", e)
#       #     return "Some Error..."
#       # except Exception as e:
#       #     print("Error:", e)
#       #     return "Some Error..."



#   # def say(text):
#   #     sp.Speak(text)

#   # def takeCommand():
#   #     r = sr.Recognizer()
#   #     with sr.Microphone() as source:
#   #         print("Listening...")
#   #         r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#   #         audio = r.listen(source)
#   #         try:
#   #             query = r.recognize_google(audio, language="en-in")
#   #             print(f"User said: {query}")
#   #             return query
#   #         except Exception as e:
#   #             print("Error:", e)
#   #             return "Some Error Occurred, sorry..."



#   # def say(text):
#   #     sp.Speak(text)

  



#   def say(text):
#     try:
#         print(text)
#         engine.say(text)
#         engine.runAndWait()
#         # sp.Speak(text)
        
#     except Exception as e:
#         print("Error occurred while speaking:", e)

#   def takeCommand():
#       r = sr.Recognizer()
#       with sr.Microphone() as source:
#           # r.pause_threshold = 1
#           audio = r.listen(source)
#           try:
#               query = r.recognize_google(audio, language="en-in")
#               print(f"User said: {query}")
#               return query
#           except Exception as e:
#               return "Some Error Occurred, sorry..."


#   # if __name__ == '__main__':
#   print('pycharm')
#   say("hello, i am jarvin, am your interwier...")
#   say("plese... tell me about yourself.")
#   query = takeCommand()
#   say("Nice to here about you")
#   say("In which technology do you want to give your interview?")
#   i = 1
#   while i < 4:
#       print("Listeing....")
#       query = takeCommand()
#       chat(query)
#       i += 1
#   print("Listeing....")
#   query = takeCommand()
#   say("ok.. thank you...")

# if __name__== '__main__':
#     call()


# #   say("ok.. give me defination of Object oriented porgraming...")
# #   i = 1
# #   while i < 4:
# #       print("Listeing....")
# #       query = takeCommand()
# #       chat(query)
# #       i += 1
# #   print("Listeing....")
# #   query = takeCommand()

# #   say("So, What is Data base...")
# #   i = 1
# #   while i < 4:
# #       print("Listeing....")
# #       query = takeCommand()
# #       chat(query)
# #       i += 1
# #   print("Listeing....")
# #   query = takeCommand()

# #   say("So, What is SQL.")
# #   i = 1
# #   while i < 4:
# #       print("Listeing....")
# #       query = takeCommand()
# #       chat(query)
# #       i += 1
# #   print("Listeing....")
# #   query = takeCommand()

# #   say("Please tell me about Project you made during your college time")
# #   i = 1
# #   while i < 6:
# #       print("Listeing....")
# #       query = takeCommand()
# #       chat(query)
# #       i += 1
# #   print("Listeing....")
# #   query = takeCommand()

# #   say("ok, Have you create any other projects.. please tell me yes or no")
# #   query = takeCommand()
# #   if "yes".lower() in query.lower():
# #       say("Please tell me about Other Projects")
# #       i = 1
# #       while i < 5:
# #           print("Listeing....")
# #           query = takeCommand()
# #           chat(query)
# #           i += 1
# #       print("Listeing....")
# #       query = takeCommand()
# #   else:
# #       say("No.. problem")

# #   say("Please tell me about your hobbies")
# #   i = 1
# #   while i < 3:
# #       print("Listeing....")
# #       query = takeCommand()
# #       chat(query)
# #       i += 1
# #   print("Listeing....")
# #   query = takeCommand()

# #   say("What are your greatest strengths")
# #   i = 1
# #   while i < 3:
# #       print("Listeing....")
# #       query = takeCommand()
# #       chat(query)
# #       i += 1
# #   print("Listeing....")
# #   query = takeCommand()

# #   say("What are your greatest Weaknesses")
# #   i = 1
# #   while i < 3:
# #       print("Listeing....")
# #       query = takeCommand()
# #       chat(query)
# #       i += 1
# #   print("Listeing....")
# #   query = takeCommand()

# #   say("Please tell me about some achievement in your life")
# #   i = 1
# #   while i < 3:
# #       print("Listeing....")
# #       query = takeCommand()
# #       chat(query)
# #       i += 1
# #   print("Listeing....")
# #   query = takeCommand()

# #   say("why do you want to work for our company")
# #   i = 1
# #   while i < 3:
# #       print("Listeing....")
# #       query = takeCommand()
# #       chat(query)
# #       i += 1
# #   print("Listeing....")
# #   query = takeCommand()

















# # -------------------------------------

# # import os
# # import random
# # import speech_recognition as sr
# # import openai
# # import pyttsx3
# # apikey = ""
# # openai.api_key = apikey

# # engine = pyttsx3.init()

# # chatStr = ""
# # def call():
# #     def chat(query):
# #         global chatStr
# #         chatStr += f"user: Generate a next basic question based on this text {query} programming language\n A.I: "
# #         try:
# #             response = openai.ChatCompletion.create(
# #                 model="gpt-3.5-turbo-16k-0613",
# #                 messages=[{"role": "system", "content": "You: " + chatStr}],
# #                 temperature=0.7,
# #                 max_tokens=256,
# #                 stop=None
# #             )
# #             response_text = response.choices[0].message['content'].strip()
# #             say(response_text)
# #             print(response_text)
# #             chatStr += response_text
# #             return response_text
# #             if not os.path.exists("Openai"):
# #                 os.mkdir("Openai")
# #             with open(f"Openai/prompt-{random.randint(1, 4565)}.txt", "w") as f:
# #                 f.write(chatStr)
# #         except openai.error.OpenAIError as e:
# #             print("OpenAI Error:", e)
# #             return "Some Error..."
# #         except Exception as e:
# #             print("Error:", e)
# #             return "Some Error..."

# #     def say(text):
# #         try:
# #             print(text)
# #             engine.say(text)
# #             engine.runAndWait()
# #         except Exception as e:
# #             print("Error occurred while speaking:", e)

# #     def takeCommand():
# #         r = sr.Recognizer()
# #         with sr.Microphone() as source:
# #             audio = r.listen(source)
# #             try:
# #                 query = r.recognize_google(audio, language="en-in")
# #                 print(f"User said: {query}")
# #                 return query
# #             except Exception as e:
# #                 return "Some Error Occurred, sorry..."

# #     if __name__ == '__main__':
# #         print('pycharm')
# #         say("hello, i am jarvin, am your interviewer...")
# #         say("please... tell me about yourself.")
# #         query = takeCommand()
# #         say("Nice to hear about you")
# #         say("In which technology do you want to give your interview?")
# #         i = 1
# #         while i < 4:
# #             print("Listening....")
# #             query = takeCommand()
# #             chat(query)
# #             i += 1
# #         print("Listening....")
# #         query = takeCommand()
# #         say("ok.. thank you...")
