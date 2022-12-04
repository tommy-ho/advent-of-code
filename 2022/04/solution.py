# reading input
f = open('input.txt', 'r')
lines = f.readlines()
assignments = [i.strip() for i in lines]
f.close()

# part 1

ans = 0

for pair in assignments:
    split = pair.split(',')
    elf1 = split[0].split('-')
    elf2 = split[1].split('-')

    elf1 = [int(i) for i in elf1]
    elf2 = [int(i) for i in elf2]

    if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or \
    (elf2[0] <= elf1[0] and elf2[1] >= elf1[1]):
        ans += 1

print(ans)


# part 1

ans = 0

for pair in assignments:
    split = pair.split(',')
    elf1 = split[0].split('-')
    elf2 = split[1].split('-')

    elf1 = [int(i) for i in elf1]
    elf2 = [int(i) for i in elf2]

    if elf1[0] <= elf2[0] <= elf1[1] or \
    elf1[0] <= elf2[1] <= elf1[1] or \
    elf2[0] <= elf1[0] <= elf2[1] or \
    elf2[0] <= elf1[1] <= elf2[1]:
        ans += 1

print(ans)