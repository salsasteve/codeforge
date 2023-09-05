import numpy as np


class Loss:

    # Calculates the data and regularization losses
    # given model output and ground truth values
    def calculate(self, output, y):

        # Calculate sample losses
        sample_losses = self.forward(output, y)

        # Calculate mean loss
        data_loss = np.mean(sample_losses)

        # Return loss
        return data_loss



class CategoricalCrossEntropy(Loss):
    """
    Categorical Cross Entropy loss function.

    This loss is commonly used for classification problems. Given true class labels
    and predicted probabilities, it computes the negative log likelihood of the true
    class labels given the predictions.

    Video explanation:  https://www.youtube.com/watch?v=dEXPMQXoiLc&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=7

    Parameters
    ----------
    No specific parameters for this loss function.

    Attributes
    ----------
    None

    Methods
    -------
    forward(ypred: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        Computes the categorical cross entropy loss.
    """

    def forward(self, y_pred: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        """
        Forward pass for the categorical cross entropy loss.

        Parameters
        ----------
        y_pred : np.ndarray
            Predicted probabilities for each class. Shape (n_samples, n_classes).

        y_true : np.ndarray
            True class labels. Can be either:
            1) A 1D array of true class labels, shape (n_samples,)
            2) A 2D array with one-hot encoded classes, shape (n_samples, n_classes).

        Returns
        -------
        np.ndarray
            Computed categorical cross entropy loss for each sample. Shape (n_samples,).

        Notes
        -----
        The loss for sample i is computed as:

        -log(y_pred[i, y_true[i]]) if y_true is 1D
        OR
        -log(sum(y_pred[i, :] * y_true[i, :])) if y_true is 2D

        The values in ypred are clipped to [1e-7, 1-1e-7] to avoid log(0) computations,
        which would result in NaN.
        """
        # Number of samples in the a batch
        samples = len(y_pred)

        # log(0) = undefinded
        # log(1) = 0
        # Clip data to prevent division by 0
        # Clip both sides to not drag mean towards any value
        # Clip y_pred values to prevent taking log(0) and log(1).
        # This is a common practice to avoid NaN values in computations.
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

        # Check the shape of y_true to determine how to extract correct predictions.
        if len(y_true.shape) == 1:
            # For 1D y_true, we extract the predicted probability of the true class for each sample.
            correct_confidences = y_pred_clipped[range(samples), y_true]
        elif len(y_true.shape) == 2:
            # For 2D y_true (one-hot encoded), we sum the products of predictions and true values.
            correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)

        # Losses
        # You want to reduce the loss aka negative_log_likelihoods
        negative_log_likelihoods = -np.log(correct_confidences)

        return negative_log_likelihoods
