lines = [line.rstrip() for line in open("input").readlines()]

trees = 0;
x_pos = 0;


for line in  [line for (i, line) in enumerate(lines) if i % 2 == 0 ] :
    if(line[x_pos % len(line)]) == '#':
        trees += 1

    x_pos += 1

print(trees)
