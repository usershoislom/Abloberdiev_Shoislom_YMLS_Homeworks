import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    X = np.ones(data.shape[0])
    eigenvalue = 0
    for i in range(num_steps):
        Ax = data @ X
        X = Ax / np.linalg.norm(Ax)
        eigenvalue = X.T @ data @ X
    
    return float(eigenvalue), X
