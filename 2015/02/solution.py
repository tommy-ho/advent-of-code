# reading input
f = open('input.txt', 'r')
dimensions = f.readlines()
f.close()

# part 1

total = 0

for x in dimensions:
    split = x.split('x')
    l = int(split[0])
    w = int(split[1])
    h = int(split[2].strip())
    side1 = 2 * l * w
    side2 = 2 * l * h
    side3 = 2 * w * h
    slack = min(side1, side2, side3)/2
    total += side1 + side2 + side3 + slack

print(total)

# part 2

total = 0

for x in dimensions:
    split = x.split('x')
    sides = [int(split[0]), int(split[1]), int(split[2].strip())]
    sides.sort()
    ribbon = 2 * sides[0] + 2 * sides[1]
    bow = sides[0] * sides[1] * sides[2]
    total += ribbon + bow

print(total)