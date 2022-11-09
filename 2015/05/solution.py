import re

# reading input
f = open('input.txt', 'r')
strings = f.readlines()
f.close()

# part 1

nice = 0
bad_substrs = ['ab', 'cd', 'pq', 'xy']

for str in strings:
    if any(substr in str for substr in bad_substrs):
        continue

    vowels = 0
    recurring = False

    for i in range(len(str)):
        if str[i] in 'aeiou':
            vowels += 1
        if i != 0 and str[i] == str[i-1]:
            recurring = True
    
    if vowels >= 3 and recurring:
        nice += 1

print(nice)

# part 2

nice = 0

for str in strings:
    pairs = []
    repeats = False

    for i in range(len(str)):
        if i < len(str) - 2:
            pairs.append(str[i:i+2])
        if i > 1 and str[i] == str[i-2]:
            repeats = True
    
    if not repeats:
        continue
    
    for pair in pairs:
        count = len(re.findall(pair, str))
        if count >= 2:
            nice += 1
            break

print(nice)