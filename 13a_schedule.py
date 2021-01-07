timestamp, second_line = [line.strip() for line in open("input",
    "r").readlines()]

timestamp = int(timestamp)

bus_lines = second_line.split(',')

open_lines = [thing if "x" else int(thing) for thing in bus_lines]

offset_lines = [(x, int(y)) for (x,y) in enumerate(open_lines) if y != "x"]

zero_offset, this_bus = offset_lines[0]
this_time = this_bus
this_jump = this_bus

print(offset_lines)

for next_offset, next_bus in offset_lines[1:]:
    while True:
        if (this_time + next_offset) % next_bus == 0:
            print(this_time)
            this_jump = this_jump * next_bus
            break
        this_time += this_jump

            
