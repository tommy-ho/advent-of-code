import re

# reading input
f = open('input.txt', 'r')
lines = f.readlines()
lines = [i.strip() for i in lines]
f.close()

# part 1

replacement = {}

for line in lines:
    if '=>' in line:
        split = line.split(' => ')
        if split[0] in replacement:
            replacement[split[0]].append(split[1])
        else:
            replacement[split[0]] = [split[1]]
    elif len(line) > 0:
        start = line

distinct = set()

for key in replacement: # start element
    iter = re.finditer(key, start)
    for i in iter: # every occurence in molecule
        for new_element in replacement[key]: # every possibly replacement
            new_molecule = start[:i.start()] + new_element + start[i.end():]
            distinct.add(new_molecule)


print(len(distinct))

# part 2

distinct = set()
used = set()
distinct.add('e')
steps = 0

while start not in distinct:
    new_distinct = set()
    for molecule in distinct:
        for key in replacement: # start element
            iter = re.finditer(key, molecule)
            for i in iter: # every occurence in molecule
                for new_element in replacement[key]: # every possibly replacement
                    new_molecule = molecule[:i.start()] + new_element + molecule[i.end():]
                    if new_molecule not in used and new_molecule not in distinct:
                        new_distinct.add(new_molecule)
    steps += 1
    used.update(distinct)
    distinct = new_distinct

print(steps)