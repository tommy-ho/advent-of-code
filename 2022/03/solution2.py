# O(n) solution using sets

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

    unique = set()

    for i in left:
        unique.add(i)
    
    for i in right:
        if i in unique:
            total += priorities[i]
            break

print(total)

# part 2

sum = 0

for r in range(0, len(rucksacks), 3):
    unique = set()
    unique2 = set()

    for i in rucksacks[r]:
        unique.add(i)
    
    for i in rucksacks[r+1]:
        if i in unique:
            unique2.add(i)
    
    for i in rucksacks[r+2]:
        if i in unique2:
            sum += priorities[i]
            break

print(sum)