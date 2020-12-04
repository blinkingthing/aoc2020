import math

with open("expenses") as f:
	content = f.readlines()

content = [x.strip() for x in content]

#part1
for a in content:
	for b in content:
		for c in content:
			ab_summed = int(a) + int(b)
			if ab_summed == 2020:
				print(int(a), int(b))
				print(ab_summed)
				print(int(a) * int(b))
				break

#part2
for a in content:
	for b in content:
		for c in content:
			abc_summed = int(a) + int(b) +  int(c)
			if abc_summed == 2020:
				print(int(a), int(b),  int(c))
				print(abc_summed)
				print(int(a) * int(b) *  int(c))
				break