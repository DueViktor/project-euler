import time
start = time.time()

highest = 0

for a in range(100):
    for b in range(100):
        n = a**b
        numbers = [int(char) for char in str(n)]
        if sum(numbers) > highest:
            highest = sum(numbers)


print("The maximum digital sum of a**b where a,b < 100 is {}".format(highest))
print("Time: {}".format(time.time()-start))