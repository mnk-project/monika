# pylint: disable=E1101

import numpy as np
import pandas as pd
import preprocessor as p
from tensorflow.keras.models import load_model
import joblib
from pathlib import Path as path
from PIL import Image as img
import streamlit as st

# Paths definition
IMG_PATH = path.joinpath(path.cwd(),'images')
ARTIFACTS_PATH = path.joinpath(path.cwd(),'model_artifacts')
DATASETS_PATH = path.joinpath(path.cwd(),'dataset')

# Load artifacts
model = load_model(Path.joinpath(artifacts_path,'model-v1.h5'))
tokenizer_t = joblib.load(Path.joinpath(artifacts_path,'tokenizer_t.pkl'))
vocab = joblib.load(Path.joinpath(artifacts_path,'vocab.pkl'))
df2 = pd.read_csv(Path.joinpath(datasets_path,'responses.csv'))

# Monika functions
def get_pred(model,encoded_input):
    pred = np.argmax(model.predict(encoded_input))
    return pred

def mnk_precausion(df_input,pred):
    words = df_input.questions[0].split()
    if len([w for w in words if w in vocab])==0 :
        pred = 1
    return pred

def get_response(df2,pred):
    upper_bound = df2.groupby('labels').get_group(pred).shape[0]
    r = np.random.randint(0,upper_bound)
    responses = list(df2.groupby('labels').get_group(pred).response)
    return responses[r]

def mnk_response(response,):
    return response

def respond(user_input,is_startup=True):
    df_input = user_input

    df_input = p.remove_stop_words_for_input(p.tokenizer,df_input,'questions')
    encoded_input = p.encode_input_text(tokenizer_t,df_input,'questions')

    pred = get_pred(model,encoded_input)
    pred = bot_precausion(df_input,pred)

    response = get_response(df2,pred)
    response = bot_response(response)

    if is_startup:
        response = "Hi, I'm Monika!"
        is_startup = False
        return response

    else:
        return  response

def get_text():
    input_text = st.text_input("You: ","type here")
    df_input = pd.DataFrame([input_text],columns=['questions'])
    return df_input

st.title("""
Monika
""")

user_input = get_text()
response = respond(user_input)

st.text_area("Monika:", value=response, height=200, max_chars=None, key=None)
