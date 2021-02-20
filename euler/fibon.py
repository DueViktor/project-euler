
from typing import List


def less_than(limit: int) -> List[int]:
    """ return all numbers in the fibonnaci sequence until val is greater or equal the limit """
    sequence = [0, 1]
    while True:
        next_ = sequence[-2] + sequence[-1]
        if next_ >= limit:
            break
        sequence.append(next_)
    return sequence


def n_first(n: int) -> List[int]:
    """ Get the first n fibonaccis """
    sequence = list()
    for i in range(n):
        sequence.append(nth(i))
    return sequence


def nth(n: int) -> int:
    """ find the n'th fibonacci number. Zero indexed """
    if n <= 1:
        return n
    else:
        return nth(n - 1) + nth(n - 2)
