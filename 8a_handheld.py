lines = [line.strip() for line in open("input", "r").readlines()]

for line_num, line in enumerate(lines):

    swap_command, swap_val_str = line.split()

    if swap_command == "nop":
        lines[line_num] = "jmp " + swap_val_str
    if swap_command == "jmp":
        lines[line_num] = "nop " + swap_val_str

    visited = []
    accumulator = 0


    pointer = 0;

    while pointer not in visited:
        if pointer >= len(lines):
            print(f"End of commands.  Accumulator: {accumulator}")
            break

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

    # put the command back
    if swap_command == "nop":
        lines[line_num] = "nop " + swap_val_str
    if swap_command == "jmp":
        lines[line_num] = "jmp " + swap_val_str




