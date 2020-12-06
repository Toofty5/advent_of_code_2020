groups = [group.rsplit('\n') for group in open("input", 'r').read().rsplit("\n\n")]

total = 0
for group in groups:
    group_answers = set(''.join(group))
    total += len(group_answers)

print(total)

