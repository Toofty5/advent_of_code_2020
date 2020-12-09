num_list = list(enumerate([int(line) for line in open("input", "r").readlines()]))

bad_num = 3199139634

for i, low_num in num_list:
    this_sum = low_num

    for j, high_num in num_list[i+1:]:
        this_sum += high_num
        if this_sum == bad_num:
            print(i, low_num)
            print(j, high_num)
            break

        if this_sum > bad_num:
            break

print(sum(number for (x,number) in num_list[562:578]))
