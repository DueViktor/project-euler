import time
from tqdm import tqdm
from lib.primes import is_prime, get_primes

start = time.time()

limit = 1000000

def consecutive_sum(limit):
    primes = get_primes(limit)
    most_number_elements = 0

    for i in tqdm(range(len(primes))):
        new_primes = primes[i:]

        for j in range(len(new_primes)):
            no_elements = len(new_primes[:j])
            prime_sum = sum(new_primes[:j])
            if prime_sum >= limit:
                break
            if no_elements > most_number_elements and is_prime(prime_sum):
                most_number_elements = no_elements
                highest_prime_sum = prime_sum
    return highest_prime_sum, most_number_elements

highest_prime_sum, most_number_elements = consecutive_sum(limit)

print("The prime, below {}, that can be written as the sum of the most consecutive primes is {} and can be written as the sum of {} primes".format(limit,highest_prime_sum,most_number_elements))
print("Time: {}".format(time.time()-start))