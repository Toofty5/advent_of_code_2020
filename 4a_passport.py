import re

lines = open("input", 'r').readlines()


entries = []

this_line = (lines.pop()).rstrip()
while len(lines) > 0:

    this_entry = {}
    while this_line != '':
        line_fields = this_line.rsplit()

        for field in line_fields:
            key, value = field.rsplit(':')
            this_entry[key] = value
        # print(this_entry)
        if(len(lines) > 0):
            this_line =(lines.pop()).rstrip()
        else:
            this_line = ''
    print(this_entry)
    entries.append(this_entry)


    if(len(lines) > 0):
        this_line =(lines.pop()).rstrip()

num_valid = 0
for entry in entries:
    valid_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    if valid_fields.issubset(set(entry.keys())):
        if not (re.match(r'[0-9]{4}',entry['byr']) and int(entry['byr']) in range(1920, 2003)):
            print(f"byr not valid {entry['byr']}")
            continue

        if not (re.match(r'[0-9]{4}',entry['iyr']) and int(entry['iyr']) in range(2010, 2021)):
            print(f"iyr not valid {entry['iyr']}")
            continue

        if not (re.match(r'[0-9]{4}',entry['eyr']) and int(entry['eyr']) in range(2020, 2031)):
            print(f"eyr not valid {entry['eyr']}")
            continue

        hgt_match = re.match(r'(\d*)(cm|in)', entry['hgt'])

        if not hgt_match:
            print(f"hgt not vaild {entry['hgt']}")
            continue

        elif (
               (hgt_match.group(2) == 'cm' and int(hgt_match.group(1)) not in range(150, 194)) or
               (hgt_match.group(2) == 'in' and int(hgt_match.group(1)) not in range(59, 77))
            ):
            print(f"hgt not valid {entry['hgt']}")
            continue

        if not( re.match("#[0-9a-f]{6}", entry['hcl'])):
            print(f"hcl not valid {entry['hcl']}")
            continue
        else:
            print(entry['hcl'])

        if entry['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            print(f"ecl not valid {entry['ecl']}")
            continue
        
        if not re.match('\d{9}', entry['pid']):
            print(f"not valid {entry['pid']}")
            continue
        else:
            print(entry['pid'])

        num_valid += 1

print(len(entries))
print (num_valid)
