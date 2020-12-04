import math

with open("input.txt") as f:
	inpt = f.readlines()

inpt = [x.strip() for x in inpt]

valid = 0



#part1
for p in inpt:
	occurences = p.split(' ')[0]
	letter = p.split(' ')[1]
	password = p.split(' ')[2]
	low = int(occurences.split('-')[0])
	high = int(occurences.split('-')[1])
	#print(p)
	count = 0
	for l in password:


		if l == letter[:1]:
			count = count + 1
	#print(count)

	if count in range(low, high+1):
		#print("testing : ",p," Letter : ",letter[:1]," Count : ",count," between ", low," and ", high)
		valid = valid + 1
		#print(valid)
print("Part 1", valid)

valid = 0
#part2
for p in inpt:
	occurences = p.split(' ')[0]
	letter = p.split(' ')[1]
	password = p.split(' ')[2]
	low = int(occurences.split('-')[0])
	high = int(occurences.split('-')[1])
	#print(p)
	count = 0

	if high <= len(password):
		if (password[low-1] == letter[:1] and password[high-1] != letter[:1]) or (password[low-1] != letter[:1] and password[high-1] == letter[:1]):
			#print("** SUCCESS ** password length : ", len(password),"high : ",high,"letter to test : ",letter," pos low : ", password[low-1], " pos high : ",password[high-1])
			valid = valid + 1
print("Part 2", valid) 
