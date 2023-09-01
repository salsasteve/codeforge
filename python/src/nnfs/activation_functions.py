import numpy as np
from typing import Union


def sigmoid(x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """
    Compute the sigmoid of x.

    The sigmoid function is defined as:
    sigmoid(x) = 1 / (1 + exp(-x))

    Parameters
    ----------
    x : float or array-like of shape (n_samples,)
        Input value or array.

    Returns
    -------
    float or np.ndarray
        The sigmoid of the input value or array.

    Examples
    --------
    >>> sigmoid(0)
    0.5

    >>> sigmoid(np.array([-1, 0, 1]))
    array([0.26894142, 0.5       , 0.73105858])
    """
    return 1 / (1 + np.exp(-x))


def relu(x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """
    Compute the Rectified Linear Unit (ReLU) of x.

    The ReLU function is defined as:
    relu(x) = max(0, x)

    Parameters
    ----------
    x : float or array-like of shape (n_samples,)
        Input value or array.

    Returns
    -------
    float or np.ndarray
        The ReLU of the input value or array.

    Examples
    --------
    >>> relu(-1)
    0

    >>> relu(np.array([-1, 0, 1]))
    array([0, 0, 1])
    """
    return np.maximum(0, x)


def tanh(x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """
    Compute the hyperbolic tangent of x.

    The tanh function is defined as:
    tanh(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))

    Parameters
    ----------
    x : float or array-like of shape (n_samples,)
        Input value or array.

    Returns
    -------
    float or np.ndarray
        The hyperbolic tangent of the input value or array.

    Examples
    --------
    >>> tanh(0)
    0.0

    >>> tanh(np.array([-1, 0, 1]))
    array([-0.76159416,  0.        ,  0.76159416])
    """
    return np.tanh(x)


def softmax(x: np.ndarray) -> np.ndarray:
    """
    Compute the softmax of x.

    The softmax function is defined as:
    softmax(x)_i = exp(x_i) / sum(exp(x))

    Parameters
    ----------
    x : array-like of shape (n_samples, n_features)
        Input array.

    Returns
    -------
    np.ndarray
        The softmax of the input array, of shape (n_samples, n_features).

    Examples
    --------
    >>> softmax(np.array([[2.0, 1.0, 0.1]]))
    array([[0.65900114, 0.24243297, 0.09856589]])
    """
    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e_x / e_x.sum(axis=-1, keepdims=True)
