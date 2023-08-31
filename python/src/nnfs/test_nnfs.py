import numpy as np
from nnfs import LayerDense

def test_initialization_shapes():
    # Create an instance of LayerDense with 5 inputs and 3 neurons
    layer = LayerDense(5, 3)
    
    # Assert if the weights matrix has shape (5, 3)
    assert layer.weights.shape == (5, 3)
    
    # Assert if biases have shape (1, 3)
    assert layer.biases.shape == (1, 3)

def test_foward_transformation():
    # Create an instance of LayerDense with 5 inputs and 3 neurons
    layer = LayerDense(5, 3)
    
    # Mock input data of shape (10, 5) (i.e., 10 samples with 5 features each)
    inputs = np.random.rand(10, 5)
    
    layer.forward(inputs)
    
    # The output should have shape (10, 3) since there are 10 samples and 3 neurons
    assert layer.output.shape == (10, 3)

    # To check the correctness of the transformation, let's manually compute expected output
    expected_output = np.dot(inputs, layer.weights) + layer.biases
    assert np.allclose(layer.output, expected_output), "The transformation is incorrect."
