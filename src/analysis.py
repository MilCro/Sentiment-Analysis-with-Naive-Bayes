
import numpy as np

training_data = np.loadtxt(open("data/training_data.csv"), delimiter=",").astype(int)
print("Shape of the training data set:", training_data.shape)
#print(training_data)


class Analysis:
    def __init__(self, k, training_data):
        self.k = k
        self.log_class_priors = np.array([0.0,0.0])
        self.log_class_conditional_likelihoods = np.zeros(shape=(2,55)) #will be a lot more than 55
        self.training_data = training_data

    def estimate_log_class_priors(self,data):
        pass

    def estimate_log_class_conditional_likelihoods(self,data):
        pass

    def train(self,data):
        self.estimate_log_class_priors(data)
        self.estimate_log_class_conditional_likelihoods(data)
    
    def predict(self, data):
        pass


def create_classifier():
    training_data = np.loadtxt(open("data/training_data.csv"), delimiter=",").astype(int)
    classifier = Analysis(k=1, training_data=training_data)
    classifier.train(training_data)
    return classifier

classifier = create_classifier()

