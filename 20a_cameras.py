import numpy as np


# put in a tuple of tile_num, tile_rotation

def tile(tile_tuple):
    tile_num, tile_rotation = tile_tuple
    this_tile = tile_dict[tile_num]
    
    if tile_rotation < 4:
        return np.rot90(this_tile, tile_rotation)
    else:
        return np.flipud(np.rot90(this_tile, tile_rotation-4))

def clean_tile(tile_tuple):
    return tile(tile_tuple)[1:9, 1:9]

    


tile_strings = [block.strip() for block in open("input", "r").read().split("\n\n")]

tile_dict = {}

for tile_string in tile_strings:

    tile_lines = tile_string.split('\n')
    first_line = tile_lines.pop(0)

    tile_num = int(first_line[5:9])
    
    line_list = []
    for line in tile_lines:
        line_list.append([char for char in line])

    tile_matrix = np.array(line_list)
    tile_dict[tile_num] = tile_matrix

# corners: [3221, 1447, 1873, 2029]
# start with 3221 as 0,0
# 144 total tiles; 12x12

# make an array of tuples, tile_num, orientation.

tile_array = np.empty([12,12], dtype=tuple)

tile_array[0][0] = (3221, 3)

# fill rest of the row
for i in range(1,12): 
    this_tile_num, this_rotation = tile_array[0][i-1]
    this_tile = tile((this_tile_num, this_rotation))
    this_right = np.rot90(this_tile)[0]

    for check_tile_num, check_tile in tile_dict.items():
        matched = False
        if check_tile_num != this_tile_num:
            check_tile = tile((check_tile_num, 0))
            for j in range(4):
                check_left = np.rot90(check_tile, k=j-1)[0]

                if (this_right == np.flip(check_left)).all():
                    tile_array[0][i] = (check_tile_num, j)
                    matched = True
                    break

                elif (this_right == check_left).all():
                    tile_array[0][i] = (check_tile_num, j+4)
                    matched = True
                    break
            

            if matched:
                # print(tile(*tile_array[0][i-1]), tile_array[0][i-1])
                # print(tile(*tile_array[0][i]), tile_array[0][i])

                break

#because I can't be bothered to figure out the math of flipping and rotating
H_FLIP = [6,7,4,5]  

#for tile_num, this_rotation in tile_array[0]:
#    this_tile = tile(tile_num, this_rotation)
#    print(tile_num, this_rotation)
#    print(this_tile)
#


# first row filled.  Build downwards.
for i in range(1,12):
    for j in range(0,12):
        this_tile_num, this_rotation = tile_array[i-1][j]
        this_tile = tile((this_tile_num, this_rotation))

        this_bottom = np.flipud(this_tile)[0]

        for check_tile_num in tile_dict.keys():
            matched = False
            if check_tile_num != this_tile_num:
                check_tile = tile((check_tile_num, 0))
                for r in range(4):
                    check_top = np.rot90(check_tile, k=r)[0]

                    if (this_bottom == check_top).all():
                        tile_array[i][j] = (check_tile_num, r)
                        matched = True
                    elif (np.flip(this_bottom) == check_top).all():
                        tile_array[i][j] = (check_tile_num, H_FLIP[r])
                        matched = True


            if matched:
                # print(tile(*tile_array[i-1][j]), tile_array[i-1][j])
                # print(tile(*tile_array[i][j]), tile_array[i][j])
                break
#print(tile_array)

cleaned_map = np.vstack([np.hstack(list(map(clean_tile, row))) for row in tile_array])

binary = lambda x: x == '#'
binary_map = np.array(list(map(binary, cleaned_map)))

# print(binary_map)

# for thing in binary_map:
#    print(thing)

# MONSTER
#                   #
# #    ##    ##    ###
#  #  #  #  #  #  #



monster_string = [char for char in '                  # #    ##    ##    ### #  #  #  #  #  #   ']

monster_mask = np.reshape(list(map(binary, monster_string)), (3,20))

r = 3
binary_view = np.rot90(binary_map, r)
count = 0
for i,j in [(i,j) for i in range(93) for j in range(76)]:
    check_window = binary_view[i:i+3, j:j+20]
    masked_window = np.logical_and(check_window, monster_mask)

    if (masked_window == monster_mask).all():
        print(f"Match found! {i},{j}")
        count += 1
print(count)
breakpoint()
