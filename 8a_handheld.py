

def init():

    global lines, visited, stack, accumulator, pointer, in_loop

    lines = [line.strip() for line in open("input", "r").readlines()]

    visited = []

    stack = []
    accumulator = 0
    in_loop = False;

    pointer = 0;

def main():
    global lines, visited, stack, accumulator, pointer, in_loop
    init()

    while visited.count(pointer) < 1:

        if pointer in visited:
            print(pointer)
        visited.append(pointer)
        
        command, val_str = lines[pointer].split()

        val = int(val_str)

        if(pointer == 267):
            in_loop = True

        if in_loop:
            stack.append((pointer, command, val))

        # print(command, val)

        if command == "nop":
            pointer += 1
        elif command == "acc":
            accumulator += val
            pointer += 1
        elif command == 'jmp':
            pointer += val
        else:
            print("what")

    print(f"pointer {pointer}")
    print(f"line {lines[pointer]}")
     
# print(f"accumulator {accumulator}")
# print(len(stack))

    for com in stack:
        print(com)

if __name__ == "__main__":
    main()
