import numpy as np
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

# test data
X, y = make_moons(n_samples=300, shuffle=True, 
                  noise=0.15, random_state=42)

print(y)
#plt.scatter(X[:, 0], X[:, 1], c=y)
#plt.show()

# In this scenario X=[[a1, b1],[a2, b2]] is the feature vector with 2 features and y=[0,1] is the label
# a is feature 1
# b is feature 2
# a1,b1 are the feature for the first sample with a class 0  X[0] = [a1,b1] y[0] = 0
# This is just an example of the test data. I didnt use real values.


class LayerDense:
        self.scale = 0.01 
        # Used to scale down the output of the 
        # Gaussian distriubiotn coming out of np.random.randn
    def __init__(self, n_inputs, n_neurons):
        # n_inputs are the number of inputs coming from 
        # the previous layer
        # n_neurons is number of neurons you want to create
        # for this layer 
        # weights are the starting weights we are creating for the 
        # each feature per neuron 
        # in the  make moon example about we have 2 features
        # so each neuron will have a weight per feature per neuron
        self.weights = self.scale * np.random.randn(n_inputs, n_neurons)
        
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

