import time
from lib.primes import is_prime

start = time.time()

string_numbers = [str(i) for i in range(10)]

limit = 1406357289

for i in range(1000000000,10000000000):
    s = str(i)
    if s[1:4] % 2 == 0:
        continue
    if s[2:5] % 3 == 0:
        continue
    if s[3:6] % 5== 0:
        continue
    if s[4:7] % 7 == 0:
        continue
    if s[5:8] % 11 == 0:
        continue
    if s[6:9] % 13 == 0:
        continue
    if s[7:10] % 17 == 0:
        continuel
    

print("Time: {}".format(time.time()-start))