# reading input
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

# part 1

mfcsam = {
    'children' : 3,
    'cats' : 7,
    'samoyeds' : 2,
    'pomeranians' : 3,
    'akitas' : 0,
    'vizslas' : 0,
    'goldfish' : 5,
    'trees' : 3,
    'cars' : 2,
    'perfumes' : 1
}

sues = {}

for line in lines:
    line = line.replace(':', '')
    line = line.replace(',', '')
    split = line.split(' ')
    id = int(split[1])
    sues[id] = {
        split[2] : int(split[3]),
        split[4] : int(split[5]),
        split[6] : int(split[7]),
    }

ans = None

for sue in sues:
    current = sues[sue]
    matches = 0
    for clue in mfcsam:
        print(clue)
        if clue not in current:
            matches += 1 # default to match if detail not remembered
        elif current[clue] == mfcsam[clue]:
            matches += 1
        else:
            break
    if matches == len(mfcsam):
        ans = sue
        break

print(ans)

# part 2

ans = None

for sue in sues:
    current = sues[sue]
    matches = 0
    for clue in mfcsam:
        print(clue)
        if clue not in current:
            matches += 1 # default to match if detail not remembered
        elif clue in ['cats', 'trees'] and current[clue] > mfcsam[clue]:
            matches += 1
        elif clue in ['pomeranians', 'goldfish'] and current[clue] < mfcsam[clue]:
            matches += 1
        elif current[clue] == mfcsam[clue]:
            matches += 1
        else:
            break
    if matches == len(mfcsam):
        ans = sue
        break

print(ans)
