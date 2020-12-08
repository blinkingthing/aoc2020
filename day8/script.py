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

#runinstructions=[]

def run_code(part,accumulator,instruction_set,runinstructions):
	#run code
	#print("starting accumulator",accumulator)
	i = 0
	while i < len(instruction_set):
		if i in runinstructions:
			#if next instruction has already been ran, return accumulator
			if part == 1:
				print("Hit repeat. accumulator = ",accumulator)
				print("Part 1 : ",accumulator)
			if part == 2:
				print("Hit repeat. accumulator = ",accumulator)
			accumulator = 0
			return 0
		else:
			#add instruction to the list of those that have run
			runinstructions.append(i)
			#print("Step",i," Running",instruction_set[i]["op"],instruction_set[i]["arg"]["operator"],instruction_set[i]["arg"]["int"],"accumulator = ",accumulator)
			if instruction_set[i]["op"] == "nop":
				#no operation
				i +=1
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
				print("accumulator = ",accumulator)
				continue
			if instruction_set[i]["op"] == "jmp":
				#do math on jmper
				if instruction_set[i]["arg"]["operator"] == "+":
					#posi jump
					i += int(instruction_set[i]["arg"]["int"])
				else:
					#negi jump
					i -= int(instruction_set[i]["arg"]["int"])
				continue


with open(sys.argv[1]) as f:
	lines = f.read().splitlines()

	for l in lines:
		instruction["op"] = l.split(" ")[0]
		argument["operator"] = l.split(" ")[1][0]
		argument["int"] = l.split(" ")[1][1:]
		instruction["arg"] = argument.copy()
		instructions.append(instruction.copy())

	jmpmodinstructions = instructions.copy()
	modinstructions = instructions.copy()
	
	#for part 1
	run_code(1,accumulator,instructions,[])

	nops = []
	jmps = []
	print(instructions)
	for i in range(len(instructions)):
		if instructions[i]["op"] == "jmp":
			jmps.append(i)
		if instructions[i]["op"] == "nop":
			nops.append(i)
	print("nop count = ",len(nops))
	print(nops)
	print("jmp count = ",len(jmps))
	print(jmps)

	#bruteforce jumps and no ops and add ones that break to these lists. 
	brokenjmps = []
	brokennops = []

	
	for n in nops:
		#print("Swapping instruction[",n,"]nop with jmp")
		#reset accumulator and modified instrucitons
		accumulator = 0
		jmpmodinstructions = instructions.copy()
		#replace nop with jmp
		jmpmodinstructions[n]['op'] = "jmp"
		if(run_code(2,accumulator,jmpmodinstructions,[])) != 0:
			print("The code ran completely. accumulator = ",accumulator)
		#switch it back
		jmpmodinstructions[n]['op'] = "nop"
	
	for j in jmps:
		#print(modinstructions)
		#print("Swapping instruction[",j,"]jmp with nop")
		#reset accumulator and modified instrucitons
		accumulator = 0
		#print("resetting mod instructions")
		modinstructions = instructions.copy()
		#print("Before: ",modinstructions[j]['op'])
		#replace jmp with nop
		modinstructions[j]['op'] = "nop"
		#print("After: ",modinstructions[j]['op'])
		if(run_code(2,accumulator,modinstructions,[])) != 0:
			print("The code ran completely. accumulator = ",accumulator)
		modinstructions[j]['op'] = "jmp"

	print("Done.")

#0
