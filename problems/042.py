import time
import string
start = time.time()

alpha_dict = {char:idx+1 for idx,char in enumerate(string.ascii_lowercase)}

def generate_triangular_numbers(limit):
    n,tn = 1,list()
    while n <= limit:
        tn.append(int(1/2*n*(n+1)))
        n += 1
    return tn

tn = generate_triangular_numbers(10000)
print("Generated triangular numbers")

c = 0

with open("data/p042_words.txt") as f:
    for line in f:
        line = line.strip().split(",")
        for word in line:
            word = word[1:-1].lower()
            word_val = 0
            for char in word:
                word_val += alpha_dict[char]
            if word_val in tn: c += 1

    

print(c)
print("Time: {}".format(time.time()-start))
