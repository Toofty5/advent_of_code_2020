lines = open("input", 'r').readlines()


entries = [] 

# Needs cleaning up: 

this_line = (lines.pop()).rstrip()
while len(lines) > 0:

    this_entry = {}
    while this_line != '':
        line_fields = this_line.rsplit()
        
        for field in line_fields:
            key, value = field.rsplit(':')
            this_entry[key] = value  # there's got to be a better way

        if(len(lines) > 0):
            this_line =(lines.pop()).rstrip()
        else:
            this_line = ''

        this_entry = {key:val for (key, val) for field.split(':') in this_line.split()}

    print(this_entry)
    entries.append(this_entry)


    if(len(lines) > 0):
        this_line =(lines.pop()).rstrip()

num_valid = 0
for entry in entries:
    valid_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    if valid_fields.issubset(set(entry.keys())):
        num_valid += 1
print(len(entries))
print (num_valid)
