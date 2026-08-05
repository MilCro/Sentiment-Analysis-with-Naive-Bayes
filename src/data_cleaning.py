
#THIS WILL ONLY NEED TO BE RUN ONCE TO PUT THE TRAINING/TEST DATA INTO THE CORRECT FORMAT

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
        if count <= 19999:
            with open("data/training_data.csv","a",newline="") as training_data:
                writer = csv.writer(training_data)
                writer.writerow(row)
        elif count <= 40000:
            with open("data/testing_data.csv","a",newline="") as testing_data:
                writer = csv.writer(testing_data)
                writer.writerow(row)
        else:
            break
        count += 1

