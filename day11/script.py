#!/usr/bin/env python3

import sys
import copy
import numpy

if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

p1 = 0
p2 = 0

# . is floor
# L is empty
# # is occupied



seatmap = {}
seatmap2 = {}
oldmap = {}
oldmap2 = {}
mapchanged = True
mapchanges = 0


def buildseatmap(seats):
	for i,row in enumerate(seats):
		for j,seat in enumerate(row):
			#print(neighbors(j,i))
			index=str(j) +","+str(i)
			seatmap[index] = neighbors(j,i)
			seatmap[index].insert(0, seat)
			#insert blank occucount
			seatmap[index].insert(1, 0)

def flipseat(smap,x,y):
	#if occupied, empty
	if toflip == "#":
		toflip = "L"
	elif toflip =="L":
		toflip = "#"



def checkoccupancy(smap):
	for key, value in smap.items():
		#print("seat ",key," surrounded by the following : ",value[2:])
		occucount = 0
		for i in value[2:]:
		#each seat needs each surrounding seat counted
			#print("- seat ",i," is ",smap[str(i[0])+","+str(i[1])][0])
			if smap[str(i[0])+","+str(i[1])][0] == "#":
				occucount += 1
		#print("Number of occupied adjacent seats : ",str(occucount))
		smap[key][1] = occucount

def move(start,direction):
	#print("move(",start,",",direction,")")
	if direction == "U" or direction == "D":
		if 0 <= numpy.add(start,directions[direction])[1] <= Y+1:
				return numpy.add(start,directions[direction])
	elif direction == "L" or direction == "R":
		if 0 <= numpy.add(start,directions[direction])[0] <= X+1:
				return numpy.add(start,directions[direction])
	elif direction == "UL" or direction =="UR" or direction == "DL" or direction == "DR":
		if 0 <= numpy.add(start,directions[direction])[0] <= X+1 and 0 <= numpy.add(start,directions[direction])[1] <= Y+1:
				return numpy.add(start,directions[direction])

def checkoccupancy2(smap):
	for key, value in smap.items():
		#print("seat ",key," surrounded by the following : ",value[2:])
		occucount = 0
		keytuple = eval(key)
		x = keytuple[0]
		y = keytuple[1]
		neighbors2 = {
			"coords" : "",
			"U" : [],
			"UR" : [],
			"R" : [],
			"DR" : [],
			"D" : [],
			"DL" : [],
			"L" : [],
			"UL" : []
		}
		neighbors2["coords"] = keytuple
		#move in a direction, check to see if you're within map
		#up
		for i in range(y,0,-1):
			neighbors2["U"].append(move(keytuple,"U"))
			newx = neighbors2["U"][-1][0]
			newy = neighbors2["U"][-1][1]
			keytuple = (newx,newy)
			#if occupied seat seen
			if seatmap[str(newx)+","+str(newy)][0] == "#":
				occucount += 1
				break
		#down
		keytuple = eval(key)
		#print(range(y,Y))
		for i in range(y,Y):
			neighbors2["D"].append(move(keytuple,"D"))
			newx = neighbors2["D"][-1][0]
			newy = neighbors2["D"][-1][1]
			keytuple = (newx,newy)
			#if occupied seat seen
			if seatmap[str(newx)+","+str(newy)][0] == "#":
				occucount += 1
				break
		#left
		keytuple = eval(key)
		#print(range(x,0,-1))
		for i in range(x,0,-1):
			neighbors2["L"].append(move(keytuple,"L"))
			newx = neighbors2["L"][-1][0]
			newy = neighbors2["L"][-1][1]
			keytuple = (newx,newy)
			#if occupied seat seen
			if seatmap[str(newx)+","+str(newy)][0] == "#":
				occucount += 1
				break
		#right
		keytuple = eval(key)
		#print(range(x,X))
		for i in range(x,X):
			neighbors2["R"].append(move(keytuple,"R"))
			newx = neighbors2["R"][-1][0]
			newy = neighbors2["R"][-1][1]
			keytuple = (newx,newy)
			#if occupied seat seen
			if seatmap[str(newx)+","+str(newy)][0] == "#":
				occucount += 1
				break
		print(neighbors2)

def checkoccupancy3(smap):
	for key, value in smap.items():
		occucount = 0
		keytuple = eval(key)
		x = keytuple[0]
		y = keytuple[1]
		#if seat is empty
		#print("checking : ",keytuple)
		
		#for each direction
		for d in dirs:
			if d == "U" or d == "D":
				#print(directions[d])
				keytuple = eval(key)
				while 0 <= numpy.add(keytuple,directions[d])[1] <= Y:
					#print(numpy.add(keytuple,directions[d])," : ",seatmap[str(keytuple[0])+","+str(keytuple[1])][0])
					oldkeytuple = keytuple
					newx = numpy.add(keytuple,directions[d])[0]
					newy = numpy.add(keytuple,directions[d])[1]
					keytuple = (newx,newy)
					#increase occucount if you see occupied seat.
					if seatmap2[str(keytuple[0])+","+str(keytuple[1])][0] == "#":
						occucount += 1
						break
					#just break if you see an empty seat
					elif seatmap2[str(keytuple[0])+","+str(keytuple[1])][0] == "L":
						break
					
			if d == "L" or d =="R":
				keytuple = eval(key)
				while 0 <= numpy.add(keytuple,directions[d])[0] <= X:
					#print(numpy.add(keytuple,directions[d])," : ",seatmap[str(keytuple[0])+","+str(keytuple[1])][0])
					oldkeytuple = keytuple
					newx = numpy.add(keytuple,directions[d])[0]
					newy = numpy.add(keytuple,directions[d])[1]
					keytuple = (newx,newy)
					#increase occucount if you see occupied seat.
					if seatmap2[str(keytuple[0])+","+str(keytuple[1])][0] == "#":
						occucount += 1
						break
					#just break if you see an empty seat
					elif seatmap2[str(keytuple[0])+","+str(keytuple[1])][0] == "L":
						break
					
			if d == "UL" or d == "UR" or d == "DL" or d == "DR":
				keytuple = eval(key)
				while 0 <= numpy.add(keytuple,directions[d])[0] <= X and 0 <= numpy.add(keytuple,directions[d])[1] <= Y:
					oldkeytuple = keytuple
					newx = numpy.add(keytuple,directions[d])[0]
					newy = numpy.add(keytuple,directions[d])[1]
					keytuple = (newx,newy)
					#increase occucount if you see occupied seat.
					if seatmap2[str(keytuple[0])+","+str(keytuple[1])][0] == "#":
						occucount += 1
						break
					#just break if you see an empty seat
					elif seatmap2[str(keytuple[0])+","+str(keytuple[1])][0] == "L":
						break
					
					
		#update this seats seen occupied seats
		seatmap2[key][1] = occucount
		
				


def printmap(smap):
	for key, value in smap.items():
		print(key,value,"\n")

def split(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]

def printseats(smap,printoccupancy):
	seats = ""
	occucounts = ""
	for key, value in smap.items():
		seats += smap[key][0]
		occucounts += str(smap[key][1])
	
	for row in split(seats,len(ferryseats[0])):
		print(row)
	print("\n")
	if printoccupancy == True:
		for row in split(occucounts,len(ferryseats[0])):
			print(row)
		print("\n")

def flipseats(smap,occufliplimit):
	for key, value in smap.items():
		#if seat is empty (L) and there are no (0) occupied seats, it becomes occupied
		if smap[key][0] == "L" and smap[key][1] == 0:
			smap[key][0] = "#"
		#if seat is occupied (#) and there are 4/5 (occufliplimit) or more occupied adjacent seats, it becomes empty
		if smap[key][0] == "#" and smap[key][1] >= occufliplimit:
			smap[key][0] = "L"

def checkchange(omap, smap):
	if omap == smap:
		mapchanged = False
		return mapchanged
	else:
		mapchanged = True
		return mapchanged

def changemap(mapchanges):
	
	#check occupancy
	checkoccupancy(seatmap)
	#make copy of map to check changes agains
	oldmap = copy.deepcopy(seatmap)
	#printmap(seatmap)
	
	#flip seats that need flipping
	flipseats(seatmap, 4)
	checkoccupancy(seatmap)
	if checkchange(oldmap,seatmap) == True:
		mapchanges += 1
		#print("current map change count ",mapchanges)
		changemap(mapchanges)
	else:
		finaloccucount = 0
		#printmap(seatmap)
		for key, value in seatmap.items():
			if value[0] == "#":
				finaloccucount += 1
		#print("final occupied seat count : ",finaloccucount)
		print("map changed ",mapchanges," times")
		print("Part 1 : ",finaloccucount)

def changemap2(mapchanges):
	printseats(seatmap2, False)
	#check occupancy
	checkoccupancy3(seatmap2)
	#make copy of map to check changes against
	oldmap2 = copy.deepcopy(seatmap2)

	#flip seats that need flipping
	flipseats(seatmap2, 5)
	#checkoccupancy3(seatmap)
	if checkchange(oldmap2,seatmap2) == True:
		mapchanges += 1
		#print("current map change count ",mapchanges)
		changemap2(mapchanges)
	else:
		finaloccucount = 0
		#printmap(seatmap)
		printseats(seatmap2, False)
		for key, value in seatmap2.items():
			if value[0] == "#":
				finaloccucount += 1
		#print("final occupied seat count : ",finaloccucount)
		print("map changed ",mapchanges," times")
		print("Part 2 : ",finaloccucount)



dirs = ["U","UR","R","DR","D","DL","L","UL"]

directions={
	"U":(0,-1),
	"UR" : (1,-1),
	"R" : (1,0),
	"DR" : (1,1),
	"D" : (0,1),
	"DL" : (-1,1),
	"L" : (-1,0),
	"UL" : (-1,-1)
}

with open(sys.argv[1]) as f:
	ferryseats = f.read().splitlines()

	# Size of "board"
	X = len(ferryseats[0])-1
	Y = len(ferryseats)-1
	#build dictionary of neighboring seat coordinates
	neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
								for y2 in range(y-1, y+2)
								if (-1 < x <= X and
									-1 < y <= Y and
									(x != x2 or y != y2) and
									(0 <= x2 <= X) and
									(0 <= y2 <= Y))]

	buildseatmap(ferryseats)
	
	seatmap2 = copy.deepcopy(seatmap)

	#part 1 
	#changemap(mapchanges)	
		
	#print(seatmap["0,0"])
	#print(seatmap["97,90"])
	
#	printmap(seatmap)

	#checkoccupancy2(seatmap)
	#print(seatmap)

	#reset for part2
	#buildseatmap(ferryseats)
	mapchanges = 0
	finaloccucount = 0

	changemap2(mapchanges)
	#checkoccupancy3(seatmap)	

	
print("\nPart 1:",p1)
print("Part 2:",p2)