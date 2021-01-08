def main():
    
    lines = [line.strip() for line in open("input", "r").readlines()]

    commands = [(line[0], int(line[1:])) for line in lines]

    wp_heading = 0  # ENWS
    wp_x = 10
    wp_y = 1
    
    ship_heading = 0  # ENWS
    ship_x = 0
    ship_y = 0

    for comm, val in commands:
        if comm == "N":
            wp_y += val
        elif comm == "S":
            wp_y -= val
        elif comm == "E":
            wp_x += val
        elif comm == "W":
            wp_x -= val

        elif (comm, val) in [("L", 90),("R", 270)]:
            wp_x, wp_y = -wp_y, wp_x


        elif (comm, val) in [("R", 90),("L", 270)]:
            wp_x, wp_y = wp_y, -wp_x

        elif val == 180 and (comm in "LR"):
            wp_x, wp_y = -wp_x, -wp_y

        elif comm == "F":
            ship_x += wp_x * val
            ship_y += wp_y * val


    print(ship_x, ship_y)
    print(abs(ship_x) + abs(ship_y))

        





if __name__ == "__main__":
    main()
