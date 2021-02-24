from euler.primes import gen_primes


lim = 2000000
primes = list()
for i, prime in enumerate(gen_primes()):
    if prime <= lim:
        primes.append(prime)
    else:
        break
print(sum(primes))
