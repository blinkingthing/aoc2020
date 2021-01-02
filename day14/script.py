#!/usr/bin/env python3

import sys
import copy
import numpy
import itertools

# Function to convert Decimal number  
# to Binary number  
def decimalToBinary(n):  
    return bin(n).replace("0b", "")  

if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

p1 = 0
p2 = 0

mem = {}

with open(sys.argv[1]) as f:
	inputlist = f.read().splitlines()
	mask = []
	for instruction in inputlist:
		
		if instruction[1] == "a":
			#mask
			mask_instruction = instruction.split(" ")
			mask = list(mask_instruction[2])
			#reverse mask (lsb instead of msb)
			#print (mask[::-1])
			#print(mask)
			
		if instruction[1] == "e":
			#mem
			#print(instruction)
			#mask to 0 with & , mask to 1 with |
			address = int(instruction.split(" ")[0][4:-1])
			value = instruction.split(" ")[2]
			binlsb = decimalToBinary(int(value))[::-1]
			print("address ",address," : value ",value," binary lsb : ",binlsb)
			binlsb = list(binlsb)
			#fill out bin with 0's
			for i in range(0,36-len(binlsb)):
				binlsb.append("0")
			for i, mb in enumerate(mask[::-1]):
				if mb != "X":
					print("bit ",mb," at #",i)
					if mb == "0":
						#and mask
						binlsb[i] = str(int(binlsb[i]) & int(mb))
					elif mb == "1":
						#or mask1
						binlsb[i] = str(int(binlsb[i]) | int(mb))
			maskedbinmsb = ''.join(binlsb[::-1])
			maskeddecimal = int(maskedbinmsb,2)
			
			#write masked decimal to memory
			mem[address] = maskeddecimal
	#print(mem)
	total = 0
	for key,value in mem.items():
		total += value
	p1 = total
	
	print("PART2")
	#part2
	#reset mask and mem
	mask = []
	xcount = 0
	xcombos = []
	xpositions = []
	mem = {}
	for instruction in inputlist:
		if instruction[1] == "a":
			#mask
			xpositions = []
			print(instruction)
			mask_instruction = instruction.split(" ")
			mask = list(mask_instruction[2])
			print(mask)
			xcount = mask.count("X")
			xcombos = list(itertools.product([0, 1], repeat=xcount))
			#print(xcombos)
			for i,m in enumerate(mask):
				if m == "X":
					xpositions.append(i)
			#print(xpositions)

			#print("number of X's : ",xcount)
		if instruction[1] == "e":
			#mem
			#print(instruction)
			#mask to 0 with & , mask to 1 with |
			address = int(instruction.split(" ")[0][4:-1])
			value = instruction.split(" ")[2]
			address_binlsb = decimalToBinary(int(address))[::-1]
			print("address_binlsb :",address_binlsb)

			address_binlsb = list(address_binlsb)
			#fill out bin with 0's
			for i in range(0,36-len(address_binlsb)):
				address_binlsb.append("0")
			for i, mb in enumerate(mask[::-1]):
				if mb == "X":
					address_binlsb[i] = "X"
				#print("bit ",mb," at #",i)
				if mb == "0":
					#do nothing
					continue
				elif mb == "1":
					#or mask1
					address_binlsb[i] = str(int(address_binlsb[i]) | int(mb))
			
			maskedbinmsb = address_binlsb[::-1]
			print("maskedbinmsb : ",maskedbinmsb)
			#maskeddecimaladdress = int(maskedbinmsb,2)
			#print(maskeddecimaladdress)

			#replace Xs with all possibilities
			print(xpositions)
			print(xcombos)
			#for each combo, replace the correct xposition in maskedbinmsb with corresponding xcombo bit
			for c in xcombos:
				for i,b in enumerate(c):
					
					#print("og masked address :",maskedbinmsb)
					#print("position to replace :",xpositions[i])
					#print("replacing",maskedbinmsb[xpositions[i]]," with ",b)
					maskedbinmsb[xpositions[i]] = str(b)
					#print(maskedbinmsb)
				result = int(''.join(maskedbinmsb),2)
				print("result : ",result)
				print("write ",value,"to mem[",result,"]")
				mem[result] = value
	memtotal = 0
	for key, value in mem.items():
		memtotal += int(value)
	p2 = memtotal




print("Part 1:",p1)
print("Part 2:",p2)