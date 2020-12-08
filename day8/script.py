#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("usage: solve.py input.txt")
    exit(1)

instruction = {
	"op" : None,
	"arg" : None
}

argument = {
	"operator" : None,
	"int" : None
}
instructions=[]

accumulator = 0

def run_code(part,accumulator,instruction_set,completed_instructions):
	#run code
	i = 0
	while i < len(instruction_set):
		if i in completed_instructions:
			#if next instruction has already been ran, print accumulator
			if part == 1:
				print("Part 1 : ",accumulator)
				return 0
			return 0
		else:
			#add instruction to the list of those that have run
			completed_instructions.append(i)
			#print("Step",i," Running",instruction_set[i]["op"],instruction_set[i]["arg"]["operator"],instruction_set[i]["arg"]["int"],"accumulator = ",accumulator)
			if instruction_set[i]["op"] == "nop":
				#no operation
				i +=1
				#if going to go outside of bounds of list, return the accumulator
				if i + 1 > len(instruction_set):
						return(accumulator)
				continue
			if instruction_set[i]["op"] == "acc":
				#do math on accumulator
				if instruction_set[i]["arg"]["operator"] == "+":
					#addition
					accumulator += int(instruction_set[i]["arg"]["int"])
					i += 1

				else:
					#subtraction
					accumulator -= int(instruction_set[i]["arg"]["int"])
					i += 1
				#if going to go outside of bounds of list, return the accumulator
				if i + 1 > len(instruction_set):
						return(accumulator)
				continue
			if instruction_set[i]["op"] == "jmp":
				#do math on jmper
				if instruction_set[i]["arg"]["operator"] == "+":
					#posi jump
					i += int(instruction_set[i]["arg"]["int"])
					#if going to go outside of bounds of list, return the accumulator
					if i +1 > len(instruction_set):
						return(accumulator)
				else:
					#negi jump
					i -= int(instruction_set[i]["arg"]["int"])
				continue

def nop_jmp_swap(nopsorjmps,modified_instructions,original,swapped):
	for n in nopsorjmps:
		#reset accumulator and modified instrucitons
		accumulator = 0
		modified_instructions = instructions.copy()
		#replace nop with jmp
		modified_instructions[n]['op'] = swapped
		if(run_code(2,accumulator,modified_instructions,[])) != 0:
			print("Part 2: ",run_code(2,accumulator,modified_instructions,[]))
			break
		#switch it back
		modified_instructions[n]['op'] = original


with open(sys.argv[1]) as f:
	lines = f.read().splitlines()

	for l in lines:
		instruction["op"] = l.split(" ")[0]
		argument["operator"] = l.split(" ")[1][0]
		argument["int"] = l.split(" ")[1][1:]
		instruction["arg"] = argument.copy()
		instructions.append(instruction.copy())
	
	#for part 1
	run_code(1,accumulator,instructions,[])

	nops = []
	jmps = []
	
	#build list of nops and jmps
	for i in range(len(instructions)):
		if instructions[i]["op"] == "jmp":
			jmps.append(i)
		if instructions[i]["op"] == "nop":
			nops.append(i)
	
	#swap the jmps and nops until you find the swap that doesn't infinitely loop
	nop_jmp_swap(nops,instructions,"nop","jmp")
	nop_jmp_swap(jmps,instructions,"jmp","nop")

