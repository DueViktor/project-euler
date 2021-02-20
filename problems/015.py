import time
start = time.time()
"""
The grid size must be even numbers. 0 for right and 1 for down.
Arrangement of binary bits (Results https://math.stackexchange.com/questions/286437/arrangement-of-binary-bits) boils down to this formula:
n!/m!**2
"""

grid_size = 20

def factorial(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s

def permu_of_binary_bits(grid_size):
    n = grid_size*2
    m = grid_size
    nom = factorial(n)
    denom = factorial(m)**2
    return int(nom/denom)
    
print("Number of permutations of bits in a ({}x{}) grid are {}".format(grid_size,grid_size,permu_of_binary_bits(grid_size)))
print("Time: {}".format(time.time()-start))