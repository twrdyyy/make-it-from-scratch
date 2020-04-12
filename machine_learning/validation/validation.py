import numpy as np
from typing import List, Tuple


# validation on train dataset, type of dataset is np.array
# we use 3 : 4 ratio as default value
def validate(train_dataset: List, ratio: float = 0.75) -> Tuple:

    "We assert that type of train dataset is np.array because we use slices as indexes"
    assert type(train_dataset) == np.array or type(train_dataset) == np.ndarray

    N = len(train_dataset)

    train, val = (
        train_dataset[0 : int(N * ratio), ...],
        train_dataset[int(N * ratio) :, ...],
    )

    return (train, val)
