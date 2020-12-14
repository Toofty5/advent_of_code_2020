def print_list(in_list):
    for thing in in_list:
        print(thing)


input_lines = [line.rstrip() for line in open("input", "r").readlines()]
HEIGHT = len(input_lines)
WIDTH = len(input_lines[0])

previous_seating = input_lines
this_seating = None
this_iteration = 0

while previous_seating != this_seating :
    this_seating = []

    for i, row in enumerate(previous_seating):
        this_row = [] 
        for j, char in enumerate(row):

            if char == '.':
                this_row.append('.')
            else:
                # 0 1 2 
                # 3   4
                # 5 6 7

                adjacencies = [-1] * 8 
                
                if i > 0:
                    for d, row_above in enumerate(reversed(previous_seating[:i])):
                        if adjacencies[1] == -1:
                            if row_above[j] == "#":
                                adjacencies[1] = 1
                            elif row_above[j] == "L":
                                adjacencies[1] = 0
                        if adjacencies[0] == -1:
                            if j-d-1 >= 0 and row_above[j-d-1] == "#":
                                adjacencies[0] = 1
                            elif j-d-1 >= 0 and row_above[j-d-1] == "L":
                                adjacencies[0] = 0

                        if adjacencies[2] == -1:
                            if j+d+1 < WIDTH and row_above[j+d+1] == "#":
                                adjacencies[2] = 1
                            elif j+d+1 < WIDTH and row_above[j+d+1] == "L":
                                adjacencies[2] = 0

                if i < HEIGHT -1:
                    for d, row_below in enumerate(previous_seating[i+1:]):
                        if adjacencies[6] == -1:
                            if row_below[j] == "#":
                                adjacencies[6] = 1
                            elif row_below[j] == "L":
                                adjacencies[6] = 0

                        if adjacencies[5] == -1:
                            if j-d-1 >= 0 and row_below[j-d-1] == "#":
                                adjacencies[5] = 1
                            elif j-d-1 >= 0 and row_below[j-d-1] == "L":
                                adjacencies[5] = 0


                        if adjacencies[7] == -1:
                            if j+d+1 < WIDTH and row_below[j+d+1] == "#":
                                adjacencies[7] = 1
                            elif j+d+1 < WIDTH and row_below[j+d+1] == "L":
                                adjacencies[7] = 0

                for left_char in reversed(previous_seating[i][:j]):
                    if left_char == "#":
                        adjacencies[3] = 1
                        break
                    elif left_char == "L":
                        adjacencies[3] = 0
                        break

                for right_char in previous_seating[i][j+1:]:
                    if right_char == "#":
                        adjacencies[4] = 1
                        break
                    elif right_char == "L":
                        adjacencies[4] = 0
                        break

                total_adjacent = adjacencies.count(1)

                if char == 'L' and total_adjacent == 0:
                    this_row.append('#')
                elif char == '#' and total_adjacent >= 5:
                    this_row.append("L")
                else:
                    this_row.append(char)


        this_seating.append(''.join(this_row))

    this_iteration += 1

    print(this_iteration)
    
    print_list(this_seating)

    occupied = 0
    for row in this_seating:
        occupied += row.count("#")
    print(occupied)


    if previous_seating == this_seating:
        break
    else:
        previous_seating = this_seating
        this_seating = []
