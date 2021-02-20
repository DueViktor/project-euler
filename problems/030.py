import time
start = time.time()

power = 5
estimated_upper_bound = 355000 # 6*9**5
final_total = 0

for i in range(2,estimated_upper_bound):
    # Skip 0 and 1 since they would always be the sum of it's powers
    total = 0

    for j in str(i):
        total += int(j)**5
    
    if total == i:
        final_total += i

print("The sum of all the numbers that can be written as the sum of fifth powers of their digits is {}.".format(final_total))
print("Time: {}".format(time.time()-start))
