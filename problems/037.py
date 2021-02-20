import time
from tqdm import tqdm
from lib.primes import get_primes,is_prime

start = time.time()

def truncatable_from_left(prime):
    prime = str(prime)
    for i in range(len(prime)):
        if is_prime(int(prime[i:])):
            continue
        else:
            return False
    return True

def truncatable_from_right(prime):
    prime = str(prime)
    for i in range(len(prime),0,-1):
        if is_prime(int(prime[:i])):
            continue
        else:
            return False
    return True


primes = get_primes(5000000)
truncatable_primes = list()

for prime in tqdm(primes):
    if prime < 8: continue
    else:
        if truncatable_from_left(prime) and truncatable_from_right(prime):
            truncatable_primes.append(prime)

print("The sum of the only eleven truncatable primes are {}".format(sum(truncatable_primes)))
print("Time: {}".format(time.time()-start))