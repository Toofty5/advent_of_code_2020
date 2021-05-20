#return list of 3
def cup_slice(number):
    this_number = linked_list[number]
    this_list = []
    for i in range(3):
        this_list.append(this_number)
        this_number = linked_list[this_number]

    return(this_list)

def offset(start, hops):
    here = start
    next_here = linked_list[here]

    for i in range(hops):
        here = next_here
        next_here = linked_list[here]

    return here

def print_list():
    here = 1

    out = []

    for i in range(9):
        out.append(here)
        here = linked_list[here]
    print(out)




input_list = [int(char) for char in '685974213']
input_list.extend(list(range(10, 1000001)))

linked_list = {}

for i, thing in enumerate(input_list):
    if i == len(input_list) - 1:
        linked_list[thing] = input_list[0]
    else:
        linked_list[thing] = input_list[i+1]

current_cup = input_list[0]

for i in range(10000000):
    if i % 10000 == 0:
        print(i)
    slice_head = linked_list[current_cup]
    slice_tail = linked_list[offset(current_cup, 2)]

    dest_cup = current_cup - 1
    this_slice = cup_slice(current_cup)

    while dest_cup in this_slice or dest_cup == 0:
        dest_cup = (dest_cup - 1) % 1000001

    linked_list[current_cup] = offset(current_cup, 4)
    linked_list[slice_tail] = linked_list[dest_cup]
    linked_list[dest_cup] = slice_head

    current_cup = linked_list[current_cup]

print_list()    



    
