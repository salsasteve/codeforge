import numpy as np
from activation_functions import sigmoid, relu, tanh, softmax


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
    assert all(
        val == 0 for val in outputs
    ), "Negative values not handled correctly in ReLU"

    # Test positive values
    positive_values = np.abs(np.random.randn(1000))
    outputs = relu(positive_values)
    assert all(
        val == original_val for val, original_val in zip(outputs, positive_values)
    ), "Positive values not handled correctly in ReLU"


def test_tanh():
    # Test at some known values
    assert tanh(0) == 0.0
    assert tanh(np.inf) == 1.0
    assert tanh(-np.inf) == -1.0

    # Test output range
    random_values = np.random.randn(1000)
    outputs = tanh(random_values)
    assert all(-1 <= val <= 1 for val in outputs), "Values out of bounds in tanh"


def test_softmax():
    # Known values
    input_array = np.array([[2.0, 1.0, 0.1]])
    expected_output = np.array([[0.65900114, 0.24243297, 0.09856589]])
    np.testing.assert_almost_equal(softmax(input_array), expected_output, decimal=8)

    # Test that sums are close to 1 for random input
    random_input = np.random.randn(10, 5)
    sums = softmax(random_input).sum(axis=1)
    assert all(np.isclose(s, 1) for s in sums), "Not all rows sum to 1 in softmax"
