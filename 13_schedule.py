timestamp, second_line = [line.strip() for line in open("input",
    "r").readlines()]

timestamp = int(timestamp)

bus_lines = second_line.split(',')

open_lines = [int(thing) for thing in bus_lines if thing != 'x']
print(timestamp)
print(open_lines)
open_lines.sort(key=lambda line:line - (timestamp % line))


for thing in open_lines:
    print(thing, thing - (timestamp % thing))




print(open_lines)
