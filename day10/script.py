#!/usr/bin/env python3

import sys
import itertools

if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

p1 = 0
p2 = 0

counted=[]
differences = []

firstadapter = 0
endgoal = 0

data = {1 : [2,3],   # Directed acyclic graph adjacency list
		2 : [3],
		3 : [4,5],
		4 : [5]}

testdata = {1: [2], 2: [3, 4, 5], 3: [4, 5], 4: [5], 5: [6], 6: [7, 8], 7: [8], 8: [9], 9: [10], 10: [11]}

pathcount=0

def dfs(data, path, paths = []):   
	datum = path[-1]
	if datum in data:
		for val in data[datum]:
			new_path = path + [val]
			paths = dfs(data, new_path, paths)
	else:
		paths += [path]
		print(len(paths))
	return paths

with open(sys.argv[1]) as f:
	adapters = f.read().splitlines()
	adapters = [int(a) for a in adapters]
	adapters.sort()
	#for each adapter
	for i in range(len(adapters)):
		#print("Adapter : ",i, " rated for ",adapters[i], " jolts")
		#check adapters 1,2, or 3 jolts higher
		for j in range(1,4):
			if adapters[i]+j in adapters and adapters[i]+j not in counted:
				#print("Found an adapter rated for ",adapters[i]+j," jolts")
				counted.append(adapters[i]+j)
				#print("Diff: ",adapters[i]+j - adapters[i])
				differences.append(adapters[i]+j - adapters[i])
				break
			#stay within adapter count
			
				#print(adapters[i], " ",j)
				#difference 
	#devices adapter is always 3 higher than highest
	devicerating = adapters[-1] + 3
	#print("Last adapter value : ",adapters[-1])
	#print("Device jolt rating : ", devicerating)
	differences.append(devicerating - adapters[-1])
	
	#account for first adapter
	#print("First adapter value : ",adapters[0] )
	#print("First adapter diff : ",adapters[0] - 0)
	differences.append(adapters[0] - 0)

	#print(differences)
	print("3's : ",differences.count(3))
	print("1's : ",differences.count(1))
				
	# endgoal = adapters[-1] + 3
	# validcount = 0
	# adapters2 = adapters[:]
	

	# for i in range(len(adapters)):
	# 	print("Working on this iteration : (0)", end=",")
	# 	counted = []
	# 	for j in range(len(adapters)):
	# 		for k in range(1,4):
	# 			if adapters[j]+k in adapters and adapters[j]+k not in counted:
	# 				print("Found an adapter rated for ",adapters[j]+k," jolts")
	# 				counted.append(adapters[j]+k)
	# 				#print("Diff: ",adapters[i]+j - adapters[i])
	# 				#differences.append(adapters[i]+j - adapters[i])
	# 				break
			
	# 		#adapters.remove(adapters[i])
	# 		print(adapters[j], end=",")


	# 	print("\n")

	# 	#find out how far we get

	# 	#restore full adapters list 
	# 	adapters = adapters2[:]
	# 	#remove next single adapter
	# 	adapters.remove(adapters[i])

	# print("endgoal is ",adapters[-1]+3)
	# endgoal = adapters[-1]+3
	# #all possible combinations
	# counted=[]
	# totalchecked = 0
	# for p in range(1,len(adapters)+1):
		
	# 	for adapter_set in list(itertools.combinations(adapters,p)):
	# 		print("checking adapterset ",p," unique #",totalchecked)
	# 		currentadapters=[]
	# 		#print(adapter_set)
	# 		for a in adapter_set:
	# 			currentadapters.append(a)
	# 		#currentadapters = list(adapter_set) ## didn't work, couldn't index
	# 		#skip if first adapter in this set is further than 3 away from 0
			
			
	# 		#for each adapter
	# 		for c in range(len(currentadapters)):
	# 		#for c, value in enumerate(currentadapters):
	# 			#check adapters 1,2, or 3 jolts higher
	# 			#print("diff between ",currentadapters[i]+1,"and ",currentadapters[i],"is ",)
				
	# 			#dont exceed length of adapter list
	# 			totalchecked += 1
	# 			if c+1 < len(currentadapters):
	# 				#dont count list if differences bigger than 3 between adapters
	# 				if currentadapters[0] - 0 > 3:
	# 					break
	# 				if currentadapters[c+1] - currentadapters[c] > 3:
	# 					#print("diff bigger than 3")
	# 					break
	# 				if currentadapters[-1] != endgoal - 3:
	# 					break
	# 				if currentadapters[c+1] - currentadapters[c] > 3:
	# 					break
	# 				if currentadapters in counted:
	# 					break
	# 				else:
	# 					counted.append(currentadapters)
	# 					#print(currentadapters)
	# 					break

	# 			##print("Adapter : ",i, " rated for ",currentadapters[i], " jolts")
	# 			#for j in range(1,4):
	# 				#if currentadapters[i]+j in currentadapters and currentadapters[i]+j not in counted:
	# 					##print("Found an adapter rated for ",currentadapters[i]+j," jolts")
	# 					#counted.append(currentadapters[i]+j)
	# 					#break
			
	# 		#if counted[-1]+3 == endgoal:
	# 		#	print("made it to ",counted[-1]+3)
	# #print(counted)
	# counted_again = []

	# for c in counted:
	# 	if all(x < 4 for x in [y-x for x, y in zip(c[:-1], c[1:])]):
	# 		counted_again.append(c)
	# #print(counted_again)
	# print(len(counted_again))
	# p2 = len(counted_again)	

	# adapters.insert(0,0)
	# print(adapters)
	# tree = {}
	# edges = []
	# index_tree = {}
	# index_edges = []
	# for i in range(len(adapters)-1):
	# 	#for each adapter make list of adapters that are within 3 of it.
	# 	nextnodes = []
	# 	indexnextnodes = []
	# 	for j in range(len(adapters)):
	# 		if adapters[j] - adapters[i] < 4 and adapters[j] - adapters[i] > 0:
	# 			nextnodes.append(int(adapters[j]))
	# 			indexnextnodes.append(j+1)
	# 			edges.append((adapters[i],adapters[j]))
	# 			index_edges.append((i+1,j+1))
	# 	#print("adapter ",i, " : ",adapters[i]," connected to ",nextnodes)
	# 	tree[adapters[i]] = nextnodes
	# 	index_tree[i+1] = indexnextnodes
	# print(tree)

	# endpoint = adapters[-1]
	# completedpaths = []

	# #for i in [1,2,3]:
	# #	completedpaths = dfs(data = tree, path = [i], paths = [])
	# #	p2 += len(completedpaths)
	# #	print("done with path start : ",i)
	# dfsruns=0
	# completedpaths = dfs(data = tree, path = [0], paths = [])
	# p2 = len(completedpaths)

	# Create a dictionary to store the number of possible routes "to each joltage".
	routes = {}

	# Initialise with 1 route to the starting joltage.
	routes[0] = 1

	# Begin iterating through adaptors (ignoring the first value because we already set it above).
	for j in adapters:
		# Each joltage route is equal to the sum of the number of routes to the previous three joltages.
		# However, some of the joltages won't be present in the list of adaptors.
		# So the number of routes to them will be 0.
		routes[j] = routes.get(j-1, 0) + routes.get(j-2, 0) + routes.get(j-3, 0)
		print("j=",j," : j-1:",routes.get(j-1,0),"+ j-2:",routes.get(j-2,0),"+ j-3:",routes.get(j-3,0),"= ",routes.get(j-1, 0) + routes.get(j-2, 0) + routes.get(j-3, 0))

	# Print the number of possible routes to get to the final adaptor.
	print(routes)
	print(f"Part 2: {routes[max(routes.keys())]}")

print("\nPart 1:",differences.count(3)*differences.count(1))
print("Part 2:",p2)