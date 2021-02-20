import time

from lib.primes import read_primes
from lib.primes import is_prime
from collections import defaultdict

start = time.time()

def prime_factors(n):
    """
    Found online
    """
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

prime_factors_list = list()
lens = list()

for i in range(2,21):
    r = prime_factors(i)
    prime_factors_list.append(r)
    lens.append(len(r))
print(prime_factors_list)
print(lens)

d = defaultdict(list)
index_ = 0
for i in range(max(lens)):
    for l in prime_factors_list:
        try:
            d[index_].append(l[index_])
        except:
            pass
    index_ += 1    

result = 1
print(d)
for key,val in d.items():
    print(type(val))
    print(val)
    result *= max(val)

print("Result is: {}".format(result))
print("Time: {:2f}".format(time.time()-start))

"""
http://mathforum.org/library/drmath/view/62527.html

Understanding:
A number divisable by 2,3,4,5,6 could be 2*3*4*5*6 = 720
If divisable by 4 then it must be divisable with 2 aswell so remove that.
3*4*5*6 = 360
Again if something is divisable with 6 it must be with 3 aswell so remove that.
4*5*6 = 120
(2*2) * 5 * (2*3) = 120
(2) * 5 * (2*3) = 60

Take all numbers that it should be divisable with a split into prime factors:
2 =>  2^1
3 =>        3^1
4 =>  2^2
5 =>               5^1
6 =>  2^1   3^1
7 =>        
     -----------------
      2^2   3^1    5^1        <--- highest exponents

2^2 * 3^1 * 5^1 = 60
"""