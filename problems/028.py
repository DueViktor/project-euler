import time
import numpy as np

start = time.time()

def sum_diagonals(matrix):
    raise NotImplementedError

shape = (3,3)

m = np.zeros(shape) # Init matrix
center = (shape[0]//2,shape[1]//2) # Get center

reached_end,c,index = False,1,center
while not reached_end:
    if index == center:
        m[index] = c
        c += 1
        index = (index[0],index[1]+1)
        
    
print("Time: {}".format(time.time()-start))