groups = [group.rsplit('\n') for group in open("input", 'r').read().rsplit("\n\n")]

total = 0
for group in groups:
    group_answers = set.intersection(*[set(entry) for entry in group])
    print(group_answers)
    total += len(group_answers)

print(total)



