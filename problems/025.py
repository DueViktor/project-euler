import time

start = time.time()

def fib_seq(digit_limit):
    idx,prev,fib = 2,1,1
    while len(str(fib)) < digit_limit:
        fib,prev = prev + fib,fib
        idx += 1
    return fib,idx

digit_limit = 1000
fib,idx = fib_seq(digit_limit)

print("The first Fibonacci number with {} digits is at index {}".format(digit_limit,idx))
print("Time: {:2f}".format(time.time()-start))