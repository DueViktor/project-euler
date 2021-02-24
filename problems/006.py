""" Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. """


from typing import List


def sum_of_squares(l: range) -> float:
    # square each item in l
    s = 0
    for i in l:
        s = s + i**2
    return s


N: range = range(1, 101)
res = (sum(N)**2) - sum_of_squares(N)
print(res)
