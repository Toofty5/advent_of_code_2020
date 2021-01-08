import re

def bin_out(int_in):
    return bin(int_in)[2:].zfill(36)

def float_out(bitmask): # list of all the possible masks
    floated_bits = []
    bit_string  = bin(bitmask)[2:].zfill(36)
    
    ones = []
    for i, char in enumerate(bit_string[::-1]):
        if char == '1':
            ones.append(i)
    for i in range(2**len(ones)):

        this_mask = 0
        for j, offset in enumerate(ones):
            mask = 1 << offset
            new_mask = (i << offset - j) & mask
            this_mask = this_mask | new_mask

        floated_bits.append(this_mask)

    return(floated_bits)


raw_file = open("input", 'r').read().split('mask = ')[1:]

values ={} 

for text_block in raw_file:
    lines = [line.strip() for line in text_block.split('\n')]
    mask_string = lines[0]

    ## every X
    mask_mask = int("".join(['1' if char == 'X' else '0' for char in mask_string]), 2)

    ## zero the X's, leave the rest
    mask_normalized = int(''.join([char if char != 'X' else '0' for char in mask_string]), 2)

    ## mask for the dest address
    dest_mask = int("".join(['0' if char == 'X' else '1' for char in mask_string]), 2)

    floated_masks = float_out(mask_mask)

    print("---------------")
    print(mask_string)
    print(bin_out(mask_mask))
    print(bin_out(mask_normalized))
    print("---------------")

    for line in lines[1:-1]:
        command = re.match(r"mem\[(\d+)\] = (\d+)", line)
        st_dest, st_val = command.group(1,2)
        dest, val = int(st_dest), int(st_val)

        print(bin_out(dest), val)

        for mask in floated_masks:
            # print(bin_out(mask | mask_normalized))

            address = (mask | mask_normalized) | (dest & dest_mask )
            #if address in values.keys():
            #    print("replacing", address )
            print(bin_out(address))
            values[address] = val

print(sum(values.values()))
