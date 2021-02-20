import time

start = time.time()

val = str(2**(1000))
l = [int(s) for s in val]

print("The sum of each digit in the result of 2 to the power of 1000 is {}.".format(sum(l)))
print("Time: {}".format(time.time()-start))