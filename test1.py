import nltk
from nltk.tokenize import word_tokenize
import random

# Simple Greetings chatbot
GREETING_KEYWORDS = ("hello", "hi", "greetings", "hey")

GREETING_RESPONSES = ["hi hi", "hey", "good day", "oh, its you"]


def greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    sentence = word_tokenize(sentence)
    for word in sentence:
        if word.lower() in GREETING_KEYWORDS:

            return random.choice(GREETING_RESPONSES)
        else:
            return 'no comprehendo'


question = input('say something : ')
answer = greeting(question)
print(answer)