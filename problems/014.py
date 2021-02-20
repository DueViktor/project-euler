"""
Statement 1: n → n/2 (n is even)
Statement 2: n → 3n + 1 (n is odd)
"""
import time

start = time.time()

l = 0

def even(n):
    return n//2

def odd(n):
    return (3*n) + 1

def collatz(n):
    sequence = list()
    while n != 1:
        sequence.append(n)
        if n%2 == 0:
            n = even(n)
        else:
            n = odd(n)
    sequence.append(1)
    return sequence

for i in range(1,1000000):
    tmp = len(collatz(i))
    if l > tmp:
        continue
    else:
        l = tmp
        n = i

print("The number under one million that produces the longest Collatz sequence is {} with a length of: {}".format(n,l))
print("Time: {}".format(time.time()-start))