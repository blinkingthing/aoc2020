#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("usage: solve.py input.txt")
    exit(1)

p1 = 0
p2 = 0

with open(sys.argv[1]) as f:
	lines = f.read().splitlines()

	for l in lines:
		print(l)

print("Part 1:",p1)
print("Part 2:",p2)