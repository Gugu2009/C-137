#Biblioteca de pré-processamento de dados de texto
import nltk

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

import json
import pickle
import numpy as np

words = []
classes = []
word_tags_list = []
ignore_words = ["'?'", "'!'", "','", "'.'", "'s'", "'m'"]
train_data_file = open('intents.json').read()
intents = json.load(train_data_file)

#função para anexar palavras-tronco
def get_stem_words(words, ignore_words):
        stem_words = [],
        for word in words:
                if word not in ignore_words:
                        w = stemmer.stem(word.lower())
                        stem_words.append(w)
        return stem_words
def create_bot_corpus(words, classes, word_tags_list, ignore_words):
        for intent in ['intents']:

        # Adicione todas as palavras dos padrões à lista
                for pattern in intent['patterns']:
                        pattern_word = nltk.word_tokenize(pattern)
                        words.extend(pattern_word)
                        word_tags_list.append((pattern_word, intent['tag']))


        # Adicione todas as tags à lista classes
                if intent [ 'tag'] not in classes:
                        classes.append(intent['tag'])
                        stem_words = get_stem_words(words, ignore_words)

        print(stem_words)
        print(word_tags_list)
        print(classes)
#Crie o corpus de palavras para o chatbot
