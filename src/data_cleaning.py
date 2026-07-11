
import csv
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords") #list of unimportant words e.g. the
from nltk.stem import PorterStemmer #reduces words to their root form
nltk.download("punkt")
nltk.download("wordnet")
from nltk import pos_tag #tags words with their type e.g. nouns NN

class Cleaning:
    def __init__(self, review):
        self.content = review[0].lower()
    
    #the following methods should be completed in the order written 

    def remove_punctuation(self):
        self.content = re.sub(r'[^a-zA-Z]', '', self.content)

    def tokenise(self):
        self.content = self.content.split()

    def remove_stop_words(self):
        self.content = [word for word in self.content if word not in stop_words_arr]
        
    def remove_nouns(self):
        tags = pos_tag(self.content)
        self.content = [word for word, tag in tags if tag not in ['NN', 'NNS', 'NNP', 'NNPS']]

    def stemming(self):
        stemmer = PorterStemmer()
        self.content = [stemmer.stem(word) for word in self.content]


stop_words_arr = stopwords.words("english")

cleaner = Cleaning()

with open("data/movie.csv","r",encoding="utf-8-sig") as data:
    reader = csv.reader(data)
    writer = csv.writer(data, delimiter=",")
    counter = 0
    for row in reader:
        cleaned_review = cleaner(row)
        #if counter <= 20000:
        if counter <= 3:
            with open("data/training_data.csv") as training_data:
                writer.writerow(cleaned_review,row[1])
        #else:
        elif counter <= 6:
            with open("data/testing_data.csv") as testing_data:
                writer.writerow(cleaned_review,row[1])
        counter += 1






