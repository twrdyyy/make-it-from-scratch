import numpy as np
from typing import List

# Binary function implementation
def binary(x: List) -> List:
    return np.where(x > 0, 1, 0)
