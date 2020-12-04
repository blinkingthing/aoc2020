import math

with open("input.txt") as f:
	inpt = f.readlines()

inpt = [x.strip() for x in inpt]
right = 0
trees = 0

lines = iter(inpt)
next(lines)
for line in lines:
	#print(line)
	#print(len(line))
	#31 spaces per line
	if right+3 < len(line):
		right = right + 3;
	else:
		right = (3 - (len(line) - right))
	if line[right] == "#":
		trees = trees + 1
	print("line : ", line, " location : ", right, " trees :", trees)
print("Part 1 : ",trees)

def slope(r,down):
	right = 0
	trees = 0
	for i in range(len(inpt)):
		#skip first 
		if i > down-1:
			#print(line)
			#print(len(line))
			#31 spaces per line
			if right+r < len(inpt[i]):
				right = right + r;
			else:
				right = (r - (len(inpt[i]) - right))
			if inpt[i][right] == "#":
				trees = trees + 1
			#print("line : ", inpt[i], " location : ", right, " trees :", trees)
	return(trees)

def slope2(r, down):
	right =0 
	trees = 0
	for i in range(len(inpt)):
		if i%2 == 0 and i != 0:
			#print(line)
			#print(len(line))
			#31 spaces per line
			if right+r < len(inpt[i]):
				right = right + r;
			else:
				right = (r - (len(inpt[i]) - right))
			if inpt[i][right] == "#":
				trees = trees + 1
	return(trees)



print(slope(3,1) * slope(1,1) * slope(5,1) * slope(7,1) * slope2(1,2))

