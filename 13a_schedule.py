timestamp, second_line = [line.strip() for line in open("input",
    "r").readlines()]

timestamp = int(timestamp)

bus_lines = second_line.split(',')

open_lines = [int(thing) for thing in bus_lines if thing != 'x']
print(open_lines)

product = 1
for thing in open_lines:
    product = product * thing
print(product)
