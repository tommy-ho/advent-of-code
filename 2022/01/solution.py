# reading input
f = open('input.txt', 'r')
lines = f.readlines()
lines = [i.strip() for i in lines]
f.close()

# part 1

elves = [0]
for line in lines:
    if line != '':
        elves[-1] += int(line)
    else:
        elves.append(0)

print(max(elves))


# part 2

elves.sort(reverse=True)
print(elves[0] + elves[1] + elves[2])