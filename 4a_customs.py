groups = [group.rsplit('\n') for group in open("input", 'r').read().rsplit("\n\n")]

for group in groups:
    group_answers = set.intersection(group)
    print(group_answers)

print(total)

