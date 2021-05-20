import re
ADJACENCIES_ODD = [(1,-1), (0, -1), (-1, 0), (1, 0), (1, 1), (0, 1)]
ADJACENCIES_EVEN = [(-1,-1), (0, -1), (-1, 0), (1, 0), (-1, 1), (0, 1)]

#return list of adjacent black tiles

def adjacent_black(tile):
    x, y = tile
    #odd-r adjacencies:
    out = []
    if y % 2 == 0:
        adjacencies = ADJACENCIES_EVEN
    else:
        adjacencies = ADJACENCIES_ODD

    for offset in adjacencies:
        off_x, off_y = offset
        if (x+off_x, y+off_y) in flipped:
            out.append((x+off_x, y+off_y))
    return out

def adjacent_white(tile):
    x, y = tile
    #odd-r adjacencies:
    out = []
    if y % 2 == 0:
        adjacencies = ADJACENCIES_EVEN
    else:
        adjacencies = ADJACENCIES_ODD

    for offset in adjacencies:
        off_x, off_y = offset
        if (x+off_x, y+off_y) not in flipped:
            out.append((x+off_x, y+off_y))
    return out


directions = [line.strip() for line in open('input', 'r').readlines()]
flipped = []

parsed = []

for line in directions:
    parsed.append([thing for thing in re.split('(s.|n.|[ew])', line) if thing is not ''])


for line in parsed:
    x = 0
    y = 0

    #odd-r coords
    for step in line:
        if step == 'nw':
            x += -1 + (y % 2)
            y -= 1
        elif step == 'ne':
            x += y % 2
            y -= 1
        elif step == 'sw':
            x += -1 + (y % 2)
            y += 1
        elif step == 'se':
            x += y % 2
            y += 1
        elif step == 'e':
            x += 1
        elif step == 'w':
            x -= 1
        else:
            print('wait, what?')

    if (x,y) in flipped:
        print(f"{x,y} is black.  flipping back")
        flipped.remove((x,y))
    else:
        flipped.append((x,y))

print(len(flipped))

for i in range(100):
    print(i, len(flipped))
    new_flip = []

    for tile in flipped:
        adjacent_b = adjacent_black(tile)
        adjacent_w = adjacent_white(tile)
        adjacencies_b = len(adjacent_b)

        #print(adjacent_b)
        #print(adjacent_w)

        if adjacencies_b == 0 or adjacencies_b > 2:
            new_flip.append(tile)

        for w_tile in adjacent_w:
            if w_tile not in new_flip and len(adjacent_black(w_tile)) == 2:
                new_flip.append(w_tile)

    for new_tile in new_flip:
        if new_tile in flipped:
            flipped.remove(new_tile)
        else:
            flipped.append(new_tile)

print(len(flipped))
