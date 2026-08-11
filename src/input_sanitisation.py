
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
from nltk.corpus import opinion_lexicon

"""
Things to do to inputs before analysis:
- convert to lower case
- remove hyperlinks
- remove stop words
- tokenise
- remove punctuation?
- stemming

"""

stop_words_arr = stopwords.words("english")

positive_words = opinion_lexicon.positive()
negative_words = opinion_lexicon.negative()
vocabulary = positive_words + negative_words #6789

class Preparation:
    def __init__(self,input):
        self.input = input
        self.output = np.zeros(6789)

    def get_output(self):
        return self.output

    def prepare(self):
        col = 0
        for word in vocabulary:
            if word in self.input:
                self.output[col] = 1
            col += 1






input = "A polar bear's head is oblong and relatively small compared to body size. The muzzle is elongated with a 'Roman-nosed' (slightly arched) snout. Polar bears have 42 teeth, which they use for catching food and for aggressive behavior. Polar bears use their incisors to shear off pieces of blubber and flesh."

preparing = Preparation(input)
print(preparing.get_output())
ready_to_use_input = preparing.get_output()

