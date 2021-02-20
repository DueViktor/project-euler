import time
from tqdm import tqdm
from lib.mixed import factors_of_x, is_abundant

start = time.time()

limit = 28123
n = 12
sieve = [1]*limit

numbers = [i for i in range(limit)]
abund = list()

while n < limit:
    a = factors_of_x(n)
    a.remove(n)
    if is_abundant(a,n):
        abund.append(n)
    n += 1

print("Time spent finding abundant numbers: {}".format(time.time()-start))

abund_sums = list()

for i in tqdm(range(len(abund))):
    for ii in range(len(abund[i:])):
        s = abund[i]+abund[ii]
        if s < limit:
            sieve[s] = 0

sum_ = sum([idx for idx,num in enumerate(sieve) if sieve[idx] == 1])

print("The sum of integers that cannot be written as the sum of two abundant numbers under {} are {}.".format(limit,sum_))
print("Time: {}".format(time.time()-start))