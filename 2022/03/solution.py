# reading input
f = open('input.txt', 'r')
lines = f.readlines()
rucksacks = [i.strip() for i in lines]
f.close()

# part 1

priorities = {}

p = 1
for i in range(97,123):
    priorities[chr(i)] = p
    p += 1

for i in range(65,91):
    priorities[chr(i)] = p
    p += 1

total = 0
for rucksack in rucksacks:
    mid = int(len(rucksack) / 2)
    left = rucksack[:mid]
    right = rucksack[mid:]

    for i in left:
        matched = False
        for j in right:
            if i == j:
                total += priorities[i]
                matched = True
                break
        if matched:
            break

print(total)

# part 2

sum = 0

for r in range(0, len(rucksacks), 3):
    for i in rucksacks[r]:
        matched = False
        for j in rucksacks[r+1]:
            for k in rucksacks[r+2]:
                if i == j == k:
                    sum += priorities[i]
                    matched = True
                    break
            if matched:
                break
        if matched:
            break

print(sum)