import time
from lib.mixed import decimal_to_binary,is_palindrome
start = time.time()

def double_base_palindrome(limit):
    sum = 0
    for i in range(limit):
        bin_base_two,bin_base_ten = decimal_to_binary(i,2),decimal_to_binary(i,10)
        if is_palindrome(bin_base_two) and is_palindrome(bin_base_ten): 
            sum += i
    return sum

limit = 10

print("The sum of all integers below {} that is binary palindromic in base 2 and 10 are {}".format(limit,double_base_palindrome(limit)))
print("Time: {}".format(time.time()-start))