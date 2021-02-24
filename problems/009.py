"""There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

a<b<c, a**2 + b**2 = c**2
3**2 + 4**2 = 5**2
3+4+5 = 12
a+b+(a**2+b**2) = x, in which c = a**2 + b**2
Example:
"""
import math
from typing import Optional, Tuple


def is_pythagorean_triplet(a: int, b: int, c: int, sum_: int) -> bool:
    return a + b + math.sqrt((a**2 + b**2)) == sum_


max_n = 1000
for a in range(1, max_n + 1):
    for b in range(a, max_n + 1):
        c = int(math.sqrt((a**2 + b**2)))
        if is_pythagorean_triplet(a, b, c, max_n):
            res = a * b * c
            print(res)
            exit()
