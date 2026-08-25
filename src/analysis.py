
import numpy as np
from input_sanitisation import *

training_data = np.loadtxt(open("data/training_data.csv"), delimiter=",").astype(int)
#print("Shape of the training data set:", training_data.shape)

class Analysis:
    def __init__(self, k, training_data):
        self.k = k
        self.log_class_priors = np.array([0.0,0.0])
        self.log_class_conditional_likelihoods = np.zeros(shape=(2,6789)) 
        self.training_data = training_data

    def estimate_log_class_priors(self, data):
        numPos = 0 #9976
        numNeg = 0 #10024
        for review in data:
            if review[0] == 1:
                numPos += 1
            else:
                numNeg += 1
        logPos = np.log10(numPos/20000) 
        logNeg = np.log10(numNeg/20000)
        self.log_class_priors = np.array([logNeg,logPos])

    def estimate_log_class_conditional_likelihoods(self,data):
        k = 6790
        alpha = 1.0

        #split into pos and neg
        posData = np.zeros(shape=(9976,6790)) 
        negData = np.zeros(shape=(10024,6790))
        posIndex = 0
        negIndex = 0
        for d in data:
            if d[0] == 1:
                posData[posIndex] = d
                posIndex += 1
            else:
                negData[negIndex] = d
                negIndex += 1

        posWordCount = np.count_nonzero(posData == 1, axis = 0)
        negWordCount = np.count_nonzero(negData == 1, axis = 0)
        totalPosWords = 0
        totalNegWords = 0
        for i in range(1,6789):
            totalPosWords += posWordCount[i]
            totalNegWords += negWordCount[i]

        posWordCount = posWordCount[1:]
        negWordCount = negWordCount[1:]

        posTheta = np.zeros(shape=(6789))
        negTheta = np.zeros(shape=(6789))
        index = 0
        for n0 in posWordCount:
            posTheta[index] = np.log10((n0 + alpha)/(totalPosWords + (alpha*k)))
            index += 1

        index = 0
        for n1 in negWordCount:
            negTheta[index] = np.log10((n1 + alpha)/(totalNegWords + (alpha*k)))
            index += 1

        theta = np.zeros(shape=(2,6789))
        theta[0] = posTheta
        theta[1] = negTheta
        self.log_class_conditional_likelihoods = theta

    def train(self,data):
        self.estimate_log_class_priors(data)
        self.estimate_log_class_conditional_likelihoods(data)
    
    def predict(self, data):
        class_predictions = np.zeros(shape=(len(data)))
        index = 0
        for d in data:
            posCounter = 0
            negCounter = 0
            for x in range(6789):
                if d[x] == 1:
                    posCounter += self.log_class_conditional_likelihoods[0,x]
                    negCounter += self.log_class_conditional_likelihoods[1,x]

            if (self.log_class_priors[0] + posCounter) > (self.log_class_priors[1] + negCounter):
                class_predictions[index] = 1
            else:
                class_predictions[index] = 0
            index += 1
        return class_predictions

    def predict_one_data(self, data):
        posCounter = 0
        negCounter = 0
        for x in range(6789):
            if data[x] == 1:
                posCounter += self.log_class_conditional_likelihoods[0,x]
                negCounter += self.log_class_conditional_likelihoods[1,x]

        if (self.log_class_priors[0] + posCounter) > (self.log_class_priors[1] + negCounter):
            class_prediction = 1
        else:
            class_prediction = 0
        
        return [class_prediction,posCounter,negCounter]

def create_classifier():
    training_data = np.loadtxt(open("data/training_data.csv"), delimiter=",").astype(int)
    classifier = Analysis(k=1, training_data=training_data)
    classifier.train(training_data)
    return classifier

classifier = create_classifier()

user_input = input("Enter text: ").lower()
preparing = Preparation(user_input)
clean_input = preparing.get_output()
print(np.count_nonzero(clean_input))

output = classifier.predict_one_data(clean_input)

print(output)




""" #84.4% accurate on training data
testing_reviews = np.loadtxt(open("data/testing_data.csv"), delimiter=",").astype(int)
test_data = testing_reviews[:, 1:]
test_labels = testing_reviews[:, 0]

predictions = classifier.predict(test_data)
accuracy = np.count_nonzero(predictions == test_labels)/test_labels.shape[0] 
print(f"Accuracy on test data is: {accuracy}")
"""

