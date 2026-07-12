
import csv
import nltk
#nltk.download('opinion_lexicon')
from nltk.corpus import opinion_lexicon
import numpy as np

positive_words = opinion_lexicon.positive()
negative_words = opinion_lexicon.negative()

num_pos = len(positive_words) #2006 
num_neg = len(negative_words) #4783 

vocabulary = positive_words + negative_words #6789

#for emptying the files
with open("data/training_data.csv","w+") as a:
    pass
with open("data/testing_data.csv","w+") as a:
    pass


with open("data/movie.csv","r",encoding="utf-8-sig") as file:
    reviews = csv.reader(file)
    count = 0
    for review in reviews:

        row = np.zeros(6790) #the first element will indicate a pos {1} or neg {0} review
        row[0] = review[1]
        col = 1
        for word in vocabulary:
            if word in review[0]:
                row[col] = 1
            col += 1

        #eventually put 20k in each file rather than 50 
        if count <= 50:
            with open("data/training_data.csv","a",newline="") as training_data:
                writer = csv.writer(training_data)
                writer.writerow(row)
        elif count <= 100:
            with open("data/testing_data.csv","a",newline="") as testing_data:
                writer = csv.writer(testing_data)
                writer.writerow(row)
        else:
            break
        count += 1

























"""
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

class Cleaning:
    def __init__(self, review):
        self.content = review[0].lower()
        print(self.content)
        self.tokenise()
        print(self.content)
        self.remove_punctuation()
        print(self.content)
        self.remove_stop_words()
        print(self.content)
        self.remove_nouns()
        print(self.content)
        self.stemming()
        print(self.content)

    #the following methods should be completed in the order written 

    def tokenise(self):
        self.content = self.content.split()

    def remove_punctuation(self):
        for word in self.content:
            word = re.sub(r'[^a-zA-Z]', '', word)

    def remove_stop_words(self):
        self.content = [word for word in self.content if word not in stop_words_arr]
        
    def remove_nouns(self):
        tags = pos_tag(self.content)
        self.content = [word for word, tag in tags if tag not in ['NN', 'NNS', 'NNP', 'NNPS']]

    def stemming(self):
        stemmer = PorterStemmer()
        self.content = [stemmer.stem(word) for word in self.content]

    def get_review(self):
        return self.content


stop_words_arr = stopwords.words("english")

with open("data/movie.csv","r",encoding="utf-8-sig") as data:
    reader = csv.reader(data)
    writer = csv.writer(data, delimiter=",")
    counter = 0
    for row in reader:
        cleaning = Cleaning(row)
        cleaned_review = cleaning.get_review()
        print("\ncleaned review:", cleaned_review)
        #if counter <= 20000:
        if counter <= 3:
            with open("data/training_data.csv") as training_data:
                writer.writerow(cleaned_review)
                writer.writerow(row[1])
        #else:
        elif counter <= 6:
            with open("data/testing_data.csv") as testing_data:
                writer.writerow(cleaned_review,row[1])
        counter += 1
"""





