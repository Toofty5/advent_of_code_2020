input_file = open("input.txt", 'r')

entries = []

this_line = input_file.readline().rstrip()

while this_line != '':
    entries.append(int(this_line));
    this_line = input_file.readline().rstrip()

my_list = [x*y*z for x in entries for y in entries for z in entries if x+y+z == 2020]

print(my_list)

    




