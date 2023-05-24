import numpy as np
import joblib
import openai
import warnings
import os
from dotenv import load_dotenv
load_dotenv()

warnings.filterwarnings('ignore')

def advan_prompt(age, extraversion, openess, neuroticism, cons,recipe):
    api_key = os.getenv('API_KEY')
    openai.api_key = api_key

    class_model = joblib.load('C:/Users/rupaa_prwuw6w/Documents/GitHub/GDSC-Icebreaker-Hackathon/svm1.joblib')
    output_map = dict(zip([0, 1, 2], ['dependable', 'crazy enthusiastic', 'grumpy']))
    user_input=np.array([8,1,1,4]).reshape((1,4))
    #user_input=np.array([age, extraversion, openess, neuroticism, cons].reshape(1, 4))
    output_pred=output_map[class_model.predict(user_input)[0]]
    prompt = [{'role':'system','content' : 'give me a 150 words detailed response to how a sarcastic '+ neuroticism+' very, '+output_pred+
            ' and very '+cons+' '+openess+' of age '+age+' should talk, act and think.'}]

    gptmod=openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages= prompt)
    response = str(gptmod.choices[-1].message.content)
    return "give me a"+recipe+' recipe with remarks where you are the person described below: "\n'+response+'"'