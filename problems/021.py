import time
start = time.time()

# Amicable numbers

def proper_divisors(n):
    d = list()
    for i in range(1,int(n/2)+1):
        if n % i == 0:
            d.append(i)
    return sum(d)

def d(n):
    a = n
    b = proper_divisors(a)
    if proper_divisors(b) == a and a != b:
        #print(a,b)
        return a,b
    return 0,0

amicable = list()

c = 1
while c < 10000:
    a,b = d(c)
    amicable.append(a)
    amicable.append(b)
    c += 1

print("The sum of amicable numbers less than 10,000 are {}".format(sum(set(amicable))))
print("Time: {}".format(time.time()-start))