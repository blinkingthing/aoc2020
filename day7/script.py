#!/usr/bin/env python3
#How many bag colors can eventually contain at least one shiny gold bag? 
import sys

if len(sys.argv) != 2:
    print("usage: solve.py input.txt")
    exit(1)

def populate_bag_colors():
	for rule in lines:
		colors.append(rule.split('bags')[0])

def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 

def find_shiny_holders():
	startcount = len(shiny_holders)
	print("starting shiny count = ",len(shiny_holders))
	for b in bags:
		for s in shiny_holders:
			for c in b["contents"]:
				if s in c["color"] and b["color"].rstrip() not in shiny_holders:
					shiny_holders.append(b["color"].rstrip())
					print(b["color"])
	print("ending shiny count = ",len(shiny_holders))
	endcount = len(shiny_holders)
	if (startcount != endcount):
		find_shiny_holders()
	else:
		shiny_holders.remove("shiny gold")
		print("Part 1 :",len(shiny_holders), "(can hold shiny golds.)")

def emptybagsatend(target_color):
	print("Reordering all bag contents")
	for b in bags:
			#if bag is ultimately within a shiny gold
		#if target_color in b["color"]:
		
		#move empty bags to end of list
		for c in b["contents"]:
			for ib in bags:
				if c["color"] in ib["color"]:
					for ic in ib["contents"]:
						if ic["count"] == "n":
							#print(b)
							#print("moving ",b["color"])
							b["contents"].append(b["contents"].pop(b["contents"].index(c)))
							#print(b)
							break

# def shiny_contents(target_color,parentcount,chain):
# 	count = 0
# 	bag_total = 0
# 	inner_bag_total = 0
# 	history = chain
# 	for b in bags:
# 			#if bag is ultimately within a shiny gold
# 		if target_color in b["color"]:
# 			#print(b["contents"])
# 			#move empty bags to end of list
# 			# for c in b["contents"]:
# 			# 	for ib in bags:
# 			# 		if c["color"] in ib["color"]:
# 			# 			for ic in ib["contents"]:
# 			# 				if ic["count"] == "n":
# 			# 					b["contents"].append(b["contents"].pop(b["contents"].index(c)))
# 			#print(b["contents"])

# 			#print(target_color," bag contains ",c["count"],c["color"],' bags')
# 			for c in b["contents"]:
# 				if c["color"] != "other":
# 					#for p in range(int(parentcount)):
# 					bag_total = int(c["count"]) * int(parentcount)
# 					inside_gold.append(bag_total)
# 					print(parentcount," ",target_color," bag contains ",c["count"],c["color"],' bags. This bags total =',bag_total,". Running total ",sum(inside_gold))
# 					history.append(int(c["count"]))
# 					print(history)

# 					shiny_contents(c["color"],int(c["count"]),history)

# 				else:
# 					print(b["color"], "bag is empty")
# 					#for h in history:
# 					#	history.remove(h)
# 					print(multiplyList(history))
# 					history.pop()
# 					return bag_total
# 			#print(target_color," bag contains ",c["count"],c["color"],' bags')
maybe_total = []
def search_bag_recursively(bag_color,parentcount,accumulative):
	for b in bags:
		if bag_color in b["color"]:
			for c in b["contents"]:
				if c["color"] == "other":
					#print("empty")
					return 0
				else:
					#print("parent count was ",parentcount)
					#print(c["count"], " ",c["color"]," bag(s)")
					#print(int(c["count"]) * int(parentcount)," ",c["color"]," bag(s) total")
					maybe_total.append(int(c["count"]) * int(parentcount))
					search_bag_recursively(c["color"],int(c["count"]) * int(parentcount),accumulative+int(c["count"]) * int(parentcount))
				#1 shiny gold, 2 wavy purple, 3 vibrant black, 4 vibrant cirmson = (4*3*2*1) = 24
				#1 shiny gold, 2 wavy putple, 3 vibrany black, 4 clear blue, 2 muted gold 
				#1 shiny gold, 2 wavy putple, 3 vibrany black, 4 clear blue, 5 bright magenta
				#1 shiny gold, 2 wavy putple, 3 vibrany black, 4 clear blue, 1 fade chartruse
				#1 shiny gold, 2 wavy putple, 3 vibrany black, 2 light chartreuse

				
				
				#find inner bags in bags list

				# if c["color"] == "other":
				# 	print(b["color"], "bag is empty")
				# 	return 1
				# else:
				# 	#check inner bag for 0 count
					
				# 	bag_total = int(c["count"]) * int(parentcount)				
					
				# 	print(parentcount," ",target_color," bag contains ",c["count"],c["color"],' bags. This bags total =',bag_total,"Running total = ",sum(total_within_shiny))
				# 	count += (int(c["count"]) * int(parentcount))
				# 	return bag_total + shiny_contents(c["color"],int(c["count"]))

				
				
				
			
					



				

bags = []
bag = {
	"color" : "color",
	"shinyhold" : False,
	"contents" : []
	
}

shiny_holders = ["shiny gold"]
shiny_held = ["shiny gold"]
inside_gold = []


with open(sys.argv[1]) as f:
	lines = f.read().splitlines()

	for l in lines:
		#toplevel bag color
		bag["color"] = l.split('bags')[0]
		#toplevel bag contents
		contents = l.split('contain')[1]
		inner_contents = contents.split(',')
		cleaned_contents = []
		for i in inner_contents:
			inner_bag = {
				"count" : 0,
				"color" : "color",
				"shinyhold" : False
			}
			
			i = i.strip()
			inner_bag["count"] = i[0]
			inner_bag["color"] = i[2:].replace("bags.","").replace("bag.","").replace("bags","").replace("bag","").strip()
			cleaned_contents.append(inner_bag.copy())
			#print(i)
		bag["contents"] = cleaned_contents
		bags.append(bag.copy())
	print("Original bag count : ",len(bags))
	
	#find bags with shiny_gold within
	find_shiny_holders()

	#emptybagsatend("shiny gold")
	
	#shiny_contents("shiny gold",1,[1])
	#print(sum(inside_gold))
	
	
	search_bag_recursively("shiny gold",1,0)
	print("Part 2 : ",sum(maybe_total),"(required inside your shiny gold)")


	# for b in bags:
	# 	#print(b)
	# 	#if main bag is shiny gold
	# 	if "shiny gold" in b["color"]:
	# 		shiny_holders.append(b["color"].rstrip())
	# 		#remove bag from list because it doesn't need to be checked anymore
	# 		bags.remove(b)
	# 	#check inner bags
	# 	for c in b["contents"]:
	# 		#if any inner bags are shiny gold
	# 		if "shiny gold" in c["color"]:
	# 			shiny_holders.append(b["color"].rstrip())
	# 			#remove bag from list because it doesn't need to be checked anymore
	# 			bags.remove(b)
	# print("Found ",len(shiny_holders)," shiny holders.  Down to ",len(bags)," bags")
	# print(shiny_holders)

	# for j in range(10):
	# 	print("looop ",j)
	# 	for b in bags:
	# 		i=0
	# 		og_shiny_length = len(shiny_holders)
	# 		while i < og_shiny_length:
	# 			more_shiny_holders = [] 
	# 			#if main bag is shiny holder
	# 			if shiny_holders[i] in b["color"]:
	# 			#if shiny_holders[i] in b["color"] and b["color"].rstrip() not in shiny_holders and b["color"].rstrip() not in more_shiny_holders:
	# 				#print("MATCHED ",shiny_holders[i],". ",b["color"]," main bag")
	# 				#more_shiny_holders.append(b["color"].rstrip())
	# 				#remove bag from list because it doesn't need to be checked anymore
	# 				bags.remove(b)
	# 			#check inner bags
	# 			for c in b["contents"]:
	# 				#if any inner bags are shiny gold
	# 				if shiny_holders[i] in c["color"] and b["color"].rstrip() not in shiny_holders and b["color"].rstrip() not in more_shiny_holders:
	# 					print("MATCHED ",shiny_holders[i],". ",c["color"]," inner bag in",b["color"]," main bag.")
	# 					more_shiny_holders.append(b["color"].rstrip())

	# 					#remove bag from list because it doesn't need to be checked anymore
	# 					bags.remove(b)
	# 			shiny_holders.extend(more_shiny_holders)
	# 			i += 1

	#for each bag
	#for each shiny bag holder
	#check to see if shiny bag holder
	
	# #for i in range(len(lines)):
	# for j in range(len(lines)):
	# 	for b in bags:
			
	# 		for s in shiny_holders:
	# 			s= s.rstrip()
	# 			#print(j, "checking ",s," against ",b["color"],". shiny gold holders found : ",len(shiny_holders))
				
	# 			if s in b["color"] and b["color"] not in shiny_holders:

	# 				shiny_holders.append(b["color"])
	# 			for c in b["contents"]:
	# 				#print(j, "checking inner bag ",s," against ",c["color"],". shiny gold holders found : ",len(shiny_holders))
	# 				if s in c["color"] and b["color"] not in shiny_holders:
	# 					print("loop ",j,". matched '",s,"'' with '",c["color"],"'' in '",b["color"],"'"," shinies : ",len(shiny_holders))
	# 					shiny_holders.append(b["color"])
			
			
	# print("Found ",len(shiny_holders)," shiny holders. Down to ",len(bags)," bags")
	# print(shiny_holders)
	# print(len(set(shiny_holders)))
	# print(len(bags))

	#297, 30, 27

	#part2 498 too low, 1838, too low 2336 too low, 1356, 1854
