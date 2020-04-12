import numpy as np
from typing import List

# We compute mean and std of dataset and then return normalized data
def normalize(dataset: List) -> List:
    assert type(dataset) == np.array or type(dataset) == np.ndarray
    return (dataset - np.mean(dataset)) / np.std(dataset)
