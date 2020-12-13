input_lines = [line.rstrip() for line in open("input", "r").readlines()]
HEIGHT = len(input_lines)
WIDTH = len(input_lines[0])

previous_seating = input_lines
this_seating = None
this_iteration = 0

while previous_seating != this_seating:
    this_seating = []

    for i, row in enumerate(previous_seating):
        this_row = [] 
        for j, char in enumerate(row):

            if char == '.':
                this_row.append('.')
            else:

                total_adjacent = 0

                # to do: condense all of this into a boolean list

                if i > 0: # UP
                    if previous_seating[i-1][j] == '#':
                        total_adjacent += 1
                    if j > 0 and previous_seating[i-1][j-1] == "#":
                        total_adjacent += 1
                    if j < WIDTH -1 and previous_seating[i-1][j+1] == "#":
                        total_adjacent += 1

                if i < HEIGHT - 1:
                    if previous_seating[i+1][j] == "#": # DOWN
                        total_adjacent += 1
                    if j > 0 and previous_seating[i+1][j-1] == "#":
                        total_adjacent += 1
                    if j < WIDTH -1 and previous_seating[i+1][j+1] == "#":
                        total_adjacent += 1

                if j > 0 and previous_seating[i][j-1] == "#": # LEFT
                    total_adjacent += 1
                if j < WIDTH - 1 and previous_seating[i][j+1] == "#": #RIGHT
                    total_adjacent += 1

                if char == 'L' and total_adjacent == 0:
                    this_row.append('#')
                elif char == '#' and total_adjacent >= 4:
                    this_row.append("L")
                else:
                    this_row.append(char)


        this_seating.append(''.join(this_row))
    this_iteration += 1

    print(this_iteration)
    # for row in this_seating:
    #     print(row)

    if previous_seating == this_seating:
        break
    else:
        previous_seating = this_seating
        this_seating = []
   
occupied = 0
for row in this_seating:
    occupied += row.count("#")
print(occupied)
