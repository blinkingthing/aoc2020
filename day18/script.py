#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

p1 = 0
p2 = 0

with open(sys.argv[1]) as f:
	inputlist = f.read().splitlines()
	
	#for line in inputlist:
	#	print(line)

	
	def checkforparenthesis(tocheck):
		parenthesis = []
		for c in tocheck:
			if c == "(" or c == ")":
				parenthesis.append(c)
		return parenthesis
		#print(parenthesis)


	def current_p_start(parenthesis):
		for i, p in enumerate(parenthesis):
			if p == ")":
				return i-1

	#print(current_p_start(parenthesis))

	def leftmost_p_contents(inputline,startingp):
		parenthesis_count = 0
		equation = []
		ending_parenthesis_loc = 0
		for i,c in enumerate(inputline):
			if c == "(":
				#add to count for every left parenthesis you see
				parenthesis_count += 1
			#if it's the target parenthesis
			if parenthesis_count == startingp+1:
				#if you reach the end of target parenthesis, break
				if c == ")":
					ending_parenthesis_loc = i
					equation.append(c)
					break
				#add contents of target perenthesis to equation[]
				equation.append(c)
		return equation, ending_parenthesis_loc
	
	def simplesolve(equation):
		if equation[1] == "*":
			return(int(equation[0]) * int(equation[2]))
		else:
			return(int(equation[0]) + int(equation[2]))
	

	def solve_from_left(equation,method):
		#strip parenthesis if they exist
		if equation[0] == "(":
			equation = equation[1:-1]
		#standard method, from left to right
		if method == 0:
			#print("** Length of equation to be solved = ",len(equation))
			#get first 2 digits + operator and solve
			first_three = equation[:3]
			#print("solve from left: ",equation)
			#print(first_three)
			#remove first_three from equation
			leftovers = []
			leftovers = equation[3:]
			#print("leftovers : ",leftovers)
			reduced = []
			reduced.append(simplesolve(first_three))
			#print("reduced after simplesolve : ",reduced)
			for l in leftovers:
				reduced.append(l)
		#part 2 method, left to right, addition before multiplication
		if method == 1:
			#if there are remaining additions
			if equation.count("+") > 0:
				leftmost_addition = []
				leftmost_add_loc = 0
				for i,e in enumerate(equation):
					if e =="+":
						leftmost_add_loc = i
						leftmost_addition.append(equation[i-1])
						leftmost_addition.append(equation[i])
						leftmost_addition.append(equation[i+1])
						break
				print(leftmost_addition)
				print(simplesolve(leftmost_addition))
				#get first 2 digits + operator and solve
				equation[leftmost_add_loc-1] = simplesolve(leftmost_addition)
				#pop remaining two parts of original equation
				equation.pop(leftmost_add_loc)
				equation.pop(leftmost_add_loc)
				print(equation)
				
				#print("leftovers : ",leftovers)
				reduced = equation
			#else do multiplications
			else:
				leftmost_multiplication = []
				leftmost_multiply_loc = 0
				for i,e in enumerate(equation):
					if e =="*":
						leftmost_multiply_loc = i
						leftmost_multiplication.append(equation[i-1])
						leftmost_multiplication.append(equation[i])
						leftmost_multiplication.append(equation[i+1])
						break
				print(leftmost_multiplication)
				print(simplesolve(leftmost_multiplication))
				#get first 2 digits + operator and solve
				equation[leftmost_multiply_loc-1] = simplesolve(leftmost_multiplication)
				#pop remaining two parts of original equation
				equation.pop(leftmost_multiply_loc)
				equation.pop(leftmost_multiply_loc)
				print(equation)
				reduced = equation
		
		
		return reduced if len(reduced) == 1 else solve_from_left(reduced,method)


	def reduceparenthesis(inputequation,method):
		parenthesis = checkforparenthesis(inputequation)
		#print(parenthesis)
		#location of first parenthesis to reduce
		starting_parenethesis = current_p_start(parenthesis)
		#print("starting parenthesis location",starting_parenethesis)
		unreduced = leftmost_p_contents(inputequation,starting_parenethesis)
		#print("unreduced :", unreduced[0])
		reduced = solve_from_left(unreduced[0],method)
		#print("reduced : ", reduced)
		start_of_replacement = unreduced[1]-(len(unreduced[0])-1)
		#print("start of section to be replaced :",start_of_replacement)
		#print("length of section to be replaced : ",len(unreduced[0]))
		#print(inputequation)
		inputequation[start_of_replacement] = reduced[0]
		#print(inputequation)
		#replace unreduced with reduced
		for i in range(len(unreduced[0])-1):
			inputequation.pop(start_of_replacement+1)
		#print(inputequation)
		parenthesis = checkforparenthesis(inputequation)
		return inputequation if len(parenthesis) == 0 else reduceparenthesis(inputequation,method)


	def solveequation(inputequation):
		#print("checking : ",inputequation)
		#remove spaces
		equation_nospaces= []
		for i in inputequation:
			if i == ' ':
				continue
			else:
				equation_nospaces.append(i)
		print(equation_nospaces)
		if len(checkforparenthesis(inputequation)) > 0:
			#parenthesis exist, reduce parenthesis
			#print("yes parenthesis")
			answer = solve_from_left(reduceparenthesis(equation_nospaces,0),0)[0]
		else:
			#no parenthesis
			answer = solve_from_left(equation_nospaces,0)[0]
		return(answer)

	answers = []
	for i in range(len(inputlist)):
		print(solveequation(inputlist[i]))
		answers.append(solveequation(inputlist[i]))
	
	print(answers)
	p1 = sum(answers)
	
	def solveequation2(inputequation):
		#print("checking : ",inputequation)
		#remove spaces
		equation_nospaces= []
		for i in inputequation:
			if i == ' ':
				continue
			else:
				equation_nospaces.append(i)
		print(equation_nospaces)
		if len(checkforparenthesis(inputequation)) > 0:
			#parenthesis exist, reduce parenthesis
			#print("yes parenthesis")
			answer = solve_from_left(reduceparenthesis(equation_nospaces,1),1)[0]
		else:
			#no parenthesis
			answer = solve_from_left(equation_nospaces,1)[0]
		return(answer)
	print("part2")

	answers = []
	for i in range(len(inputlist)):
		print(solveequation2(inputlist[i]))
		answers.append(solveequation2(inputlist[i]))
	
	print(answers)
	p2 = sum(answers)




print("Part 1:",p1)
print("Part 2:",p2)