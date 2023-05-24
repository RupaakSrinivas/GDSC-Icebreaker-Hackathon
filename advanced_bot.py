import numpy as np
import joblib, os
import openai,random
import warnings
from dotenv import load_dotenv
warnings.filterwarnings('ignore')

def age(input_age):
    dict_age = dict(zip([1,2,3]
                        , [str(10), str(29), str(85)]))
    return dict_age[input_age]
def extrovert(input_extrovert):
    dict_extrovert = dict(zip([1,2,3],
                              [random.randint(1, 4), random.randint(5, 6), random.randint(7, 10)]))
    return dict_extrovert[input_extrovert]
def openness(input_openness):
    dict_openness = dict(zip([1,2,3],
                             [random.randint(1, 4), random.randint(5, 7), random.randint(8, 10)]))
    return dict_openness[input_openness]
def neuroticism(input_neuro):
    dict_neuro = dict(zip([1,2,3],
                          [random.randint(1, 5), random.randint(6, 7), random.randint(8, 10)]))
    return dict_neuro[input_neuro]
def cons(input_cons):
    dict_cons = dict(zip([1,2], [random.randint(8, 10), random.randint(1, 4)]))
    return dict_cons[input_cons]


def advan_prompt(age, extraversion,openess, neuro, cons1,recipe):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    openai.api_key = api_key
    age=age(age)
    class_model = joblib.load(r"C:\Users\rupaa_prwuw6w\Documents\GitHub\GDSC-Icebreaker-Hackathon\svm1.joblib")
    output_map = dict(zip([0, 1, 2], ['dependable', 'crazy enthusiastic', 'grumpy']))
    user_input=np.array([extrovert(extraversion),openness(openess),neuroticism(neuro),cons(cons1)].reshape(1, 4))
    output_pred=output_map[class_model.predict(user_input)[0]]
    prompt = [{'role':'system','content' : 'give me a 150 words detailed response to how a sarcastic '+ neuro+' very, '+output_pred+
            ' and very '+cons1+' '+openess+' of age '+age+' should talk, act and think.'}]

    gptmod=openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages= prompt)
    response = str(gptmod.choices[-1].message.content)
    return "give me a"+recipe+' recipe with remarks where you are the person described below: "\n'+response+'"'
