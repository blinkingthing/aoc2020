#!/usr/bin/env python3

import sys
import copy
import numpy

if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

p1 = 0
p2 = 0

facedir = "E"
movedir = ""

shipcoords = {
	"E" : 0,
	"W" : 0,
	"N" : 0,
	"S" : 0
}

waypointcoords = {
	"E" : 10,
	"W" : 0,
	"N" : 1,
	"S" : 0
}


rightturn = ["N","E","S","W","N","E","S"]
leftturn = ["N","W","S","E","N","W","S"]

def turn(turndirection,facedir,value):
	print(facedir," index is ",turndirection.index(facedir))
	if int(value) == 90:
		facedir = turndirection[turndirection.index(facedir)+1]
		return facedir
	elif int(value) == 180:
		facedir = turndirection[turndirection.index(facedir)+2]
		return facedir
	elif int(value) == 270:
		facedir = turndirection[turndirection.index(facedir)+3]
		return facedir

def rotatewaypoint(coorddict,turndir,rotval):
	rotated = {}
	for key, value in coorddict.items():
		cardinal = ""
		if int(rotval) == 90:
			#get rotated cardinal direction and set it to the same value, remove old direction/value
			cardinal = turndir[turndir.index(key)+1]
			rotated[cardinal] = value
			
		elif int(rotval) == 180:
			#get rotated cardinal direction and set it to the same value, remove old direction/value
			cardinal = turndir[turndir.index(key)+2]
			rotated[cardinal] = value
			
		elif int(rotval) == 270:
			#get rotated cardinal direction and set it to the same value, remove old direction/value
			cardinal = turndir[turndir.index(key)+3]
			rotated[cardinal] = value
	return rotated
			

def manhattan(coords):
	return max(coords["N"], coords["S"]) - min(coords["N"], coords["S"]) + max(coords["E"], coords["W"]) - min(coords["E"], coords["W"])

with open(sys.argv[1]) as f:
	inputlist = f.read().splitlines()
	direction =""
	value = 0
	for i in inputlist:
		direction = i[0]
		value = i[1:]
		print("direction : ",direction," value :",value)
		#forward
		if direction == "F":
			shipcoords[facedir] += int(value)
			print("moving forward (",facedir,") ",value," spaces")
		#right turn - change facedir
		elif direction == "R":
			facedir = turn(rightturn,facedir,value)
			print("turning right ",value," degrees to face ",facedir)
		#left turn - change facedir
		elif direction == "L":
			facedir = turn(leftturn,facedir,value)
			print("turning left ",value," degrees to face ",facedir)
		elif direction == "N" or direction == "E" or direction == "W" or direction == "S":
			shipcoords[direction] += int(value)
			print("moving ",direction," ",value," spaces")
	
	print(shipcoords)
	#print("Manhattan Distance = ",manhattan(shipcoords))
	p1 = manhattan(shipcoords)
	
	#reset shipcoords
	shipcoords["N"] = 0
	shipcoords["E"] = 0
	shipcoords["W"] = 0
	shipcoords["S"] = 0
	print("## PART 2 ## ship:",shipcoords)
	#part 2
	for i in inputlist:
		direction = i[0]
		value = i[1:]
		print("## direction : ",direction," value :",value)
		if direction == "N" or direction == "E" or direction == "W" or direction == "S":
			waypointcoords[direction] += int(value)
			print("moving waypoint ",direction," ",value," spaces")
			print("WP: ",waypointcoords)
		if direction == "R":
			print("rotating waypoint to the ",direction)
			print("WP: ",waypointcoords)
			waypointcoords = rotatewaypoint(waypointcoords,rightturn,value)
			print("WP: ",waypointcoords)
		if direction == "L":
			print("rotating waypoint to the ",direction)
			print("WP: ",waypointcoords)
			waypointcoords = rotatewaypoint(waypointcoords,leftturn,value)
			print("WP: ",waypointcoords)
		if direction =="F":
			for key,v in waypointcoords.items():
				movevalue = int(v)*int(value)
				shipcoords[key] += movevalue
				#waypointcoords[key] += movevalue
				print("moving ship towards waypoint (",key,") ",movevalue," spaces")
			print("SHIP COORDS : ",shipcoords)
			print("WP: ",waypointcoords)
	p2 = manhattan(shipcoords)
	print(manhattan(shipcoords))
		



print("Part 1:",p1)
print("Part 2:",p2)