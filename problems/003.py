import time
start = time.time()

def is_prime(number):
    i = 2
    while i != number:
        if number % i == 0:
            return False
        i += 1

    return True

n = 600851475143
p = 2
found = False

while found == False:
    while n % p == 0:
        n /= p
        if is_prime(n) == True:
            found = True
    p += 1

print("The largest prime factor of the number 600851475143 is {}".format(int(n)))
print("Time: {}".format(time.time()-start))
