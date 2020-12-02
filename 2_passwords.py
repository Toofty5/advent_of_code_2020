lines = [line.rstrip() for line in open("input").readlines()]
entries = [line.split() for line in lines]


valid_passwords = 0

for entry in entries:
	char_min, char_max = map(int, entry[0].rsplit('-'))
	this_char = entry[1].rstrip(':')
	
	this_password = entry[2]

	count = this_password.count(this_char)
	if count >= char_min and count <= char_max:
		valid_passwords += 1
		print(this_password)

print(valid_passwords)
