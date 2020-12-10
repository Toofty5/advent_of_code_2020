enum_list = list(enumerate([int(line) for line in open("input", "r").readlines()]))

bad_num = 3199139634

for i, num1 in enum_list:
    for j, num2 in enum_list[i+1:]:
        this_list = [num for k, num in enum_list[i:j+1]]
        this_sum = sum(this_list)

        if this_sum == bad_num:
            print(i, j)
            print(min(this_list), max(this_list), min(this_list) +
                    max(this_list))
            print(this_sum)
            print(this_list)

        if this_sum > bad_num:
            break
