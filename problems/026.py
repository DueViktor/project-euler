import time

start = time.time()

def reciprocal_cycle(d):
    # 1/d
    d_ = 2
    while d_ < d:
        print(1/d_)
        d_ += 1
        decimals = str(1/d)
        #print(decimals)
        #print()
        

limit = 10
reciprocal_cycle(limit)    

print("Time: {}".format(time.time()-start))