passes = [line.rstrip() for line in open('input').readlines()]

bin_passes = []
for entry in passes:
    bin_entry = entry.replace('F', '0').replace('B', '1').replace('L',
            '0').replace('R', '1')
    bin_passes.append(bin_entry)


int_passes = []

for entry in bin_passes:
    int_passes.append(int(entry, 2))


print(max(int_passes))

print([seat for seat in range(min(int_passes),max(int_passes)) if seat not in int_passes])
