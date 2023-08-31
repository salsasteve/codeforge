import numpy as np
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
from typing import List, Any

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
    """
    Dense (Fully Connected) Layer for a Neural Network.

    This layer implements a fully connected neural network layer,
    with weights and biases for each neuron.

    Parameters
    ----------
    n_inputs : int
        Number of input features (or neurons from the previous layer).

    n_neurons : int
        Number of neurons for this layer.

    Attributes
    ----------
    weights : ndarray of shape (n_inputs, n_neurons)
        The weights matrix of the layer. Initialized with values
        drawn from a Gaussian distribution, scaled by a factor.

    biases : ndarray of shape (1, n_neurons)
        The biases vector for each neuron. Initialized with zeros.

    output : ndarray
        The output of the layer after applying the forward pass.
        Shape varies based on the input shape and number of neurons.

    Notes
    -----
    The forward operation is essentially computing the dot product 
    of inputs and weights, and then adding biases. Conceptually,
    weights help in scaling and biases assist in shifting the 
    values (akin to the `mx+b` linear formula).
    """

    def __init__(self, n_inputs: int, n_neurons: int):
        self.scale: float = 0.01 
        self.weights: np.ndarray = self.scale * np.random.randn(n_inputs, n_neurons)
        self.biases: np.ndarray = np.zeros((1, n_neurons))
        self.output: np.ndarray = np.empty(0)

    def forward(self, inputs: np.ndarray) -> None:
        """
        Compute the forward pass of the dense layer.

        Parameters
        ----------
        inputs : ndarray
            Input data or features. Shape varies based on data and 
            previous layers.

        Returns
        -------
        None
        """
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

