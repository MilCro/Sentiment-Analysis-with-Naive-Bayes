
import re
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
from nltk.stem import PorterStemmer
nltk.download("punkt")
nltk.download("wordnet")

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
    def __init__(self, og_input):
        self.og_input = og_input
        self.clean_input = ""
    
    def remove_hyperlinks(self, input):
        pass

    def remove_stop_words(self, input):
        pass

    def remove_punctuation(self, input):
        pass

    def tokenise(self, input):
        pass

    def stemming(self, input):
        pass

