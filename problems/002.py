import time
start = time.time()

def sum_even_fibonacci(limit = 4000000):
    
    first = 1
    second = 2
    
    n = [first]

    for i in range(1,10000000):
        if second <= limit:
            n.append(second)
            tmp = second
            second = first + second
            first = tmp
        else:
            break
    
    sum = 0

    for i in n:
        if i % 2 == 0:
            sum += i

    print("The sum of the even numbers are: {}".format(sum))
    print("The Fibonacci Sequence under 4,000,000 are: \n{}".format(n))

    return sum
    
sum_even_fibonacci()

print("Time: {}".format(time.time()-start))