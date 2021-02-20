import time
start = time.time()

p_1 = 100
p_2 = 100
palindrome = list()

for i in range(999,99,-1):
    for ii in range(999,99,-1):
        r = str(i * ii)
        k = str()
        for x in range(len(r) -1,-1,-1):
            k += r[x]
        if k == r:
            palindrome.append(int(r))

print("The largest palindrome made from the product of two 3-digit numbers are {}".format(max(palindrome)))
print("Time: {}".format(time.time()-start))