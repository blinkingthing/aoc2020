#!/usr/bin/env python3

import sys
import copy
import numpy
from math import gcd

if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

p1 = 0
p2 = 0

def compute_lcm(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm

def busadd(bus,earliest):
	arrival = 0
	while arrival < earliest:
		arrival += bus
		if arrival > earliest:
			return arrival

def tcheck(buses,t):
	tgood = False
	for key,value in buses.items():
		if (t + value) % key == 0:
			tgood = True
			#print("Tgood! - ",t," % ",key," == ",value)
		else:
			tgood = False
			break
	if tgood == True:
		return "Passed"
	
	

with open(sys.argv[1]) as f:
	inputlist = f.read().splitlines()
	earliest = int(inputlist[0])
	buses = inputlist[1].split(",")
	buses2 = copy.deepcopy(buses)
	buses = list(filter(("x").__ne__, buses))
	buses = list(map(int, buses))
	print(earliest)
	print(buses)

	arrivals = []

	for b in buses:
		#print("BUS ID ",b)
		arrivals.append(busadd(b,earliest))
	
	waittime = min(arrivals) - earliest
	#busID with shortest time * wait time
	p1 = buses[arrivals.index(min(arrivals))] * waittime

	busdict = {}
	for b in buses2:
		if b != 'x':
			print("Bus ID :",int(b)," T+",buses2.index(b))
			busdict[int(b)] = buses2.index(b)
	#busdict{busid:T+ departure time}
	#print(busdict)

	busdepartures = []

	for key, value in busdict.items():
		busdepartures.append(value)

	#print(busdepartures)

	#had working solution that was extremely inefficient and would never have actually solved part2. learned solution from @whiplashoo (https://github.com/whiplashoo/advent_of_code_2020/blob/main/day13.py)

	timestamp = 0
	matched_buses = [buses[0]]
	while True:
		#reduce number of timestamps to try by incrementing by lcm of bus ID's who's departure time + timestamp leaves no remainder.
		timestamp += compute_lcm(matched_buses)
		#print("adding ",compute_lcm(matched_buses)," to timestamp")
		#print("checking ",timestamp)
		for i, b in enumerate(buses):
			#check timestamp + bus ID departure time offset remainder
			if (timestamp + busdepartures[i]) % b == 0:
				if b not in matched_buses:
					#print(" no remainder: ",timestamp)
					#print("adding ",b," to matched-buses because ",timestamp," + bus #",b,"'s offset (+T ",busdepartures[i],") / ",b," = 0")
					matched_buses.append(b)
					#print(matched_buses)
		if len(matched_buses) == len(buses):
			break

	#print(timestamp)
	p2 = timestamp


print("Part 1:",p1)
print("Part 2:",p2)