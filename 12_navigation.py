import math

def main():
    lines = [line.strip() for line in open("input", "r").readlines()]

    commands = [(line[0], int(line[1:])) for line in lines]

    heading = 0  # ENWS
    x = 0
    y = 0
    
    for comm, val in commands:
        if comm == "N":
            y += val
        elif comm == "S":
            y -= val
        elif comm == "E":
            x += val
        elif comm == "W":
            x -= val


        elif comm == "F":
            
            x += int(math.cos(math.radians(heading))) * val
            y += int(math.sin(math.radians(heading))) * val

            print(int(math.sin(math.radians(heading))), int(math.cos(math.radians(heading))))

        elif comm == "L":
            heading = (heading + val) % 360
        elif comm == "R":
            heading = (heading - val) % 360

    print(x, y)
    print(abs(x) + abs(y))

        





if __name__ == "__main__":
    main()
