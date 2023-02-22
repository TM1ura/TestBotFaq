import json
import codecs
import pymorphy3
from thefuzz import fuzz

# Создание морфологического анализатора
morph = pymorphy3.MorphAnalyzer()

# Открытие файла с FAQ
with codecs.open('data.json', encoding='utf-8', mode='r') as dataFile:
    data = json.load(dataFile)

# Функция обработки вопроса
def analys_question(text):
    # Перевод слов в нормальную форму
    text = ''.join(morph.parse(word)[0].normal_form for word in text.split())
    questions =  list(data.keys())
    scores = list()

    # Сравнение с вопросами из файла
    for question in questions:
        # Перевод слов в нормальную форму
        norm_question = ''.join(morph.parse(word)[0].normal_form for word in question.split())

        # Сравнение вопросов
        scores.append(fuzz.token_sort_ratio(norm_question.lower(), text.lower()))

    answer = data[questions[scores.index(max(scores))]]
    score = max(scores)
    question = questions[scores.index(max(scores))]

    return question, answer, score