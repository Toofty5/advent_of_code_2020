enum_list = list(enumerate([int(line) for line in open("input", "r").readlines()]))

bad_num = 3199139634

for i, num1 in enum_list:
    for j, num2 in enum_list[i+1:]:
        this_sum = sum([num for k, num in enum_list[i:j+1]])

        if this_sum == bad_num:
            print(i, j)
            print(num1, num2, num1+num2)
            print(this_sum)
            print([num for k, num in enum_list[i:j+1]])

        if this_sum > bad_num:
            break
