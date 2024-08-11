import numpy as np
class SampleClass:
    """
    A class representing a pair of numpy arrays.

    Attributes:
        x (np.ndarray): The first numpy array.
        y (np.ndarray): The second numpy array.

    Methods:
        sample_method(self, a: float = 0, b: float = 0)

    Raises:
        TypeError: If x or y is not a numpy array.
        ValueError: If x or y is not a 1D array, or if x and y have different lengths.
    """
    def __init__(self, x: np.ndarray, y: np.ndarray) -> None:
        """
        Initializes the Class instance with x and y numpy arrays.

        Args:
            x (np.ndarray): The first numpy array.
            y (np.ndarray): The second numpy array.

        Raises:
            TypeError: If x or y is not a numpy array.
            ValueError: If x or y is not a 1D array, or if x and y have different lengths.
        """
        # Check if x and y are numpy arrays
        if not isinstance(x, np.ndarray):
            raise TypeError('x must be a numpy array')
        if not isinstance(y, np.ndarray):
            raise TypeError('y must be a numpy array')

        # Check if x and y are 1D arrays
        if x.ndim != 1:
            raise ValueError('x must be a 1D array')
        if y.ndim != 1:
            raise ValueError('y must be a 1D array')

        # Check if x and y have the same length
        if x.shape[0] != y.shape[0]:
            raise ValueError('x and y must have the same number of elements')

        # Assign x and y to instance variables
        self.x = x
        self.y = y

    def sample_method(self, a: float = 0, b: float = 0) -> np.ndarray:
        """
        This method returns a linear combination of the instance's x and y arrays.

        Args:
            a (float, optional): The coefficient for the x array. Defaults to 0.
            b (float, optional): The coefficient for the y array. Defaults to 0.

        Returns:
            np.ndarray: The linear combination of x and y.
        """
        # Calculate the linear combination of x and y
        return self.x * a + self.y * b


