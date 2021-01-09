numbers = [2,15,0,9,1]

this_num = 20

count = len(numbers) + 1

num_dict = {}
for i, num in enumerate(numbers):
    print(i, num)
    num_dict[num] = i + 1

#print(num_dict)

while count <= 30000000:
    next_num = 0

    if this_num in num_dict:
        next_num = count - num_dict[this_num]

    num_dict[this_num] = count 
        

    if count % 100000 == 0:
        print(count, this_num)

    this_num = next_num

    count += 1                                                                                                                         
