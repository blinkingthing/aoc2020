#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("usage: solve.py input.txt")
    exit(1)

with open(sys.argv[1]) as f:
	lines = f.read().splitlines()
	#lines=['FBFBBFFRLR']
	row=0
	col=0

	ids=[]
	seatid={}
	seen = []
	seenrow = []
	seenid = []
	
	for bpass in lines:
		
		bpass = bpass.replace("F","0")
		bpass = bpass.replace("B","1")

		bpass = bpass.replace("L","0")
		bpass = bpass.replace("R","1")

		row = int(bpass[:7],2)
		column = int(bpass[-3:],2)

		ids.append(row * 8 + column)
		seatid={
			'row':row,
			'column':column,
			'id' : row*8+column
		}
		seen.append(seatid)
		#check for nonexistent rows/seats
		
	print('Part 1 :',max(ids))

	for s in seen:
	 	if s['row'] not in seenrow:
	 		seenrow.append(s['row'])
	 	if s['id'] not in seenid:
	 		seenid.append(s['id'])
	
	seenid = sorted(seenid)

	for i in range(seenid[0],seenid[-1]):
		if i not in seenid:
			print('Part 2 :',i)