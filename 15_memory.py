numbers = [2,15,0,9,1,20]
numbers.reverse()

while len(numbers) < 2020:
    last_num = numbers[0]

    try:
        index = numbers[1:].index(last_num) + 1
    except ValueError:
        numbers.insert(0,0)
        continue
    numbers.insert(0, index)

    print(len(numbers), numbers[0])

    
