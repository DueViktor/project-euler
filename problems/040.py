import time
start = time.time()

def generate_int_list(limit):
    decimals = str()
    i = 1
    while len(decimals) < limit:
        decimals += str(i)
        i += 1
    return [int(char) for char in decimals]

l = generate_int_list(1000000)
d1,d10,d100,d1000,d10000,d100000,d1000000 = l[1-1],l[10-1],l[100-1],l[1000-1],l[10000-1],l[100000-1],l[1000000-1]
sum_ = d1*d10*d100*d1000*d10000*d100000*d1000000

print("d1: {}\nd10: {}\nd100: {}\nd1000: {}\nd10000: {}\nd100000: {}\nd1000000: {}\nThe product are {}".format(d1,d10,d100,d1000,d10000,d100000,d1000000,sum_))
print("Time: {}".format(time.time()-start))