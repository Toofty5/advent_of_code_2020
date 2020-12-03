
# removed .txt extension from windows
input_file = open("input", 'r')

"""
entries = []

this_line = input_file.readline().rstrip()

while this_line != '':
    entries.append(int(this_line));
    this_line = input_file.readline().rstrip()
"""

# changed up the file input for some list comprehension fun
entries = [int(line) for line in input_file.readlines()]

# Since we only traverse once, using pop instead of keeping a pointer
while entries != []:
    this_number = entries.pop(0);
    for other_number in entries:
        if this_number + other_number == 2020:
            print(this_number * other_number)


