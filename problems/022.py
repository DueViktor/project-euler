import string
import time

start = time.time()

def init():
    with open("data/p022_names.txt") as f:
        names = sorted([line.split(",") for line in f if line][0])

    pos = 1
    letters = dict()

    for letter in str(string.ascii_lowercase):
        letters[letter] = pos
        pos += 1
    return names,letters

names,letters = init()

pos,name_scores_total = 1,0

for name in names:
    name = name[1:-1]
    word_score = 0
    for char in name.lower():
        word_score += letters[char]
    name_scores_total += word_score * pos
    pos += 1

print("The total name score is {}".format(name_scores_total))
print("Time: {}".format(time.time()-start))