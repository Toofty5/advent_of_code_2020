import re

# yes, this is a mess
[text_fields, text_your_ticket, text_nearby_tickets] = open("input", "r").read().strip().split("\n\n")
fields = [ list(map(int, (re.match(r".+: (\d+)-(\d+) or (\d+)-(\d+)", line)).groups())) for line in text_fields.split("\n")]
your_ticket = [int(thing) for thing in text_your_ticket.strip().split("\n")[1].split(",")]
nearby_tickets = [list(map(int, line.split(","))) for line in text_nearby_tickets.split("\n")[1:]]

for field in fields:
    print(field)
#print(f"your ticket\n{your_ticket}")
#print(f"nearby tickets\n{nearby_tickets}")


valid_tix = []
total = 0

for ticket in nearby_tickets:

    for item in ticket:    
        valid = False
        
        for from1, to1, from2, to2 in fields:

            if item in range(from1, to1+1) or item in range(from2, to2+1):
                print(item)
                valid = True
                break
        if not valid:
            total += item


print(total)

