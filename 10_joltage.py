adapter_list = [int(line) for line in open("input", "r").readlines()]
adapter_list.sort()
print(adapter_list)

one_diff = 0
three_diff = 0

for i, adapter in enumerate(adapter_list):
    if(i+1 < len(adapter_list)):
        print(adapter_list[i+1], adapter)
        difference = adapter_list[i+1] - adapter

    if difference == 1:
        one_diff += 1
    elif difference == 3:
        three_diff += 1
    else:
        print(difference)

three_diff += 1
print(one_diff + three_diff)
print (one_diff, three_diff, one_diff * three_diff)
