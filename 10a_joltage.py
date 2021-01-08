
# return list of lists of consecutive items (difference of {1,2} or 3)
def jolt_split(input_list):

    return_list = []
    ones_list = []
    threes_list = []
    on_ones = True
    previous_num = 0

    for this_num in input_list: 
        difference = this_num - previous_num

        if difference in (1,2):
            if not on_ones:
                return_list.append(threes_list)
                threes_list = []
                on_ones = True
            ones_list.append(this_num)

        elif difference == 3:
            if on_ones:
                return_list.append(ones_list)
                ones_list = []
                on_ones = False
            threes_list.append(this_num)

        else:  
            print("bad diff")
            break
    
        previous_num = this_num

    # stick the remaining list on
    if on_ones:
        return_list.append(ones_list)
    else:
        return_list.append(threes_list)

    return return_list

    
def jolt_out(input_list):
    return_list = []
    ones = input_list[0::2]
    threes = input_list[1::2]

    print("ones")
    print(ones)

    total = 1

    for thing in ones:
        # multiplier = 99

        if len(thing) == 4:
            multiplier = 7
        elif len(thing) == 3:
            multiplier = 4
        elif len(thing) == 2:
            multiplier = 2
        elif len(thing) == 1:
            multiplier = 1

        print(thing, multiplier)

        total = total * multiplier
    print(total)




adapter_list = [int(line) for line in open("input", "r").readlines()]
adapter_list.sort()

print(f"Adapter list: {adapter_list}")

jolt_out(jolt_split(adapter_list))
