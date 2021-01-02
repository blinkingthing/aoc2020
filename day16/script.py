#!/usr/bin/env python3

import sys
import numpy

if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

p1 = 0
p2 = 0

fields={}
yourticket = []
nearbytickets = []

with open(sys.argv[1]) as f:
	inputlist = f.read().splitlines()
	for i,line in enumerate(inputlist):
		#skip blanks
		if len(line) > 0:
			if "your ticket" in line:
				#print(inputlist[i+1])
				yours = inputlist[i+1].split(",")
				yourticket = list(map(int,yours))
				for l in range(i+2,len(inputlist)):
					if len(inputlist[l]) > 0 and inputlist[l][0] != "n":
						#print(inputlist[l])
						nearby = inputlist[l].split(",")
						nearbysingle = list(map(int, nearby))
						for n in nearbysingle:
							nearbytickets.append(n)
				break
			#print(line.split(":")[0],line.split(":")[1][1:])
			fields[line.split(":")[0]] = line.split(":")[1][1:]
			#fields[line.split(" ")[0][:-1]] = line[len(line.split(" ")[0])+1:]

	print("your ticket:",yourticket)
	print("nearby tickets:",nearbytickets)
	print(fields)

	all_fields = []
	all_tickets = yourticket + nearbytickets
	for key,value in fields.items():
		#print(value.split(" ")[0].split("-"))
		one = list(range(int(value.split(" ")[0].split("-")[0]),int(value.split(" ")[0].split("-")[1])+1))
		#print(value.split(" ")[2])
		two = list(range(int(value.split(" ")[2].split("-")[0]),int(value.split(" ")[2].split("-")[1])+1))
		fields[key] = one + two
		all_fields += fields[key]
		#print(value)
	print(fields)

	all_tickets = list(set(all_tickets))
	all_fields = list(set(all_fields))
	
	print("part 1 tickets : ",all_tickets)
	print("part 1 valid fields : ",all_fields)
	# differences = numpy.setdiff1d(all_tickets,all_fields)
	# print("part 1 differences : ",differences)
	# sumofdifferences = 0
	# for d in differences:
	# 	sumofdifferences += d
	# p1 = sumofdifferences
	diff =[]
	


print("Part 1:",p1)
print("Part 2:",p2)