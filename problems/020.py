import time
from lib.mixed import factorial

start = time.time()

val = str(factorial(100))
s = sum([int(s) for s in val])

print("The sum of each digit in the result of 100! is {}.".format(s))
print("Time: {}".format(time.time()-start))