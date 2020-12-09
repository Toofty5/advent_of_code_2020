num_list = list(enumerate([int(line) for line in open("input", "r").readlines()]))

pointer = 25

for i, this_num in num_list[25:]:
    match = False
    # slice of the previous 25
    for j, first_num in num_list[i-25:i]:

        # iterate through the rest of the numbers

        for k, second_num in num_list[j+1:i]:
            if first_num + second_num == this_num:
                match = True
                # print("match!")
                break


    if not match:
        print(this_num)
