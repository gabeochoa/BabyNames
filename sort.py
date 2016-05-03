import sys

with open('names.txt') as f:
    content = f.readlines()

stripped = []
for name in content:
	stripped.append(name.rstrip())

sor = sorted(stripped)

f = open('myfile','w')
for s in sor:
	f.write(s + "\n")
f.close()