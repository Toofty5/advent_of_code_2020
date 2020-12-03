input_file = open("input.txt", 'r')

entries = []

this_line = input_file.readline().rstrip()

while this_line != '':
    entries.append(int(this_line));
    this_line = input_file.readline().rstrip()

while entries != []:
    this_number = entries.pop(0);
    for other_number in entries:
        if this_number + other_number == 2020:
            print(this_number * other_number)


