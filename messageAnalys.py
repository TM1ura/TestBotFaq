import json
import codecs
import pymorphy2
from thefuzz import fuzz

morph = pymorphy2.MorphAnalyzer()

with codecs.open('data.json', encoding='utf-8', mode='r') as dataFile:
    data = json.load(dataFile)

def analys_question(text):
    text = ''.join(morph.parse(word)[0].normal_form for word in text.split())
    questions =  list(data.keys())
    scores = list()

    for question in questions:
        norm_question = ''.join(morph.parse(word)[0].normal_form for word in question.split())
        scores.append(fuzz.token_sort_ratio(norm_question.lower(), text.lower()))
    answer = data[questions[scores.index(max(scores))]]

    return answer