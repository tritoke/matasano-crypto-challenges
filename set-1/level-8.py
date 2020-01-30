from math import log, e
import numpy as np


def from_hex(text):  # type: ignore
    if len(text) % 2 != 0:
        text.append("0")
    return bytes([
        int(text[i:i+2], 16)
        for i in range(0, len(text), 2)
    ])


def entropy(labels, base=None):  # type: ignore
    """
    Computes entropy of label distribution.

    from:
    https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python
    """

    n_labels = len(labels)

    if n_labels <= 1:
        return 0

    value, counts = np.unique(labels, return_counts=True)
    probs = counts / n_labels
    n_classes = np.count_nonzero(probs)

    if n_classes <= 1:
        return 0

    ent = float(0)

    # Compute entropy
    base = e if base is None else base
    for i in probs:
        ent -= i * log(i, base)

    return ent


data = open("8.txt", "rb").read().splitlines()

all_blocks = np.array([
    [
        line[i:i+16]
        for i in range(0, len(line), 16)
    ] for line in data
])

answer = b"".join(min(all_blocks, key=lambda x: len(np.unique(x))))

print(answer.decode())
