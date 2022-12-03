input = 29000000

# part 1

houses = []

# only need to track up to input/10 number of houses because
# the elves are delivering in quantities of 10 gifts per house
for i in range(int(input/10)):
    houses.append(0)

for i in range(1, int(input/10)):
    for j in range(i, int(input/10), i):
        houses[j] += i * 10

# print first house in list >= input
for i in range(len(houses)):
    if houses[i] >= input:
        print(f'House {i} has {houses[i]} gifts')
        break


# part 2

houses = []

# ceiling division to identify new number of houses to track
for i in range(int(-(input//-11))):
    houses.append(0)

for i in range(1, int(-(input//-11))):
    for j in range(i, 50*i+1, i):
        # try/except for when an elf is trying to deliver to a house
        # that is not tracked on the houses list
        try:
            houses[j] += i * 11
        except IndexError:
            continue

# print first house in list >= input
for i in range(len(houses)):
    if houses[i] >= input:
        print(f'House {i} has {houses[i]} gifts')
        break