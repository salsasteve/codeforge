import numpy as np
from LayerDense import LayerDense
from activation_functions import sigmoid, relu, tanh, softmax


def test_initialization_shapes():
    # Create an instance of LayerDense with 5 inputs and 3 neurons
    layer = LayerDense(5, 3)

    # Assert if the weights matrix has shape (5, 3)
    assert layer.weights.shape == (5, 3)

    # Assert if biases have shape (1, 3)
    assert layer.biases.shape == (1, 3)


def test_forward_sigmoid():
    layer = LayerDense(3, 2)
    layer.weights = np.array([[1, -1], [1, -1], [1, -1]])
    layer.biases = np.zeros((1, 2))
    layer.activation = "sigmoid"

    input_data = np.array([[1, 2, 3]])
    layer.forward(input_data)

    expected_output = sigmoid(np.dot(input_data, layer.weights) + layer.biases)
    assert np.allclose(layer.output, expected_output)


def test_forward_relu():
    layer = LayerDense(3, 2)
    layer.weights = np.array([[1, -1], [1, -1], [1, -1]])
    layer.biases = np.zeros((1, 2))
    layer.activation = "relu"

    input_data = np.array([[1, 2, 3]])
    layer.forward(input_data)

    expected_output = relu(np.dot(input_data, layer.weights) + layer.biases)
    assert np.allclose(layer.output, expected_output)


def test_forward_tanh():
    layer = LayerDense(3, 2)
    layer.weights = np.array([[1, -1], [1, -1], [1, -1]])
    layer.biases = np.zeros((1, 2))
    layer.activation = "tanh"

    input_data = np.array([[1, 2, 3]])
    layer.forward(input_data)

    expected_output = tanh(np.dot(input_data, layer.weights) + layer.biases)
    assert np.allclose(layer.output, expected_output)


def test_forward_softmax():
    layer = LayerDense(3, 2)
    layer.weights = np.array([[1, -1], [1, -1], [1, -1]])
    layer.biases = np.zeros((1, 2))
    layer.activation = "softmax"

    input_data = np.array([[1, 2, 3]])
    layer.forward(input_data)

    expected_output = softmax(np.dot(input_data, layer.weights) + layer.biases)
    assert np.allclose(layer.output, expected_output)


def test_forward_linear():
    layer = LayerDense(3, 2)
    layer.weights = np.array([[1, -1], [1, -1], [1, -1]])
    layer.biases = np.zeros((1, 2))
    layer.activation = "linear"  # or any unrecognized string

    input_data = np.array([[1, 2, 3]])
    layer.forward(input_data)

    expected_output = np.dot(input_data, layer.weights) + layer.biases
    assert np.allclose(layer.output, expected_output)
