#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

p1 = 0
p2 = 0

infinitegrid = {}

with open(sys.argv[1]) as f:
	inputlist = f.read().splitlines()
	#z is initially 0 for first layer
	z =0
	
	#build initial grid from input
	for i,line in enumerate(inputlist):
		for j,cube in enumerate(line):
			#print("Cube x=",j,", y=",i," z=",z,"cube = ",cube)
			if cube == "#":
				infinitegrid[(j,i,z)]=1
			else:
				infinitegrid[(j,i,z)]=0
	
	def surrounding(coordinates):
		#print("checking coords surrounding ",coordinates)
		surrounding_coords = []
		mod,mod2,mod3 = -1,-1,-1
		
		for i in range(len(coordinates)):
			for j in range(len(coordinates)):
				for k in range(len(coordinates)):
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

	print(infinitegrid)

	

	for key,value in infinitegrid.items():
		seen_active = []
		seen_inactive = []
		#print("checking ",key)
		#check active neighbors
		for cube in surrounding(key):
			if cube in infinitegrid:
				#print(s)
				if infinitegrid[cube] == 1:
					#if seen in infinitegrid and active
					if cube not in seen_active:
						seen_active.append(cube)
				else:
					#if seen in infinitegrid and inactive
					if cube not in seen_inactive:
						seen_inactive.append(cube)
			#if in surround, but not in infinitegrid, it's inactive
			elif cube not in infinitegrid:
				if cube not in seen_inactive:
						seen_inactive.append(cube)				

		active_neighbors = len(seen_active)
		inactive_neighbors = len(seen_inactive)
		#print("active ",seen_active)
		print(cube,"has ",active_neighbors," active neighbors and ",inactive_neighbors," inactive neighbors")
		#print("inactive ",seen_inactive)
		
	



print("Part 1:",p1)
print("Part 2:",p2)