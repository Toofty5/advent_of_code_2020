lines = [line.strip() for line in open("input", "r").readlines()]

visited = []
accumulator = 0


pointer = 0;

while pointer not in visited:
    visited.append(pointer)
    
    command, val_str = lines[pointer].split()

    val = int(val_str)

    if command == "nop":
        pointer += 1
    elif command == "acc":
        accumulator += val
        pointer += 1
    elif command == 'jmp':
        pointer += val
    else:
        print("what")
print(accumulator)




