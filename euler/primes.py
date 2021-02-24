from typing import List


def highest_factor(n: int) -> int:
    """ credit to : https://stackoverflow.com/a/17311362 """
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return int(n)


def factors(n: int) -> List[int]:
    """ credit to : https://stackoverflow.com/a/22808285 """
    i = 2
    factors = list()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
