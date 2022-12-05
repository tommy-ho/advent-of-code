# reading input
f = open('input.txt', 'r')
lines = f.readlines()
lines2 = lines.copy()
f.close()

# part 1

# construct the stacks

stacks = []

for i in range(1, len(lines[0]), 4):
    stacks.append([])

for line in lines:
    if line.startswith(' 1'):
        break
    stack_no = 0
    for i in range(1, len(line), 4):
        if line[i] != ' ':
            stacks[stack_no].insert(0, line[i])
        stack_no += 1


# executing the instructions

lines = [i.strip() for i in lines]

for line in lines:
    if not line.startswith('move'):
        continue
    split = line.split(' ')
    count = int(split[1])
    source = int(split[3]) - 1
    dest = int(split[5]) - 1

    for i in range(count):
        crate = stacks[source].pop()
        stacks[dest].append(crate)

ans = ''
for stack in stacks:
    ans += stack[-1]

print(ans)


# part 2

# construct the stacks

stacks = []

for i in range(1, len(lines2[0]), 4):
    stacks.append([])

for line in lines2:
    if line.startswith(' 1'):
        break
    stack_no = 0
    for i in range(1, len(line), 4):
        if line[i] != ' ':
            stacks[stack_no].insert(0, line[i])
        stack_no += 1


# executing the instructions

lines2 = [i.strip() for i in lines2]

for line in lines2:
    if not line.startswith('move'):
        continue
    split = line.split(' ')
    count = int(split[1])
    source = int(split[3]) - 1
    dest = int(split[5]) - 1

    crates = stacks[source][len(stacks[source])-count:]
    stacks[dest] += crates
    del stacks[source][-count:]

ans = ''
for stack in stacks:
    ans += stack[-1]

print(ans)