from lib.mixed import is_palindrome
import time
start = time.time()

limit = 10**32
divisible = 10000019
div_by_x_and_palindrome = list()
for i in range(1,limit):
    if i % divisible == 0 and is_palindrome(i):
        div_by_x_and_palindrome.append(i)

print("There are {} palindromes under {} that are divisable with {}".format(len(div_by_x_and_palindrome),limit,divisible))
print("Time: {}".format(time.time()-start))