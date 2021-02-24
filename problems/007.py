""" What is the 10 001st prime number? """
from euler.primes import gen_primes

limit: int = 10001

for i, prime in enumerate(gen_primes()):
    if i > limit - 1:
        print(prime)
        break
