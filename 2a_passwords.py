lines = [line.rstrip() for line in open("input").readlines()]
entries = [line.split() for line in lines]


valid_passwords = 0

for entry in entries:
	pos1, pos2 = map(int, entry[0].rsplit('-'))
	pos1, pos2 = pos1 - 1, pos2 - 1

	this_char = entry[1].rstrip(':')
	
	this_password = entry[2]

	check_chars = this_password[pos1], this_password[pos2]

	if check_chars[0] != check_chars[1] and this_char in check_chars:
		valid_passwords += 1
		print(check_chars)


print(valid_passwords)
