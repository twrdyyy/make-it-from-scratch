import numpy as np
import matplotlib.pyplot as plt
from typing import List

# ReLU implementation
def relu(x: List or float) -> List or float:
    return np.maximum(0, x)


# Leaky ReLU implementation
def lrelu(x: List or float) -> List or float:
    return np.where(x > 0, x, x * 0.01)


# Parametric ReLU implementation
def prelu(x: float, alpha: float = 0.05):
    return np.where(x > 0, x, x * alpha)
