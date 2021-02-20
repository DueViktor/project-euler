import time

start = time.time()

data = list()

with open("data/p067_triangle.txt") as f:
    for line in f:
        line = line.strip().split(" ")
        line = [int(val) for val in line]
        data.append(line)

for i in range(len(data)-1,-1,-1):
    row = list()

    for j in range(i):
        row.append(max([data[i][j],data[i][j+1]]) + data[i-1][j])

    data[i-1] = row

print("The path with the largest sum result in a sum of {}.".format(data[0][0]))
print("Time: {}".format(time.time()-start))