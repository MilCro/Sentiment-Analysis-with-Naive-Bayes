
import csv

"""
creates a list of words which are positive and a list which is negative
naive bayes will be run using each vocab and the results combined somehow
to produce a result of e.g. 78.5% positive, 30,8% negative, overall mostly positive sentiment (7/10)
"""

class CreateVocabulary:
    def __init__(self, sentiment):
        self.sentiment = sentiment #pos or neg
        if sentiment == "pos":
            self.path = "data/positive_vocabulary.csv"
        else:
            self.path = "data/negative_vocabulary.csv"

    def add_to_vocab(self, path):
        pass

