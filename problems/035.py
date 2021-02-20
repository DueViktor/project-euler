import time
from lib.primes import get_primes, is_prime
start = time.time()

def is_circular_prime(n):
    p = 2*str(n)
    for i in range(len(str(n))):
        new_prime = p[i:i+len(str(n))]
        if is_prime(int(new_prime)): 
            continue
        else:
            return False
    return True

primes = get_primes(1000000)

c = 0
for prime in primes:
    if is_circular_prime(prime):
        c += 1
    else:
        continue

print(c)
print("Time: {}".format(time.time()-start))