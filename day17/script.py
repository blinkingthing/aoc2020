#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

p1 = 0
p2 = 0

startinggrid = {}
startinggrid2 = {}

with open(sys.argv[1]) as f:
	inputlist = f.read().splitlines()
	#z is initially 0 for first layer
	z =0
	w = 0
	
	#build initial grid from input
	for i,line in enumerate(inputlist):
		for j,cube in enumerate(line):
			#print("Cube x=",j,", y=",i," z=",z,"cube = ",cube)
			if cube == "#":
				startinggrid[(j,i,z)]=1
				startinggrid2[(j,i,z,w)]=1
			else:
				startinggrid[(j,i,z)]=0
				startinggrid2[(j,i,z,w)]=0
				

	def surrounding3(coordinates):
		#print("checking coords surrounding ",coordinates)
		surrounding_coords = []
		mod,mod2,mod3 = -1,-1,-1
		coordinates = coordinates[:3]
		#print(coordinates)
		for i in range(3):
			for j in range(3):
				for k in range(3):
					#print("mods ",mod,mod2,mod3)
					
					coord = (coordinates[0]+mod,coordinates[1]+mod2,coordinates[2]+mod3)
					if coord != coordinates:
						#print(coord)
						surrounding_coords.append(coord)
				
					mod3 += 1
				#every 1
				mod3 = -1
				mod2 +=1
			#every9 
			mod2 = -1
			mod+=1
		#print(surrounding_coords)
		return surrounding_coords


	def surrounding(coordinates):
		#print("checking coords surrounding ",coordinates)
		surrounding_coords = []
		mod,mod2,mod3,mod4 = -1,-1,-1,-1
		
		#range == 3 because you can be on either side of the og position. +1, 0, or -1
		for i in range(3):
			for j in range(3):
				for k in range(3):
					for l in range(3):
						#print("mods ",mod,mod2,mod3)
						
						coord = (coordinates[0]+mod,coordinates[1]+mod2,coordinates[2]+mod3,coordinates[3]+mod4)
						if coord != coordinates:
							#print(coord)
							surrounding_coords.append(coord)
						#print(coord)
						mod4 += 1
					mod4 = -1
					mod3 += 1
				#every 1
				mod3 = -1
				mod2 +=1
			#every9 
			mod2 = -1
			mod+=1
		
		
		#print(surrounding_coords)
		return surrounding_coords
	
	#print(startinggrid)
	def activeneightboors(part,inputgrid):
		#seen_active = []
		#print("checking ",key)
		#check active neighbors
		#print("inputgrid : ",inputgrid)
		#max and min actives for each direction
		outputgrid = {}
		surrounding_cubes = []
		if part == 1:
			for key, value, in inputgrid.items():
				#only check cubes surrounging an active
				if value == 1:
					#print("neighboors of ",key," : ",surrounding(key))
					for cube in surrounding3(key):
						
						#add all cubes seen to surrounding_cubes to iterate over
						if cube not in surrounding_cubes:
							surrounding_cubes.append(cube)
					#count active neighbors
		elif part == 2:
			for key, value, in inputgrid.items():
				#only check cubes surrounging an active
				if value == 1:
					#print("neighboors of ",key," : ",surrounding(key))
					for cube in surrounding(key):
						#print(cube)
						#add all cubes seen to surrounding_cubes to iterate over
						if cube not in surrounding_cubes:
							surrounding_cubes.append(cube)
					#count active neighbors
		print("total surrounding cubes : ",len(surrounding_cubes))
		if part == 1:
			for outtercube in surrounding_cubes:
				active_neighboor_count = 0
				for cube in surrounding3(outtercube):
					if cube in inputgrid:
						#if cube not in seen_active:
						#	seen_active.append(cube)
						if inputgrid[cube] == 1:
							active_neighboor_count += 1
				#print(outtercube," has ",active_neighboor_count," active neighbors")
				#active neighbor rules / conditions
				#if outter was part of input grid, check if active
				if outtercube in inputgrid:
					if inputgrid[outtercube] == 1:
						#active rules
						if 1 < active_neighboor_count < 4:
							outputgrid[outtercube] = 1
						else:
							outputgrid[outtercube] = 0
					else:
						#inactive rules
						if active_neighboor_count == 3:
							outputgrid[outtercube] = 1
						else:
							outputgrid[outtercube] = 0
				else:
					#inactiverules
					if active_neighboor_count == 3:
						outputgrid[outtercube] = 1
					else:
						outputgrid[outtercube] = 0
			#print(seen_active)
			#print(len(surrounding_cubes))
				#print(outtercube,len( surrounding_cubes))
		elif part == 2:
			for outtercube in surrounding_cubes:
				active_neighboor_count = 0
				for cube in surrounding(outtercube):
					if cube in inputgrid:
						#if cube not in seen_active:
						#	seen_active.append(cube)
						if inputgrid[cube] == 1:
							active_neighboor_count += 1
				#print(outtercube," has ",active_neighboor_count," active neighbors")
				#active neighbor rules / conditions
				#if outter was part of input grid, check if active
				if outtercube in inputgrid:
					if inputgrid[outtercube] == 1:
						#active rules
						if 1 < active_neighboor_count < 4:
							outputgrid[outtercube] = 1
						else:
							outputgrid[outtercube] = 0
					else:
						#inactive rules
						if active_neighboor_count == 3:
							outputgrid[outtercube] = 1
						else:
							outputgrid[outtercube] = 0
				else:
					#inactiverules
					if active_neighboor_count == 3:
						outputgrid[outtercube] = 1
					else:
						outputgrid[outtercube] = 0
			#print(seen_active)
			#print(len(surrounding_cubes))
				#print(outtercube,len( surrounding_cubes))
		if part == 1 :
			print("PART 1 : active cubes : ",sum(value == 1 for value in outputgrid.values()))
		else: 
			print("PART 2 : active cubes : ",sum(value == 1 for value in outputgrid.values()))
		p2 = sum(value == 1 for value in outputgrid.values())
		return outputgrid
	

	def cycle(inputgrid,cycles = 0):
		if cycles < 6:
			return cycle(activeneightboors(1,inputgrid), cycles+1)
	
	def cycle2(inputgrid,cycles = 0):
		if cycles < 6:
			return cycle2(activeneightboors(2,inputgrid), cycles+1)
		
		
	

#print(len(surrounding((0,0,0,0))))	
#print(len(surrounding3((0,0,0))))	
#print(startinggrid)
#p1 = sum(value == 1 for value in cycle(cycle(cycle(cycle(cycle(cycle(startinggrid)))))).values())



#print(sum(value == 1 for value in cycle(startinggrid,2)[0].values()))
p1 = cycle(startinggrid)
p2 = cycle2(startinggrid2)


print("Part 1  : ",p1)
print("Part 2 : ",p2)