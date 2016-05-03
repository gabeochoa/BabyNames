import sys
from collections import defaultdict
import matplotlib.pyplot as plt

with open('names.txt') as f:
    content = f.readlines()

stripped = []
for name in content:
    stripped.append(name.rstrip())

print (stripped)

start = 1880
end = 2015

namedict = defaultdict(list)

def findYears(name):
    yrs = []
    for i in range(start, end):
        f = open("data/yob" + str(i)+".txt", 'r')
        if name in f.read():
            yrs.append(i)
    return yrs

for name in stripped:
    print(findYears(name))
    break