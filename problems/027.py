import time
from lib.primes import is_prime

start = time.time()

def quadratic_expression(n,a,b):
    return n**2 + a*n + b

def get_prime_length(a,b):
    n,consequtive = 0, list()
    while is_prime(quadratic_expression(n,a,b)):
        consequtive.append(n)
        n += 1
    return len(consequtive)

def get_ab(a_limit,b_limit):
    d = dict()
    for a in range(a_limit * -1,a_limit+1):
        for b in range(b_limit+1):
            d[(a,b)] = get_prime_length(a,b)
    return d

sbv = sorted(get_ab(1000,1000).items(), key=lambda kv: kv[1],reverse = True)

print("The product of the coefficients a={} and b={} which the longest sequence of primes are: {}".format(sbv[:1][0][0][0],sbv[:1][0][0][1],sbv[:1][0][0][0]*sbv[:1][0][0][1]))
print("Time: {}".format(time.time()-start))