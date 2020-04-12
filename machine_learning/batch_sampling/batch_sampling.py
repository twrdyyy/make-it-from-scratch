import numpy as np
from typing import Generator, List

# python generator that yields samples of given dataset e.g.
# dataset = np.zeros((100, 10))
# for batch in sampling(dataset):
#      print(len(batch))
#
# 32
# 32
# 32
# 4
def sampling(dataset: List, batch_size: int = 32) -> Generator:
    assert type(dataset) == np.array or type(dataset) == np.ndarray

    "we go through provided dataset and we cut it into batch_size size samples"
    for batch in range(0, len(dataset), batch_size):
        if batch + 32 < len(dataset):
            yield dataset[batch : batch + batch_size, ...]  # yield sample
        else:
            yield dataset[batch:, ...]  # yield rest of dataset
