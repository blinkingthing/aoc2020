#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("usage: solve.py input.txt")
    exit(1)

with open(sys.argv[1]) as f:
	lines = f.read().splitlines()
	answers = []
	answer = ""
	for line in lines:
		if line != '':
			answer = answer + line
			if line == lines[-1]:
				#if last line
				answer = answer + line
				answers.append(answer)
				answer = ""
		else:
			answers.append(answer)
			answer = ""


	#print(answers)

	count = 0
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	for a in answers:
		a2 = list(set(a))
		for z in alphabet:
			if z in a2:
				count += 1
	print("Part 1: ",count)

	#reset count
	count = 0
	singlecount = 0
	answers = []
	answer = {
		"size" : 0,
		"answer" : ""
	}
	groupsize = 0
	for line in lines:
		if line != '':
			answer["answer"] = answer["answer"] + line
			groupsize += 1
			if line == lines[-1]:
				answer["answer"] = answer["answer"] + line
				answers.append(answer.copy())
				#reset
				groupsize = 0
				answer["answer"] = answer["answer"]
				answer["answer"] = ""
				answer["size"] = 0

		else:
			answers.append(answer.copy())
			#reset
			groupsize = 0
			answer["answer"] = answer["answer"]
			answer["answer"] = ""
			answer["size"] = 0
			
		answer["size"] = groupsize

	for a in answers:
		if a["size"] == 1:
			for z in alphabet:
				if z in a["answer"]:
					count += 1
				
		elif a["size"] > 1:
			for z in alphabet:
				#if current answerset has occurense of (z) that match the size of the group that answered, increase yes count by 1
				if a["answer"].count(z) == a["size"]:
					count += 1

	print("Part 2: ",count)
