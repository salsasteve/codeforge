import numpy as np
from activation_functions import sigmoid, relu, tanh, softmax


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

    activation :

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

    def __init__(self, n_inputs: int, n_neurons: int, activation: str = ""):
        self.scale: float = 0.01
        self.weights: np.ndarray = self.scale * np.random.randn(n_inputs, n_neurons)
        self.biases: np.ndarray = np.zeros((1, n_neurons))
        self.output: np.ndarray = np.empty(0)
        self.activation = activation

    def forward(self, inputs: np.ndarray) -> None:
        """
        Compute the forward pass through the dense layer with optional activation.

        Parameters
        ----------
        inputs : array-like of shape (n_samples, n_features)
            The input data to propagate through the layer.

        Returns
        -------
        None
            The result is stored in the `output` attribute of the class.

        Attributes set
        --------------
        output : np.ndarray
            The output of the forward pass, after applying weights, biases, and activation.

        Notes
        -----
        The type of activation applied is determined by the `activation` attribute of the class.
        Supported activations are 'sigmoid', 'relu', and 'tanh'. If none or an unrecognized
        activation is specified, the output is the raw result (linear activation).

        Examples
        --------
        >>> layer = LayerDense(3, 2, activation='relu')
        >>> data = np.array([[0.1, 0.2, 0.3]])
        >>> layer.forward(data)
        >>> print(layer.output)
        array([[...]])
        """
        raw_output = np.dot(inputs, self.weights) + self.biases

        # Apply the activation function, if specified
        if self.activation == "sigmoid":
            self.output = sigmoid(raw_output)
        elif self.activation == "relu":
            self.output = relu(raw_output)
        elif self.activation == "tanh":
            self.output = tanh(raw_output)
        elif self.activation == "softmax":
            self.output = softmax(raw_output)
        else:  # If no activation or unrecognized activation is provided, use linear activation
            self.output = raw_output
