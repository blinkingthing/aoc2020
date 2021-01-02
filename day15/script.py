#!/usr/bin/env python3
#more efficient version stolen from u/hexidon's code on reddit (https://www.reddit.com/r/adventofcode/comments/koooxb/2020_day_15_part_2_python_3_faster_algorithm/)
#I believe I had it solved, but the code was inefficient and would've taken 8 hours to get an answer

import sys
import copy
import numpy

if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

p1 = 0
p2 = 0

#memory game
#most recently spoken number
#has number been spoken
#if spoken before say "AGE" (how many turns since it was previously spoken)
#or if it's a new number, say "0"

# def spoken(number,isstarter):
# 	print(number, "spoken")
# 	if isstarter == True:
# 		print("starter")
# 		return number
# 	else: 
# 		return number


def next_number_efficient(current, nth):
	#default to 0
	next_number = 0
	#print("looking for ",current)
	if current in spoken:
		#this works if current was the last spoken word because it's index minus the current index gives the 0 needed
		#print("FOUND : nextnumber = ",nth, " - ",spoken[current])
		next_number = nth - spoken[current]
		#print("next_number : ",next_number)
	#either way
	#print("setting spoken[",current,"] to ",nth)
	spoken[current] = nth
	return next_number

spoken = {}

with open(sys.argv[1]) as f:
	startingnumbers = f.read().splitlines()
	startingnumbers = startingnumbers[0].split(",")
	startingnumbers = list(map(int, startingnumbers))
	print(startingnumbers)

	lim = 30000000
	lim2 = 2020

	for i in range(len(startingnumbers)):
		spoken[startingnumbers[i]] = i

	#print(spoken)

	current = startingnumbers[-1]
	nth = len(startingnumbers) - 1

	#print("start at ",nth,", with ",current)

	for i in range(nth, lim - 1):
		current = next_number_efficient(current, i)
		if i == lim2-nth+4:
			p1 = str(current)
		

	p2 = str(current)
	#lastsaid = list(spoken.keys())[list(spoken.values()).index(nth-1)]
	#print(lastsaid)

	#while True:
	#	if currentnumber not in spoken:
	#		spoken[currentnumber] = nth
		




	# while True:
	# 	#print("Turn ",nth+1,prevspoken)
	# 	print("Turn ",nth+1)
	# 	if nth < starterlength-1:
	# 		response = spoken(startingnumbers[nth],True)
	# 		prevspoken.append(response)
	# 		#print(response)
	# 	#elif nth > starterlength:
	# 	#	print("last starter")
	# 	#	response = spoken(startingnumbers[nth],True)
	# 	#	prevspoken.append(response)
	# 	elif nth == starterlength-1:
	# 		print("last starter")
	# 		prevspoken.append(startingnumbers[-1])
	# 		prevspoken.append("0")
	# 		response = "0"
	# 	elif nth == 2020-1:
	# 		p1 = prevspoken[-1]
	# 		print(p1)
	# 	elif nth == 30000000-1:
	# 		p2 = prevspoken[-1]
	# 		print(p2)
	# 	else:
	# 		#print("checking ",prevspoken," for ",response)
	# 		if prevspoken.count(response) == 1:
	# 			response = "0"
	# 			prevspoken.append("0")
	# 		elif response in prevspoken:
	# 			for i,p in enumerate(reversed(prevspoken)):
	# 				#print(i,p)
	# 				if i>0 and p == response:
	# 					#print(p, "found ", i," turns ago")
	# 					response = str(i)
	# 					prevspoken.append(response)
	# 					break
	# 		#print(response)
		
	# 	nth += 1
	# print(prevspoken)

	#while True:


print("Part 1:",p1)
print("Part 2:",p2)