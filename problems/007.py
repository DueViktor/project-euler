from lib.primes import is_prime as ip
import time

start = time.time()

i = 3
limit = 10001
prime_number = 1

while prime_number != limit:
    if ip(i):
        prime_number += 1
    i += 2

print("Prime number {} is {}.".format(limit,i-2))
print("Time: {}".format(time.time()-start))