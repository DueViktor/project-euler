""" What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? """

from euler.primes import factors
from collections import defaultdict


prime_factors_list = list()
lens = list()
divisibles = [2, 3, 5, 7, 11, 13, 17, 19]

for divis in divisibles:
    prime_factors = factors(divis)
    print(prime_factors)
#     prime_factors_list.append(prime_factors)
#     lens.append(len(r))
# print(prime_factors_list)
# print(lens)

# d = defaultdict(list)
# index_ = 0
# for i in range(max(lens)):
#     for l in prime_factors_list:
#         try:
#             d[index_].append(l[index_])
#         except BaseException:
#             pass
#     index_ += 1

# result = 1
# print(d)
# for key, val in d.items():
#     print(type(val))
#     print(val)
#     result *= max(val)

# print("Result is: {}".format(result))

"""
http://mathforum.org/library/drmath/view/62527.html

Understanding:
A number divisable by 2,3,4,5,6 could be 2*3*4*5*6 = 720
If divisable by 4 then it must be divisable with 2 aswell so remove that.
3*4*5*6 = 360
Again if something is divisable with 6 it must be with 3 aswell so remove that.
4*5*6 = 120
(2*2) * 5 * (2*3) = 120
(2) * 5 * (2*3) = 60

Take all numbers that it should be divisable with a split into prime factors:
2 =>  2^1
3 =>        3^1
4 =>  2^2
5 =>               5^1
6 =>  2^1   3^1
7 =>
     -----------------
      2^2   3^1    5^1        <--- highest exponents

2^2 * 3^1 * 5^1 = 60
"""
