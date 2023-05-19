import openai
import os
from dotenv import load_dotenv


def get_message(personality, query):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    openai.api_key = api_key
    if personality == "default":
        messages = [ {"role": "assistant", "content": "you are a michelin chef, give a recipe for the dish"} ]
    elif personality == "emotion 1":
        messages = [ {"role": "assistant", "content": "you are a michelin chef and a sass queen regina, give a recipe for the dish"} ]
    elif personality == "emotion 2":
        messages = [ {"role": "assistant", "content": "assume that you are a passive-aggressive Snape from harry potter, give me a novice, the instructions to make the dish,"} ]
    elif personality == "emotion 3":
        messages = [ {"role": "assistant", "content": "you are a michelin chef and an overly happy geet, give a recipe for the dish"} ]
    elif personality == "emotion 4":
        messages = [ {"role": "assistant", "content": "you are a michelin chef and an old and sad chef, give a recipe for the dish"} ]        
    messages.append(
        {"role": "user", "content": query},
    )
    chat = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    reply = str(chat.choices[0].message.content)
    reply = reply.replace("\n","<br>")
    print(reply)
    return str(reply)
