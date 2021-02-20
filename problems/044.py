import time
start = time.time()

def is_pentagonal(n):
    """
    function to check if the number is pentagonal number or not
    credit: Radius of circle 
    """
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False

pentagonal_numbers = [n for n in range(10000000) if is_pentagonal(n)]
l = [(0,0),1000000000,1000000000] # pair,sum,diff
for j in range(len(pentagonal_numbers)):
    for k in range(len(pentagonal_numbers)):
        if j == k: continue
        else:
            sum_ = pentagonal_numbers[k] + pentagonal_numbers[j]
            diff = abs(pentagonal_numbers[k] - pentagonal_numbers[j])
            #print(is_pentagonal(sum_),is_pentagonal(diff))
            if sum_ <= l[1] and diff <= l[2] and is_pentagonal(sum_) and is_pentagonal(diff):
                l = [(pentagonal_numbers[j],pentagonal_numbers[k]),sum_,diff]
            
print("The pair of pentagonal number {} for which the sum and difference are pentagonal and the difference is minimised is have a difference of {}".format(l[0],l[2]))
print("Time: {}".format(time.time()-start))