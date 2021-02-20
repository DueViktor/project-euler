"""
Way to slow. Look into this some day...
http://code.jasonbhill.com/sage/project-euler-problem-12/
"""

import time
from lib.mixed import factors_of_x

start = time.time()

tn  = 1
lnn = 1
limit = 500
found = False

def next_triangular_number(ptn,lnn):
    """
    ptn = previous triangular number
    lnn = largest_natural_number to ptn

    returns: new triangular number, new highest natural number
    """
    new_tn = ptn + (lnn + 1)
    return new_tn, lnn + 1

while not found:
    if tn <= limit:
        tn,lnn = next_triangular_number(tn,lnn)
        continue
    divisors = factors_of_x(tn)
    if len(divisors) > limit:
        found = True
    else:
        tn,lnn = next_triangular_number(tn,lnn)

print("The first triangular number with over {} divisors is {}.".format(limit,tn))
print("Time: {}".format(time.time()-start))