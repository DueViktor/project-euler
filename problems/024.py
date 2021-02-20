# With help from https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

import time
start = time.time()

def next_lexicographic_perm(l):
    
    i = len(l)-1

    while 0 < i and arr[i-1] >= arr[i]: # This while find non-increasing suffix. 
        
        i -= 1

    if i <= 0: return False # There are no next permutation.
        
    j = len(l) - 1
    while l[j] <= l[i - 1]:  # Get index of swap. Left of suffix.
        j -= 1

    l[i - 1], l[j] = l[j], l[i - 1] # Swap index
	
    l[i : ] = l[len(l) - 1 : i - 1 : -1] # Reverse suffix
    return l
    
arr = [0,1,2,3,4,5,6,7,8,9]
limit = 1000000

c = 1
while c < limit:
    arr = next_lexicographic_perm(arr)
    c += 1

answer = str1 = ''.join(str(i) for i in arr)

print("The millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 are {}".format(answer))
print("Time: {}".format(time.time()-start))