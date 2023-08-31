import numpy as np

from activation_functions import sigmoid, relu, tanh


def test_sigmoid():
    # Test at some known values
    assert sigmoid(0) == 0.5
    assert sigmoid(np.inf) == 1.0
    assert sigmoid(-np.inf) == 0.0
    
    # Test output range
    random_values = np.random.randn(1000)
    outputs = sigmoid(random_values)
    assert all(0 <= val <= 1 for val in outputs), "Values out of bounds in sigmoid"


def test_relu():
    # Test at some known values
    assert relu(0) == 0
    assert relu(5) == 5
    assert relu(-5) == 0
    
    # Test negative values
    negative_values = -np.abs(np.random.randn(1000))
    outputs = relu(negative_values)
    assert all(val == 0 for val in outputs), "Negative values not handled correctly in ReLU"

    # Test positive values
    positive_values = np.abs(np.random.randn(1000))
    outputs = relu(positive_values)
    assert all(val == original_val for val, original_val in zip(outputs, positive_values)), "Positive values not handled correctly in ReLU"


def test_tanh():
    # Test at some known values
    assert tanh(0) == 0.0
    assert tanh(np.inf) == 1.0
    assert tanh(-np.inf) == -1.0

    # Test output range
    random_values = np.random.randn(1000)
    outputs = tanh(random_values)
    assert all(-1 <= val <= 1 for val in outputs), "Values out of bounds in tanh"
