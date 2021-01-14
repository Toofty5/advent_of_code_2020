import numpy as np

def neighbors(index_z, index_y, index_x):
    # index_z += padding
    # index_x += padding
    # index_y += padding

    check_view = pocket_array[index_z-1:index_z+2 , index_y-1:index_y+2 ,
            index_x-1: index_x+2]
    # print(check_view)
    return np.count_nonzero(check_view) - check_view[1,1,1]
    


in_file = [line.strip() for line in open("input", "r").readlines()]

turns = 6
padding = turns + 2

width = len(in_file[0]) + (padding * 2) + 1
height = len(in_file) + (padding * 2) + 1
depth = 1 + (padding * 2)
fourth = 1 + (padding * 2)

pocket_array = np.zeros([fourth, depth, height, width])

for i, line in enumerate(in_file):
    for j, char in enumerate(line):
        if char == '#':
            pocket_array[padding, padding, j+padding, i+padding] = 1
        else:
            pocket_array[padding, padding, j+padding, i+padding] = 0




new_array = np.zeros(pocket_array.shape)

active_indices = []
print(fourth, depth, height, width)
print(pocket_array.shape)

for i in range(0, turns):
    for (z,y,x), val in np.ndenumerate(pocket_array):
        if (z in range(1, depth - 1) and
            y in range(1, height - 1) and
            x in range(1, width - 1)):
            this_neighbors = neighbors(z,y,x)
            if val and this_neighbors in [2,3]:
                    new_array[z,y,x] = 1
            elif not val and this_neighbors == 3:
                    new_array[z,y,x] = 1
    pocket_array = new_array
    new_array = np.zeros(pocket_array.shape)

    print(i, np.count_nonzero(pocket_array))
    # print(pocket_array[padding])
