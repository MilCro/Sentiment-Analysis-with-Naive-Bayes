
import csv
import numpy as np
import re
import nltk
nltk.download("averaged_perceptron_tagger_eng") #list of words tagged with types
from nltk.corpus import stopwords
nltk.download("stopwords") #list of unimportant words e.g. the
from nltk.stem import PorterStemmer #reduces words to their root form
nltk.download("punkt")
nltk.download("wordnet")
from nltk import pos_tag #tags words with their type e.g. nouns NN

"""
Things to do to inputs before analysis:
- convert to lower case
- remove hyperlinks
- remove stop words
- tokenise
- remove punctuation?
- stemming

"""

class Preparation:
    def __init__(self, input):
        self.input = input.lower()

        self.tokenise() #remove hyperlinks before or after this
        self.remove_punctuation()
        self.remove_stop_words()
        self.stemming()


    def get_input(self):
        return self.input
    
    def remove_hyperlinks(self):
        pass

    def remove_stop_words(self):
        self.input = [word for word in self.input if word not in stop_words_arr]

    def remove_punctuation(self): #not sure if i should use this
        for word in self.input:
            word = re.sub(r'[^a-zA-Z]', '', word)

    def tokenise(self):
        self.input = self.input.split()

    def stemming(self, input):
        stemmer = PorterStemmer()
        self.input = [stemmer.stem(word) for word in self.input]



stop_words_arr = stopwords.words("english")


