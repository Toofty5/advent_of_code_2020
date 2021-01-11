import numpy as np

def neighbors(z, y, x):
    z += padding
    x += padding
    y += padding

    check_view = pocket_array[z-1:z+2 , y-1:y+2 , x-1: x+2]
    print(pocket_array[turns])
    print(check_view)
    print(np.count_nonzero(check_view) - check_view[1,1,1])


in_file = [line.strip() for line in open("input", "r").readlines()]

turns = 6
padding = turns + 2

width = len(in_file[0]) + (padding * 2)
height = len(in_file) + (padding * 2)
depth = 1 + (turns * 2)

pocket_array = np.zeros([depth, width, height])

for i, line in enumerate(in_file):
    for j, char in enumerate(line):
        if char == '#':
            pocket_array[padding, i+padding, j+padding] = 1
        else:
            pocket_array[padding, i+padding, j+padding] = 0

for index, item in np.ndenumerate(pocket_array):
    print(index, item)
