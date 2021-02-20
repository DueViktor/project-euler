import time
start = time.time()

def sum_of_squares(l):
    s = 0
    for i in l:
        s = s + i**2
    return s

def square_of_sum(l):
    s = sum(l)**2
    return s

n = range(1,101)

print("The difference between the sum of squares of the first 100 natural numbers and the square of the sum is {}".format(square_of_sum(n)-sum_of_squares(n)))
print("Time: {}".format(time.time()-start))