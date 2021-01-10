import re

# yes, this is a mess
[text_fields, text_your_ticket, text_nearby_tickets] = open("input", "r").read().strip().split("\n\n")


# fields = [ list(map(int, (re.match(r".+: (\d+)-(\d+) or (\d+)-(\d+)", line)).groups())) for line in text_fields.split("\n")]
fields_dict = {}
for line in text_fields.strip().split("\n"):
    groups = re.match("(.+): (\d+)-(\d+) or (\d+)-(\d+)", line.strip()).groups()
    name = groups[0]
    ranges = tuple(map(int, groups[1:]))

    fields_dict[name] = ranges


your_ticket = [int(thing) for thing in text_your_ticket.strip().split("\n")[1].split(",")]
nearby_tickets = [list(map(int, line.split(","))) for line in text_nearby_tickets.split("\n")[1:]]

valid_tix = []
invalid_tix = []

for ticket in nearby_tickets:
    field_tracker = []
    valid_ticket = False

    for item in ticket:    
        possible_fields = set()
        for field_name, (from1, to1, from2, to2) in fields_dict.items():
            if item in range(from1, to1+1) or item in range(from2, to2+1):
                possible_fields.add(field_name)

        if possible_fields != set():
            field_tracker.append(possible_fields)
            valid_ticket = True
        else:
            # print("invalid item", item)
            valid_ticket = False
            break

    if valid_ticket:
        valid_tix.append(ticket)
    else:
        invalid_tix.append(ticket)

columns = []
for i in range(len(valid_tix[0])):
    this_col = []
    for j in range(len(valid_tix)):
        this_col.append(valid_tix[j][i])
    columns.append(this_col)

field_sets = [] 
for col in columns:
    possible_fields = fields_dict.copy()

    for item in col:
        for field_name, (from1, to1, from2, to2) in fields_dict.items():
            if item not in range(from1, to1+1) and item not in range(from2, to2+1):
                possible_fields.pop(field_name)

    field_sets.append(set(possible_fields))


final_sets = list(enumerate(field_sets))

final_sets.sort(key=lambda this_set: len(this_set[1]))

final_fields = [final_sets[0]]
for i, line in list(enumerate(final_sets))[1:]:
    final_fields.append((line[0], line[1].difference(final_sets[i-1][1])))

final_fields.sort(key=lambda line:line[0])

for i, thing in enumerate(final_fields):
    print(thing, your_ticket[i])

