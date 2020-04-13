import numpy as np
from typing import List
import matplotlib.pyplot as plt

# Sigmoid function implementation
def sigmoid(x: List) -> List:
    return 1 / (1 + np.exp(-x))
