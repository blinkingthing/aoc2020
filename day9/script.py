#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("usage: solve.py input.txt")
    exit(1)

p1 = 0
p2 = 0

#conditional preamble length for example vs input
if "example" in sys.argv[1]:
	preamble_length=5 #example
else:
	preamble_length=25 #input

pre_start = 0
pre_end = preamble_length

valid=[]
invalid=[]

with open(sys.argv[1]) as f:
	lines = f.read().splitlines()
	#make sure preamble doesn't exceed length of input
	while pre_end < len(lines):
		#print(lines[pre_start:pre_end])
		test_sums = []
		for i in lines[pre_start:pre_end]:
			for j in lines[pre_start:pre_end]:
				#print("Testing ",i,"+",j,"==",int(i)+int(j),"?")
				#put the sum of i and j in test_sums
				test_sums.append(int(i)+int(j))
				#add the number following the end of the preamble into a valid list if is in our test_sum list
				if int(lines[pre_end]) in test_sums:
					valid.append(lines[pre_end])
				#otherwise put it in the invalid list
				else:
					invalid.append(lines[pre_end])
		#increase the start and end of the preamble by 1 and start it over
		pre_end += 1
		pre_start += 1
	
	#parts 1 answer is the only number that shows up in invalid but not valid (the difference between set(invalid) and set (valid))
	p1 = int(str(set(invalid).difference(set(valid)))[2:-2])

	print("Part 1:",p1)

	p2_lines = []
	for l in lines:
		if int(l) < p1:
			p2_lines.append(int(l))

	#"run" == consecutive set of numbers from input, shortest possible is 2, longest possible is the length of the input
	shortest_run = 2
	longest_run = len(p2_lines)
	matching_run = []

	start = 0 
	#iterate through each line
	for j in range(len(p2_lines)):
		#iterate through each potential run length
		for i in range(shortest_run, len(p2_lines)):
			#make sure your runs stay within the limits of the input
			if start+j+i < len(p2_lines):
				#if the sum of the run = the answer from part 1
				if sum(p2_lines[start+j:start+j+i]) == p1:
					#print("Range start ", start+j," Range end :",start+j+i)
					#print(p2_lines[start+j]," through ",p2_lines[start+i+j]," sum to ",sum(p2_lines[start+j:start+j+i]))
					#print("p2: ",p2_lines[start+j]+p2_lines[start+i+j])
					matching_run=p2_lines[start+j:start+j+i]
					#part 2 = the sum of the smallest and largest int from the run
					p2 = sorted(matching_run)[0]+sorted(matching_run)[-1]

print("Part 2:",p2)