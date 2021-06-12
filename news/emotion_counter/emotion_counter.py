import pandas as pd
from . import data_preparation
import os
from config.settings import BASE_DIR

data = pd.read_csv(os.path.join(BASE_DIR, 'news', 'emotion_counter', 'emotions_without_duplicates.csv'))

def list_of_synonyms(text):
    remove_special_characters_except_commas = text.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
    list_of_words = remove_special_characters_except_commas.split(",")
    return list(list_of_words)


def emotion_counter(text):
    list_of_important_tokens = data_preparation.prepared_data(text)
    list_of_lists = data['synonyms'].tolist()
    list_of_emotions = data['name'].tolist()
    list_of_list_of_synonyms = [list_of_synonyms(value) for value in list_of_lists]
    emotion_score = [0]*len(data)
    for token in list_of_important_tokens:
        for i in range(0, len(data)):
            if token in list_of_list_of_synonyms[i]:
                emotion_score[i] = emotion_score[i] + 1
    dictinary_of_all_score = {list_of_emotions[i]:emotion_score[i] for i in range(0, len(data)) if emotion_score[i] != 0}
    return dictinary_of_all_score
