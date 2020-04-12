# Batch sampling

With batch sampling we feed our model not with the whole training dataset but with small samples of it. Often samples (let's call them batches) have size (batch_size) equal to Nth power of 2 e.g. 32, 64.

This is implementation of python generator that takes whole training dataset and yields dataset samples of given size.
