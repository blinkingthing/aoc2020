#!/usr/bin/env python3
#How many bag colors can eventually contain at least one shiny gold bag? 
import sys

if len(sys.argv) != 2:
    print("usage: solve.py input.txt")
    exit(1)

bags = []
bag = {
	"color" : "color",
	"shinyhold" : False,
	"contents" : []
	
}

shiny_holders = ["shiny gold"]
inside_shiny_gold = []

def find_shiny_holders():
	startcount = len(shiny_holders)
	#print("starting shiny count = ",len(shiny_holders))
	for b in bags:
		for s in shiny_holders:
			for c in b["contents"]:
				if s in c["color"] and b["color"].rstrip() not in shiny_holders:
					shiny_holders.append(b["color"].rstrip())
					#print(b["color"])
	#print("ending shiny count = ",len(shiny_holders))
	endcount = len(shiny_holders)
	if (startcount != endcount):
		find_shiny_holders()
	else:
		shiny_holders.remove("shiny gold")
		print("Part 1 :",len(shiny_holders), "(can hold shiny golds.)")

def search_bag_recursively(bag_color,parentcount,accumulative):
	for b in bags:
		if bag_color in b["color"]:
			for c in b["contents"]:
				if c["color"] == "other":
					#empty bag / dead end
					return 0
				else:
					#this bags count * it's parent's count
					childandparent = int(c["count"]) * int(parentcount)
					inside_shiny_gold.append(childandparent)
					search_bag_recursively(c["color"],childandparent,accumulative+int(c["count"]) * int(parentcount))

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
	#print("Original bag count : ",len(bags))
	
	#find bags with shiny gold within
	find_shiny_holders()

	#find the bags that go in the bags that go in the bags....that go in the shiny gold
	search_bag_recursively("shiny gold",1,0)
	print("Part 2 :",sum(inside_shiny_gold),"(required inside your shiny gold)")
