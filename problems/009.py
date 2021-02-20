import time, math
start = time.time()

"""
a<b<c, a**2 + b**2 = c**2
3**2 + 4**2 = 5**2
3+4+5 = 12
a+b+(a**2+b**2) = x, in which c = a**2 + b**2
Example: 
"""

def pythagorean_triplet(maxi):
	for a in range(1,maxi+1):
		for b in range(a,maxi+1):
			if a+b+math.sqrt((a**2+b**2)) == maxi:
				c = int(math.sqrt((a**2+b**2)))
				print("a = {}, b = {}, c = {}, a+b+c = {}".format(a,b,c,a+b+c))
				return a,b,c
	return False
	
a,b,c = pythagorean_triplet(1000)
print("The product of a*b*c is {}".format(a*b*c))
print("Time: {}".format(time.time()-start))