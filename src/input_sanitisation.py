
#import csv
import numpy as np
import re
from string import punctuation
import nltk
#nltk.download("averaged_perceptron_tagger_eng") #list of words tagged with types
from nltk.corpus import stopwords
#nltk.download("stopwords") #list of unimportant words e.g. the
from nltk.stem import PorterStemmer #reduces words to their root form
#nltk.download("punkt")
#nltk.download("wordnet")

"""
Things to do to inputs before analysis:
- convert to lower case
- remove hyperlinks
- remove stop words
- tokenise
- remove punctuation?
- stemming

"""

class Sanitisation:
    def __init__(self, input):
        self.input = input.lower()

        self.tokenise()
        self.remove_stop_words()



    def get_input(self):
        return self.input

    def tokenise(self):
        r = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))
        self.input = r.split(self.input)

    def remove_stop_words(self):
        self.input = [word for word in self.input if word not in stop_words_arr]

stop_words_arr = stopwords.words("english")

class Preparation:
    def __init__(self,input):
        self.input = self.input
        self.length = len(self.input)
        self.output = np.zeros(self.length)

