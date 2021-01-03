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

	#print("your ticket:",yourticket)
	#print("nearby tickets:",nearbytickets)
	#print("length of your ticket", len(yourticket))
	#print("length of nearby tickets before removing invalid",len(nearbytickets))
	#print(fields)

	all_fields = []
	all_tickets = yourticket + nearbytickets

	for key,value in fields.items():
		#print(value.split(" ")[0].split("-"))
		one = list(range(int(value.split(" ")[0].split("-")[0]),int(value.split(" ")[0].split("-")[1])+1))
		#print(value.split(" ")[2])
		two = list(range(int(value.split(" ")[2].split("-")[0]),int(value.split(" ")[2].split("-")[1])+1))
		#print(key)
		#print(one)
		#print(two)
		fields[key] = one + two
		all_fields += fields[key]
		#print(key)
		#print(value)
	#print(fields)

	#all_tickets = list(set(all_tickets))
	#all_fields = list(set(all_fields))
	
	#print("part 1 tickets : ",all_tickets)
	#print("part 1 valid fields : ",all_fields)
	# differences = numpy.setdiff1d(all_tickets,all_fields)
	# print("part 1 differences : ",differences)
	# sumofdifferences = 0
	# for d in differences:
	# 	sumofdifferences += d
	# p1 = sumofdifferences
	
	##PART 1 lesson learned - read the prompt - I was checking for differences between all the tickets and the fields, should've only been checking nearby tickets

	diff = 0
	nearby = []
	ticketlength = len(fields)
	invalidtickets = []

	for i in nearbytickets:
		if i not in all_fields:
			diff += i
			invalidtickets.append(i)
			
	nearby = [nearbytickets[i:i + ticketlength] for i in range(0, len(nearbytickets), ticketlength)]

	#print(nearby)
	#print(invalidtickets)
	ticketstoremove = []
	validtickets = []
	for i,n in enumerate(nearby):
		for t in invalidtickets:
			#print("Checking ",n," for ",t)
			if t in n:
				#print("found ",t," in ",n)
				#remove nearby tickets with invalid tickets
				#nearby.remove(nearby[i])
				ticketstoremove.append(i)
	#print("need to remove these tickets :",ticketstoremove)
	for i,n in enumerate(nearby):
		if i not in ticketstoremove:
			validtickets.append(nearby[i])
	#for v in validtickets:
		#print(v)
	#print(len(nearby))
	#print(len(validtickets))
	#print("length of nearby after removing invalid ticekts :",len(nearby)*ticketlength)

	ticketcolumns = []
	for i in range(len(fields)):
		ticketcolumns.append([])
	validfields = []
	
	#print(len(ticketcolumns))
	#print(len(nearby))
	

	for ticket in validtickets:
		#print(ticket)
		for i,c in enumerate(ticket):
			ticketcolumns[i].append(ticket[i])
	
	

	def checkfit(tc,field):
		perfectfit = True
		for t in ticketcolumns[tc]:
			if t not in fields[field]:
				perfectfit = False
		return perfectfit

	columnsandfits = {}
	#check each column to see how many fields' rules it adheres to perfectly
	for i,tc in enumerate(ticketcolumns):
		fitcount = 0
		fits = []
		for key,value in fields.items():
			if checkfit(i,key) == True:
				#print("Column ",i," Field ",key,' Perfect fit :',checkfit(i,key))
				fitcount += 1
				fits.append(key)
		#print("Column ",i," has ",fitcount," perfect fits ",fits)
		columnsandfits[i] = fits
	
	#print(columnsandfits)

	matchedcolumns = {}

	#until all 20 columns are matched find the column with least ammount of fits. Add the one that isn't in matched columns to matched columns
	while len(matchedcolumns) < 20:
		for key,value in columnsandfits.items():
			#print(len(value))
			if len(value) == len(matchedcolumns)+1:
				for v in value:
					#print(v)
					if v not in matchedcolumns:
						
						matchedcolumns[v] = key
		
	#print(matchedcolumns)
	#print(yourticket)
	
	#my validated ticket
	myvalidatedticket = {}
	for key,value in matchedcolumns.items():
		for i,yt in enumerate(yourticket):
			if value == i:
				myvalidatedticket[key] = yourticket[i]
	
	#ticket with corrected fields and values
	#print(myvalidatedticket)

	
	
	p2 = 1
	for key, value in myvalidatedticket.items():
		if "departure" in key:
			#just departures
			#print(key," : ",myvalidatedticket[key])
			
			p2 *= myvalidatedticket[key]






	
	
	#for n in nearby:
	#	print(n)
	# #print(nearby)
	# for n in nearby:
	# 	for key,value in fields.items():
	# 		#print(value.split(" ")[0].split("-"))
	# 		#one = list(range(int(value.split(" ")[0].split("-")[0]),int(value.split(" ")[0].split("-")[1])+1))
	# 		#print(value.split(" ")[2])
	# 		#two = list(range(int(value.split(" ")[2].split("-")[0]),int(value.split(" ")[2].split("-")[1])+1))
	# 		#print(key)
	# 		#print(one)
	# 		#print(two)
	# 		for i,q in enumerate(n):
	# 			if n[i] in fields[key]:
	# 				ticketcolumns[i].append(key)
	# 				print(n[i]," in ", key)
	# 				print("++++")
	
	# for i,t in enumerate(ticketcolumns):
		
	# 	for key,value in fields.items():
	# 		columnsthatfit = 0
	# 		print(key," in ticketcolumn",i," ",t.count(key)," times")
	# 		if t.count(key) == len(ticketcolumns):
	# 			columnsthatfit += 1
	# 		print(columnsthatfit)
	
	
	
	
			
			
	

	#print(diff)
	p1 = diff

	
	
	
	

print("Part 1:",p1)
print("Part 2:",p2)