input_list = [int(char) for char in '685974213']

input_list = input_list + list(range(10,1000001))



current_cup = input_list[0] 
for i in range(1000000):
    # determine destination cup
    # get the index of current cup
    # reindex list to bring current cup to front
    # get pickup slice (3 right after current)
    # pull out pickup slice
    # make new current
    # if this destination works, get its index
    # drop the slice after the destination index

    dest_cup = current_cup - 1
    current_index = input_list.index(current_cup)
    input_list = input_list[current_index:] + input_list[:current_index]
    pickup = input_list[1:4]
    input_list = [input_list[0]] + input_list[4:]
    current_cup = input_list[1]
    


    while True:
        if(dest_cup in input_list):
            dest_index = input_list.index(dest_cup)+1
            break
        else:
            print(f"destination cup {dest_cup} not in list.")
            dest_cup = (dest_cup - 1) % 10

    
    input_list[dest_index:dest_index] = pickup


    print(i, current_cup, dest_cup)
    

start_index = input_list.index(1)
out_list = input_list[start_index:start_index+3] 
print(''.join([str(thing) for thing in out_list]))
breakpoint()
