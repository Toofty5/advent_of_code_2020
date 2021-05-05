import numpy as np

tile_strings = [block.strip() for block in open("input", "r").read().split("\n\n")]

tile_dict = {}

for tile_string in tile_strings:

    tile_lines = tile_string.split('\n')
    first_line = tile_lines.pop(0)

    tile_num = int(first_line[5:9])
    
    line_list = []
    for line in tile_lines:
        line_list.append([char for char in line])

    tile_matrix = np.matrix(line_list)
    tile_dict[tile_num] = tile_matrix


#all we need are corners for now.  find tiles with no matches on two sides
corners = []
for tile_num, tile in tile_dict.items():
    print(tile_num)
    sides_matched = 0

    #for each side in first tile
    for i in range(4):
        top_line = np.rot90(tile, k = i)[0]
        side_matched = False
        
        for check_tile_num, check_tile in tile_dict.items():
            #print(f"checking {tile_num} {check_tile_num}")
            if check_tile_num != tile_num:
                #for each side in second tile
                for j in range(4):
                    check_top_line = np.rot90(check_tile, k=j)[0]
                    if (check_top_line == top_line).all()\
                            or (check_top_line == np.flip(top_line)).all():
                        #print(f"Sides matched: ({tile_num} {i})({check_tile_num} {j})")
                        side_matched = True
            
        if side_matched:
            sides_matched += 1

    print(f'sides_matched: {sides_matched}')
    if sides_matched == 2:
        corners.append(tile_num)

print(corners)
print(np.product(corners))

print(len(tile_dict))

                    

           
