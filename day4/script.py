import math

with open("input.txt") as f:
	inpt = f.readlines()

lines = 0
passports = []
temp = ''

blanks = 0

for i in range(len(inpt)):
	if len(inpt[i]) > 2:
		temp = temp + inpt[i]
	if inpt[i] == '\n' or i == len(inpt)-1:
		blanks = blanks + 1
		passports.append(temp)
		temp = ''

matches = 0
optionals = 0
fails = 0

part2 = []

for p in passports:
	try:
		if 'byr' in p and 'eyr' in p and 'iyr' in p and 'hgt' in p and 'hcl' in p and 'ecl' in p and 'pid' in p and 'cid' not in p:
			matches = matches + 1
			part2.append(p)
		elif 'byr' in p and 'eyr' in p and 'iyr' in p and 'hgt' in p and 'hcl' in p and 'ecl' in p and 'pid' in p and 'cid' in p:
			optionals = optionals + 1
			part2.append(p)
		else:
			fails = fails + 1
	except IndexError:
		continue

print("part 1 : ",matches + optionals)


for i in range(len(part2)):
	part2[i] = part2[i].replace('\n', ' ').split()

valids = 0
falses = 0
count = 0

for p in part2:
	valid = True
	for params in p:
		key = params[:3]
		value = params[4:]
		if key == "byr":
			if int(value) >= 1920 and int(value) <= 2002:
				continue
			else:
				falses = falses + 1
				valid = False
				break
		if key == "iyr":
			if int(value) >= 2010 and int(value) <= 2020:
				continue
			else:
				falses = falses + 1
				valid = False
				break
		if key == "eyr":
			if int(value) >= 2020 and int(value) <= 2030:
				continue
			else:
				falses = falses + 1
				valid = False
				break
		if key == "hgt":
			if value[-2:] == "cm":
				if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
					continue
				else:
					falses = falses + 1
					valid = False
					break
			if value[-2:] == "in":
				if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
					continue
				else:
					falses = falses + 1
					valid = False
					break
		if key == 'hcl':
			#try:
			if value[0] == '#':
				try:
					if int(value[1:], 16):
						continue
				except ValueError:
					falses = falses + 1
					valid = False
					break
			else:
				falses = falses + 1
				valid = False
		if key == "ecl":
			if len(value) == 3:
				if "blu" in value or "amb" in value or "brn" in value or "gry" in value or "grn" in value or "hzl" in value or "oth" in value:
					continue
				else:
					falses = falses + 1
					valid = False
					break
			else:
				falses = falses + 1
				valid = False
				break
		if key == "pid":
			try:
				if int(value):
					if len(value) == 9:
						continue
					else:
						falses = falses + 1
						valid = False
						break
				else:
					falses = falses + 1
					valid = False
					break
			except ValueError:
				falses = falses + 1
				valid = False
				break
		if key =="cid":
			continue
		else: 
			#this is the final thing I needed to get it working correctly. Check for valid key names.
			valid = False
			break
	#still valid? add it up
	if valid:
		valids = valids + 1
	#print("passport# : ",count, " valid# : ",valids," fail# ", falses)
	count = count + 1
#print("invalids : ", falses)
print("part 2: ",valids)

#wrong answer log :( 196. 121. 151. 45. 65. 143. 133
