import re


raw_file = open("input", 'r').read().split('mask = ')[1:]

values ={} 

for text_block in raw_file:
    lines = [line.strip() for line in text_block.split('\n')]
    mask_string = lines[0]

    ## AND this to val first to zero anything that needs changing.
    mask_mask = int("".join(['1' if char == 'X' else '0' for char in mask_string]), 2)

    ## zero the X's.  OR this after masking
    mask_normalized = int(''.join([char if char != 'X' else '0' for char in mask_string]), 2)


    for line in lines[1:-1]:
        command = re.match(r"mem\[(\d+)\] = (\d+)", line)
        st_dest, st_val = command.group(1,2)
        dest, val = int(st_dest), int(st_val)
        #print(dest, val)

        #print((val & mask_mask) | mask_normalized)

        values[dest] = (val & mask_mask )| mask_normalized

print(sum(values.values()))





