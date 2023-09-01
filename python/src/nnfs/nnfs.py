import numpy as np
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
from typing import List, Any
from activation_functions import sigmoid, relu, tanh, softmax

# test data
X, y = make_moons(n_samples=300, shuffle=True, noise=0.15, random_state=42)

print(y)
# plt.scatter(X[:, 0], X[:, 1], c=y)
# plt.show()

# In this scenario X=[[a1, b1],[a2, b2]] is the feature vector with 2 features and y=[0,1] is the label
# a is feature 1
# b is feature 2
# a1,b1 are the feature for the first sample with a class 0  X[0] = [a1,b1] y[0] = 0
# This is just an example of the test data. I didnt use real values.
