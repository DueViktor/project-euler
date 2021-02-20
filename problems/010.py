import time
import numpy as np
from lib.primes import is_prime

start = time.time()

lim = 2000000

def primes(limit):
	"""
	A generator which yield primes until limit
	"""
	yield 2
	cur = 3
	while cur < limit:
		if is_prime(cur):
			yield cur
		cur += 2

print("Sum of primes until {} is {}".format(lim,sum(primes(lim))))
print("Time: {}".format(time.time()-start))